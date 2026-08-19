import asyncio
async def function1():
    await asyncio.sleep(2)
    print("first function")
async def function2():
    await asyncio.sleep(3)
    print("2nd function")
async def function3():
    await asyncio.sleep(4)
    print("3rd function")
async def main():
    task = asyncio.create_task(function1())
    print(task)
    # await function1()
    # await function2()
    # await function3()
    await asyncio.gather(
        function1(),
        function2(),
        function3()
)
asyncio.run(main())


#web
import requests
async def fun1():
    url = "https://images.wallpapersden.com/image/wxl-assassins-s-creed-shadows-4k-gaming_92804.jpg"
    response = await asyncio.to_thread(requests.get, url)
    open("image1.jpg", "wb").write(response.content)
async def fun2():
    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVU1yPwsndr6O04BWNkKrKD4zsV88Suja3S8Y9_m-rtLocPtcTfM6Q_AM&s=10"
    response = await asyncio.to_thread(requests.get, url)
    open("image2.jpg", "wb").write(response.content)
async def fun3():
    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqhMe2evBINY4tnuq0mtxVmzhFwgPGfsiRa0enNSaYSA&s=10"
    response = await asyncio.to_thread(requests.get, url)
    open("image3.jpg", "wb").write(response.content)
async def main2():
    await asyncio.gather(
        fun1(),
        fun2(),
        fun3()
    )
asyncio.run(main2())
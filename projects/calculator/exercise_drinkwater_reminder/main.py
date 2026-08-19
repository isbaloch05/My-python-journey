from plyer import notification
import time
def Alert():
    notification.notify(
        title = "Drink water reminder",
       message = "Drink water" ,
       timeout= 10
    )
# while True:
    # time.sleep(7200)
    # Alert()





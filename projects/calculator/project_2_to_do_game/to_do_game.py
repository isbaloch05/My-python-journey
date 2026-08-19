tasks=[]
task={"description":"go to gym","done":True}
tasks.append(task)
print(tasks)
#to add tasks
def add_tasks(tasks):
   description= input("Enter task description:")
   new_task={"description":description,"done":False}
   tasks.append(new_task)
add_tasks(tasks)
print(tasks)
#to view tassks
def view_task(tasks):
   for index ,elements in  enumerate(tasks):
      print(index,elements)
view_task(tasks)
#the completetask
def complete_task(tasks):
    choice = int(input("Which task number is completed? "))
    index = choice - 1
    tasks[index]["done"] = True
complete_task(tasks)
# complete_task(tasks)
print(tasks)
#to delete a task
def delete_task(tasks):
   select=int(input("Which task number is to delete:"))
   index=select - 1
   del tasks[index]
delete_task(tasks)
print(tasks)
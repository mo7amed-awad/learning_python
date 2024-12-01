tasks = [{"task":"Quran", "completed":True},
         {"task":"Salah", "completed":True}, 
         {"task":"Study", "completed":False},
         {"task":"Exercise", "completed":True}, 
         {"task":"Sleep", "completed":False},
         {"task":"Visit Hamada", "completed":True}]

def main():
    message = """1 - Add tasks to a list
    2 - mark tasks as complette
    3 - view tasks
    4 - Quit"""

    while True:
        print(message)
        choice = input("Enter your choice : ") 

        if choice == "1":
            add_task()

        elif choice == "2":
            mark_task_complete()

        elif choice == "3":
            view_tasks(tasks)

        elif choice == "4":
            break
        
        else:
            print("Invalid choice, please enter a number between 1 and 4")

def add_task():
    task=input("Enter Task : ")
    task_info = {"task":task,"completed":False}
    tasks.append(task_info)
    print("Task added to the list successfully ")

def mark_task_complete():
    incomplete_tasks = [task for task in tasks if task["completed"]==False]
    if not incomplete_tasks:
        print("No Tasks to mark as complete")
        return

    for i,task in enumerate(incomplete_tasks):
        print(f"{i+1}-{task['task']}")
        print("-"*30)
    
    try:
        task_number = int(input("choose the task number to complete : "))

        if task_number < 1 or task_number > len(incomplete_tasks):
            print("Invalid Task Number")
            return
        incomplete_tasks[task_number-1]["completed"]=True
        print("Task marked completed")
    except ValueError:
        print("invalid input ,please enter number")
    # except IndexError:
    #     print("Please choose from the available tasks")

def view_tasks(task_list):

    if not task_list:
        print("No tasks to view")
        return
    
    for i,task in enumerate(task_list):
        status="✔" if task["completed"] else "❌"
        # if task["completed"]:
        #     status = "✔"
        # else:
        #     status = "❌"
        print(f'{i+1}. {task["task"]} {status}')


if __name__=="__main__":
    main()

# print("the next line will print the value of __name__")
# print(__name__)
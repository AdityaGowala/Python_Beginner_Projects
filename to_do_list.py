# add the task 
# remove tasks
# view tasks

all_tasks = []

def view_tasks():
    if len(all_tasks) == 0:
        print("No Tasks Found... Please add tasks")
    else:
        for i , task in enumerate(all_tasks , 1):
            print(f"{i}. {task}")


def add_task():
    task = input("Enter your task: ")
    all_tasks.append(task)

def remove_tasks(delete_index):
    all_tasks.pop(delete_index-1)
    return



def main():
    while True:
        view_tasks()
        decision = input("Press 'a' to add a task \nPress 'd' to remove a task \nPress 'q' to quit\n").lower().strip()
        if decision == 'a':
            add_task()
        elif decision == 'd':
            delete_index = int(input("Enter the index of the task you want to delete: "))
            remove_tasks(delete_index)
        elif decision == 'q':
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid input! Please try again.")
main()

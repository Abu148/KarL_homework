from datetime import date

class Task:
    def __init__(self, title: str, description: str, due_date: date, status: str = "Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status 
    def mark_completed(self):
        self.status = "Completed"
    def __str__(self):
        return f"Task: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}"

tk1 = Task("Title", "Creating a class", date(2004, 2, 14))
print(tk1)

tk1.mark_completed()
print("\nOnce finished: ")
print(tk1) 

class ToDoList:
    def __init__(self):
        self.tasks = [] 

    def add_task(self, task: Task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added successfully!")

    def mark_task_completed(self, title: str):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"Task '{title}' marked as completed!")
                return
        print(f"Task '{title}' not found!")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nAll Tasks:")
        for task in self.tasks:
            print(task, "\n" + "-"*30)

    def list_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if task.status == "Pending"]
        if not incomplete_tasks:
            print("No incomplete tasks.")
            return
        print("\nIncomplete Tasks:")
        for task in incomplete_tasks:
            print(task, "\n" + "-"*30)



todo = ToDoList()

task2 = Task("Buy Groceries", "Milk, Eggs, Bread", date(2025, 4, 5))


todo.add_task(task1)
todo.add_task(task2)
todo.add_task(task3)

todo.list_all_tasks()

todo.mark_task_completed("Buy Groceries")

todo.list_incomplete_tasks()

task3 = Task("Workout", "Go for a run in the morning", date(2025, 4, 6))

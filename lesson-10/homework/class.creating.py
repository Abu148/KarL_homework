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

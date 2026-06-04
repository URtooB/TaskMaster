from datetime import datetime


class Task:
    def __init__(self, task_id: int, title: str, priority: str = "Medium"):
        self.id = task_id
        self.title = title
        self.priority = priority.capitalize() # (Low / Medium / High)
        self.is_completed = False
        self.created_at = datetime.now()

    def mark_complete(self):
        self.is_completed = True

    def __repr__(self):
        status = "Y" if self.is_completed else "N"
        date_str = self.created_at.strftime("%Y-%m-%d")
        return f"[{self.id}] {status} | {self.title} ({self.priority}) | Created: {date_str}"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.id_counter = 1

    def add_task(self, title: str, priority: str = "Medium"):
        new_task = Task(self.id_counter, title, priority)
        self.tasks.append(new_task)
        self.id_counter += 1
        print(f"Success: Added '{title}' to your list!")

    def list_all_tasks(self):
        if not self.tasks:
            print("Your todo list is empty!")
            return

        print("\n--- YOUR TASK LIST ---")
        for task in self.tasks:
            print(task)
        print("----------------------\n")



# TEST CODE
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Test1", "High")
    manager.add_task("Test2", "Low")
    manager.add_task("Test3")

    manager.list_all_tasks()

    print("Task1 complete...")
    manager.tasks[0].mark_complete()

    manager.list_all_tasks()

from datetime import datetime


class Task:
    def __init__(self, task_id: int, title: str, priority: str = "Medium"):
        self.id = task_id
        self.title = title
        # priority can be: Low, Medium, High
        self.priority = priority.capitalize()
        self.is_completed = False
        self.created_at = datetime.now()

    def mark_complete(self):
        self.is_completed = True

    def __repr__(self):
        status = "✅" if self.is_completed else "❌"
        date_str = self.created_at.strftime("%Y-%m-%d")
        return f"[{self.id}] {status} | {self.title} ({self.priority}) | Created: {date_str}"


class TaskManager:
    def __init__(self):
        # This list will hold all our Task objects
        self.tasks = []
        self.id_counter = 1

    def add_task(self, title: str, priority: str = "Medium"):
        new_task = Task(self.id_counter, title, priority)
        self.tasks.append(new_task)
        self.id_counter += 1
        print(f"Success: Added '{title}' to your list!")

    def list_all_tasks(self):
        if not self.tasks:
            print("Your todo list is empty! 🎉")
            return

        print("\n--- YOUR TASK LIST ---")
        for task in self.tasks:
            print(task)
        print("----------------------\n")



# --- TEST CODE ---
if __name__ == "__main__":
    # 1. Initialize the manager
    manager = TaskManager()

    # 2. Add some test tasks
    manager.add_task("Finish Python project skeleton", "High")
    manager.add_task("Buy groceries", "Low")
    manager.add_task("Read 10 pages of a book") # Defaults to Medium

    # 3. View the tasks
    manager.list_all_tasks()

    # 4. Try marking the first task as complete
    print("Marking task 1 as complete...")
    manager.tasks[0].mark_complete()

    # 5. View them again to see if the emoji changes!
    manager.list_all_tasks()
class Task:
    def __init__(self, name, number_of_task, time_period, description=""):
        self.name = name
        self.number_of_task = number_of_task
        self.time_period = time_period
        self.description = description

    def __str__(self):
        return f"Task: {self.name}, Description: {self.description}, Time Period: {self.time_period}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def choose_func(self, func_name):
        print(f"Choosing function: {func_name} 1 add_task, 2 show_tasks, 3 remove_task, 4 clear_tasks")
        func_name = func_name.lower()
        print(f"notes: if you not yet press 1 to add task, you can not use 2, 3, 4 \n ")
        
        if func_name == "add_task" or func_name == "1":
            return self.add_task
        elif func_name == "show_tasks" or func_name == "2":
            return self.show_tasks
        elif func_name == "remove_task" or func_name == "3":
            return self.remove_task
        elif func_name == "clear_tasks" or func_name == "4":
            return self.clear_tasks
        else:
            raise ValueError(f"Function {func_name} not recognized.")

    def add_task(self, task):
        # Check if the task already exists
        lambda_task = lambda t: t.name == task.name
        if not any(map(lambda_task, self.tasks)):
            self.tasks.append(task)
            # Sort tasks by number_of_task descending (or by priority if needed)
            self.tasks.sort(key=lambda t: t.number_of_task, reverse=True)
            print(f'Task {task.name} added successfully')
        else:
            print(f'Task {task.name} already exists.')

    def show_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        for task in self.tasks:
            print(task)

    def remove_task(self, task_name):
        original_count = len(self.tasks)
        self.tasks = list(filter(lambda task: task.name != task_name, self.tasks))
        if len(self.tasks) < original_count:
            print(f"Task '{task_name}' removed.")
        else:
            print(f"Task '{task_name}' not found.")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks cleared.")
if __name__ == "__main__":
    manager = TaskManager()
    while True:
        print("\nChoose a function: 1) add_task, 2) show_tasks, 3) remove_task, 4) clear_tasks, 5) exit")
        choice = input("Enter your choice: ").strip()
        if choice == "5" or choice.lower() == "exit":
            print("Exiting...")
            break
        try:
            func = manager.choose_func(choice)
            if choice == "1" or choice.lower() == "add_task":
                name = input("Task name: ")
                number = int(input("Task number: "))
                period = input("Time period: ")
                description = input("Description (optional): ")
                task = Task(name, number, period, description)
                func(task)
            elif choice in ("2", "show_tasks"):
                func()
            elif choice in ("3", "remove_task"):
                task_name = input("Task name to remove: ")
                func(task_name)
            elif choice in ("4", "clear_tasks"):
                func()
        except Exception as e:
            print(f"Error: {e}")

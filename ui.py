class UIManager:
    
    def display_menu(self):
        print("\n============ Task Manager ============")
        print("1. Add Task")    
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Save and Exit")
        print("======================================")
        
    def get_user_input(self, prompt):
        return input(prompt)
    
    def show_tasks(self, tasks):
        if not tasks:
            print("No task found!")
        for task in tasks:
            status = "✅" if task['completed'] else "❌"
            print(
                f"{task['id']} ~ {task['title'] }: {task['description']} => {status}"
            )
    
    def show_message(self, msg):
        print(msg)

class UIManager:
    
    @staticmethod
    def display_menu():
        print("\n============ Task Manager ============")
        print("1. Add Task")    
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Mark task as incomplete")
        print("7. show all completed tasks")
        print("8. show all incomplete tasks")
        print("9. Save and Exit")
        print("======================================")
        
    @staticmethod    
    def get_user_input(prompt):
        return input(prompt)
    
    @staticmethod
    def show_tasks(tasks):
        if not tasks:
            print("No task found!")
        for task in tasks:
            status = "✅" if task['completed'] else "❌"
            print(
                f"------------- Task ID: {task['id']} ---------------\n"
                f"Title: {task['title']}\n"
                f"Description: {task['description']}\n"
                f"Status: {status}\n"
                f"Creation Date: {task['creationDate']}\n"
                f"Due Date: {task['dueDate']}\n"
                "----------------------------------------\n"
            )

    @staticmethod
    def show_message(msg):
        print(msg)

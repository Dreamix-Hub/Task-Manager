"""
This module provides the UIManager class for handling user interactions, including displaying menus,
getting user input, and showing tasks or messages.
"""

class UIManager:
    @staticmethod
    def display_menu():
        """
        Display the main menu for the Task Manager application.
        """
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
        """
        Get input from the user.

        Args:
            prompt (str): The prompt message to display to the user.

        Returns:
            str: The user input.
        """
        return input(prompt)

    @staticmethod
    def show_tasks(tasks):
        """
        Display a list of tasks.

        Args:
            tasks (list): A list of task dictionaries to display.
        """
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
        """
        Display a message to the user.

        Args:
            msg (str): The message to display.
        """
        print(msg)

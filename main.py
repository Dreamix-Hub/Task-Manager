"""
This module contains the main entry point for the Task Manager application.
It initializes the necessary components and provides a CLI-based menu for user interaction.
"""

from ui import UIManager
from task_manager import TaskManager
from date import Date
from filter_tasks import FilterTask
from storage_manager import StorageManager

def main():
    """
    The main function initializes the Task Manager application and handles user input
    through a CLI-based menu.
    """
    task_manager = TaskManager()
    ui = UIManager()
    stroage_manager = StorageManager()

    while True:
        ui.display_menu()  # Display the CLI-based menu

        choice = int(ui.get_user_input("Enter your choice: "))

        match(choice):
            case 1:
                # Add a new task
                title = ui.get_user_input("Title: ")
                description = ui.get_user_input("Description: ")
                due_date = ui.get_user_input("Due date (YYYY-MM-DD): ")
                task = {
                    "id": TaskManager().get_task_id() + 1,
                    "title": title,
                    "description": description,
                    "completed": False,
                    "creationDate": Date().get_current_date(),  # Get the current date
                    "dueDate": Date().validate_date(due_date)  # Validate the due date
                }
                task_manager.add_task(task)

            case 2:
                # Show all tasks
                task_manager.show_task()

            case 3:
                # Update an existing task
                task_id = int(ui.get_user_input("Enter task id to update: "))
                title = ui.get_user_input("Title: ")
                description = ui.get_user_input("Description: ")
                if task_manager.update_task(task_id, title, description):
                    print("Task updated successfully ✅")
                else:
                    print("Error while updating task ❌")

            case 4:
                # Delete a task
                task_id = int(ui.get_user_input("Enter task id to delete: "))
                if task_manager.delete_task(task_id):
                    print("Task deleted successfully ✅")
                else:
                    print("Error while deleting task ❌")

            case 5:
                # Mark a task as completed
                task_id = int(ui.get_user_input("Enter task id to mark as completed: "))
                if task_manager.mark_task_as_completed(task_id):
                    print("done ✅")
                else:
                    print(f"No task with id {task_id}")

            case 6:
                # Mark a task as incomplete
                task_id = int(ui.get_user_input("Enter task id to mark as incomplete: "))
                if task_manager.mark_task_as_incompleted(task_id):
                    print("done ✅")
                else:
                    print(f"No task with id {task_id}")

            case 7:
                # Show all completed tasks
                ui.show_message("\n------- All completed tasks -------\n")
                ui.show_tasks(FilterTask(stroage_manager.load_task()).filter_completed_tasks())

            case 8:
                # Show all incomplete tasks
                ui.show_message("\n------- All incompleted tasks -------\n")
                ui.show_tasks(FilterTask(stroage_manager.load_task()).filter_incompleted_tasks())

            case 9:
                # Exit the application
                break

            case _:
                print("Invalid input")

main()
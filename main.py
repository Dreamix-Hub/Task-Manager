from ui import UIManager
from storage_manager import StorageManager
from task_manager import TaskManager

def main():
    task_manager = TaskManager()
    ui = UIManager()
    storage_manager = StorageManager()
    
    while True:
        ui.display_menu() # display the CLI based menu
        
        choice = int(ui.get_user_input("Enter your choice: "))
        
        match(choice):
            case 1:
                title = ui.get_user_input("Title: ")
                description = ui.get_user_input("Description: ")
                task = {
                    "id": TaskManager().get_task_id() + 1,
                    "title":title,
                    "description":description,
                    "completed":False
                }
                task_manager.add_task(task)        
            
            case 2:
                task_manager.show_task()
            
            case 3:
                task_id = int(ui.get_user_input("Enter task id to update: "))
                title = ui.get_user_input("Title: ")
                description = ui.get_user_input("Description: ")
                if task_manager.update_task(task_id, title, description):
                    print("Task updated successfully ✅")
                else:
                    print("Error while updating task ❌")
            
            case 4:
                task_id = int(ui.get_user_input("Enter task id to delete: "))
                if task_manager.delete_task(task_id):
                    print("Task deleted successfully ✅")
                else:
                    print("Error while deleting task ❌")
            
            case 5:
                task_id = int(ui.get_user_input("Enter task id to mark as completed: "))
                
                if task_manager.mark_task_as_completed(task_id):
                    print("done ✅")
                else:
                    print(f"No task with id {task_id}")
                
            case 6:
                break
            
            case _:
                print("Invalid input")
        

main()
from storage_manager import StorageManager
from ui import UIManager

class TaskManager:
    def __init__(self):
        self.tasks = StorageManager().load_task()  # Load tasks from the file into the instance variable

    # return the id of last task in the list and if no task found it will return 0
    def get_task_id(self):
        task_list = self.tasks
        last_id =   task_list[-1].get('id', 0) if task_list else 0        
        return last_id 
        
    def add_task(self, task):
        self.tasks.append(task)
        StorageManager().save_task(self.tasks) # save the tasks' list in tasks.json file
        UIManager().show_message("Task Added successfully ✅")
    
    def show_task(self):
        UIManager().show_tasks(StorageManager().load_task())
    
    def update_task(self, task_id, title, description):
        for task in self.tasks:
            if task_id == task['id']:
                task['title'] = title
                task['description'] = description 
                StorageManager().save_task(self.tasks)
                return True
        else:
            print(f"No task with id {task_id}")
            return False
    
    def delete_task(self, task_id):
        for task in self.tasks:
            if task_id == task['id']:
                self.tasks.remove(task)
                StorageManager().save_task(self.tasks)
                return True
        return False  # Return False only after checking all tasks
    
    def mark_task_as_completed(self, task_id):
        for task in self.tasks:
            if task_id == task['id']:
                task['completed'] = True
                StorageManager().save_task(self.tasks)
                return True
        return False  # Return False only after checking all tasks
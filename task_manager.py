"""
This module provides the TaskManager class for managing tasks, including adding, updating,
deleting, and marking tasks as completed or incomplete.
"""

from storage_manager import StorageManager
from ui import UIManager
from search import Search

class TaskManager:
    def __init__(self):
        """
        Initialize the TaskManager with tasks loaded from the storage.
        """
        self.tasks = StorageManager().load_task()

    def get_task_id(self):
        """
        Get the ID of the last task in the list.

        Returns:
            int: The ID of the last task, or 0 if no tasks exist.
        """
        task_list = self.tasks
        last_id = task_list[-1].get('id', 0) if task_list else 0
        return last_id

    def add_task(self, task):
        """
        Add a new task to the task list and save it to storage.

        Args:
            task (dict): The task dictionary to add.
        """
        self.tasks.append(task)
        StorageManager().save_task(self.tasks)
        UIManager().show_message("Task Added successfully ✅")

    @staticmethod
    def show_task():
        """
        Display all tasks using the UIManager.
        """
        UIManager().show_tasks(StorageManager().load_task())

    def update_task(self, task_id, title, description):
        """
        Update the title and description of a task by its ID.

        Args:
            task_id (int): The ID of the task to update.
            title (str): The new title for the task.
            description (str): The new description for the task.

        Returns:
            bool: True if the task was updated, False otherwise.
        """
        task = Search(self.tasks).search_task(task_id)
        if task:
            task['title'] = title
            task['description'] = description
            StorageManager().save_task(self.tasks)
            return True
        else:
            print(f"No task with id {task_id}")
            return False

    def delete_task(self, task_id):
        """
        Delete a task by its ID.

        Args:
            task_id (int): The ID of the task to delete.

        Returns:
            bool: True if the task was deleted, False otherwise.
        """
        task = Search(self.tasks).search_task(task_id)
        if task:
            self.tasks.remove(task)
            StorageManager().save_task(self.tasks)
            return True
        return False

    def mark_task_as_completed(self, task_id):
        """
        Mark a task as completed by its ID.

        Args:
            task_id (int): The ID of the task to mark as completed.

        Returns:
            bool: True if the task was marked as completed, False otherwise.
        """
        task = Search(self.tasks).search_task(task_id)
        if task:
            task['completed'] = True
            StorageManager().save_task(self.tasks)
            return True
        return False

    def mark_task_as_incompleted(self, task_id):
        """
        Mark a task as incomplete by its ID.

        Args:
            task_id (int): The ID of the task to mark as incomplete.

        Returns:
            bool: True if the task was marked as incomplete, False otherwise.
        """
        task = Search(self.tasks).search_task(task_id)
        if task:
            task['completed'] = False
            StorageManager().save_task(self.tasks)
            return True
        return False

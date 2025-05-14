"""
This module provides a class for searching tasks by their ID.
"""

class Search:
    def __init__(self, task):
        """
        Initialize the Search class with a list of tasks.

        Args:
            task (list): A list of task dictionaries.
        """
        self.tasks = task

    def search_task(self, id):
        """
        Search for a task by its ID.

        Args:
            id (int): The ID of the task to search for.

        Returns:
            dict: The task dictionary if found, otherwise an empty dictionary.
        """
        for task in self.tasks:
            if task['id'] == id:
                return task
        return {}
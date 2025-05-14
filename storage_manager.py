"""
This module provides functionality for saving and loading tasks to and from a JSON file.
"""

import json

class StorageManager:
    def __init__(self, filename='tasks.json'):
        """
        Initialize the StorageManager with a filename.

        Args:
            filename (str): The name of the file to save/load tasks.
        """
        self.filename = filename

    def save_task(self, task):
        """
        Save a list of tasks to the JSON file.

        Args:
            task (list): A list of task dictionaries to save.

        Returns:
            None
        """
        try:
            with open(self.filename, 'w') as f:
                json.dump([t for t in task], f, indent=4)
        except FileNotFoundError:
            return []

    def load_task(self):
        """
        Load tasks from the JSON file.

        Returns:
            list: A list of task dictionaries loaded from the file.
        """
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [task for task in data]
        except FileNotFoundError:
            print("NO task left!")

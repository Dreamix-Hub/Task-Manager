"""
This module provides functionality for filtering tasks based on their completion status.
"""

class FilterTask:
    def __init__(self, task):
        """
        Initialize the FilterTask class with a list of tasks.

        Args:
            task (list): A list of task dictionaries.
        """
        self.tasks = task

    def filter_completed_tasks(self):
        """
        Filter and return all completed tasks.

        Returns:
            list: A list of completed task dictionaries.
        """
        completed_tasks = [task for task in self.tasks if task['completed']]
        return completed_tasks

    def filter_incompleted_tasks(self):
        """
        Filter and return all incomplete tasks.

        Returns:
            list: A list of incomplete task dictionaries.
        """
        incompleted_tasks = [task for task in self.tasks if not task['completed']]
        return incompleted_tasks
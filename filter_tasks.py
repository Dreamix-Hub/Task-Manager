
class FilterTask:
    
    def __init__(self,task):
        self.tasks = task
    
    # filter the completed tasks and return them
    
    def filter_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task['completed']]
        return completed_tasks  
    
    # filter the incompleted tasks and return them
    def filter_incompleted_tasks(self):
        incompleted_tasks = [task for task in self.tasks if not task['completed']]
        return incompleted_tasks
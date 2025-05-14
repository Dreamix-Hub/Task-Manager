
class Search:
    def __init__(self,task):
        self.tasks = task
        # get the list of tasks from the task manager
    
    # return the task with the given id if found, otherwise return an empty dictionary
    def search_task(self, id):
        for task in self.tasks:
            if task['id'] == id:
                return task
        return {} 
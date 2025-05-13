import json

class StorageManager:
    
    def __init__(self, filename='tasks.json'):
        self.filename = filename
    
    def save_task(self,task):
        try:
            with open(self.filename, 'w') as f:
                json.dump([t for t in task], f, indent=4)
        except FileNotFoundError:
            return []
    
    def load_task(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [task for task in data]
        except FileNotFoundError:
            print("NO task left!")
    
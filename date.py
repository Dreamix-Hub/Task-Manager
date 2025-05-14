import datetime

class Date:
    
    # return the current date in YYYY-MM-DD format when the user adds a task
    @staticmethod
    def get_current_date():
        return datetime.datetime.now().strftime("%Y-%m-%d")
    
    # validate the user's input date
    @staticmethod
    def validate_date(date):
        try:
            return datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
        except Exception as e:
            print("Invalid date format 🤦")


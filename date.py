import datetime

class Date:
    """
    A utility class for handling date-related operations such as getting the current date
    and validating user-provided dates.
    """

    @staticmethod
    def get_current_date():
        """
        Returns the current date in the format YYYY-MM-DD.

        Returns:
            str: The current date formatted as YYYY-MM-DD.
        """
        return datetime.datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def validate_date(date):
        """
        Validates and formats a user-provided date string.

        Args:
            date (str): The date string to validate, expected in the format YYYY-MM-DD.

        Returns:
            str: The validated and formatted date string in YYYY-MM-DD format.

        Raises:
            ValueError: If the date string is not in the correct format.
        """
        try:
            return datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format 🤦")
            raise


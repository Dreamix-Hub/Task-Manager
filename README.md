# Task-Manager

Assignment 1 of Subject SCD (Software Construction & Development). This repository contains a CLI-based Task Manager System capable of performing CRUD operations.

## Features

- Add new tasks with a title, description, and due date.
- View all tasks with details such as title, description, status, creation date, and due date.
- Update existing tasks by modifying their title and description.
- Delete tasks by their ID.
- Mark tasks as completed or incomplete.
- Filter tasks to view only completed or incomplete ones.
- Save and load tasks from a JSON file for persistence.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Dreamix-Hub/Task-Manager.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Task-Manager
   ```

3. Ensure you have Python 3 installed. You can check your Python version with:
   ```bash
   python --version
   ```

4. Install any required dependencies (if applicable). For this project, no external dependencies are required.

## Usage

1. Run the main script to start the Task Manager application:
   ```bash
   python main.py
   ```

2. Follow the on-screen menu to perform various operations:
   - Add tasks
   - View tasks
   - Update tasks
   - Delete tasks
   - Mark tasks as completed or incomplete
   - Filter tasks

3. Tasks are automatically saved to a JSON file (`tasks.json`) for persistence.

## File Structure

- `main.py`: Entry point for the application.
- `task_manager.py`: Contains the `TaskManager` class for managing tasks.
- `ui.py`: Handles user interactions and displays menus.
- `storage_manager.py`: Manages saving and loading tasks to/from a JSON file.
- `filter_tasks.py`: Provides functionality to filter tasks based on their completion status.
- `search.py`: Contains the `Search` class for finding tasks by their ID.
- `date.py`: Utility class for handling date-related operations.

## Example

Here is an example of using the Task Manager system:

1. Run the application:
   ```bash
   python main.py
   ```

2. Select option `1` to add a new task.

3. Enter the task details when prompted:
   ```
   Title: Example Task
   Description: This is a sample task.
   Due date (YYYY-MM-DD): 2025-12-31
   ```
   The task will be added and saved to the `tasks.json` file.

4. Select option `2` to view all tasks:
   ```
   ------------- Task ID: 1 ---------------
   Title: Example Task
   Description: This is a sample task.
   Status: ❌
   Creation Date: 2025-05-16
   Due Date: 2025-12-31
   ----------------------------------------
   ```

5. Select option `3` to update a task:
   ```
   Enter task id to update: 1
   Title: Updated Task
   Description: Updated description.
   Task updated successfully ✅
   ```

6. Select option `4` to delete a task:
   ```
   Enter task id to delete: 1
   Task deleted successfully ✅
   ```

7. Select option `5` to mark a task as completed:
   ```
   Enter task id to mark as completed: 1
   done ✅
   ```

8. Select option `6` to mark a task as incomplete:
   ```
   Enter task id to mark as incomplete: 1
   done ✅
   ```

9. Select option `7` to view all completed tasks:
   ```
   ------- All completed tasks -------
   ------------- Task ID: 2 ---------------
   Title: Completed Task
   Description: This task is done.
   Status: ✅
   Creation Date: 2025-05-16
   Due Date: 2025-12-31
   ----------------------------------------
   ```

10. Select option `8` to view all incomplete tasks:
   ```
   ------- All incompleted tasks -------
   ------------- Task ID: 3 ---------------
   Title: Incomplete Task
   Description: This task is not done yet.
   Status: ❌
   Creation Date: 2025-05-16
   Due Date: 2025-12-31
   ----------------------------------------
   ```

## License

This project is for educational purposes and does not include a specific license.

import pytest
from unittest.mock import patch, MagicMock
import main  # Assuming the main script is saved as main.py

@pytest.fixture
def mock_task():
    return {
        "id": 1,
        "title": "Sample Task",
        "description": "Test description",
        "completed": False,
        "creationDate": "2024-01-01",
        "dueDate": "2024-01-10"
    }

@patch("main.Date")
@patch("main.TaskManager")
@patch("main.UIManager")
def test_handle_add_task(mock_ui, mock_tm, mock_date, mock_task):
    # Arrange
    mock_ui.return_value.get_user_input.side_effect = [
        "Test Task", "This is a task", "2025-12-31"
    ]
    mock_date.return_value.get_current_date.return_value = "2025-05-16"
    mock_date.return_value.validate_date.return_value = "2025-12-31"
    mock_tm.return_value.get_task_id.return_value = 1

    # Act
    main.handle_add_task()

    # Assert
    mock_tm.return_value.add_task.assert_called_once()
    task_arg = mock_tm.return_value.add_task.call_args[0][0]
    assert task_arg["id"] == 2
    assert task_arg["title"] == "Test Task"
    assert task_arg["description"] == "This is a task"
    assert task_arg["completed"] is False

@patch("main.TaskManager")
@patch("main.UIManager")
def test_handle_update_task_success(mock_ui, mock_tm):
    mock_ui.return_value.get_user_input.side_effect = ["1", "Updated", "Updated Desc"]
    mock_tm.return_value.update_task.return_value = True

    main.handle_update_task()
    mock_tm.return_value.update_task.assert_called_once_with(1, "Updated", "Updated Desc")

@patch("main.TaskManager")
@patch("main.UIManager")
def test_handle_update_task_failure(mock_ui, mock_tm):
    mock_ui.return_value.get_user_input.side_effect = ["999", "Title", "Desc"]
    mock_tm.return_value.update_task.return_value = False

    main.handle_update_task()
    mock_tm.return_value.update_task.assert_called_once_with(999, "Title", "Desc")

@patch("main.TaskManager")
@patch("main.UIManager")
def test_handle_delete_task_success(mock_ui, mock_tm):
    mock_ui.return_value.get_user_input.return_value = "1"
    mock_tm.return_value.delete_task.return_value = True

    main.handle_delete_task()
    mock_tm.return_value.delete_task.assert_called_once_with(1)

@patch("main.TaskManager")
@patch("main.UIManager")
def test_handle_mark_completed_task(mock_ui, mock_tm):
    mock_ui.return_value.get_user_input.return_value = "1"
    mock_tm.return_value.mark_task_as_completed.return_value = True

    main.handle_mark_completed_task()
    mock_tm.return_value.mark_task_as_completed.assert_called_once_with(1)

@patch("main.TaskManager")
@patch("main.UIManager")
def test_handle_mark_incompleted_task(mock_ui, mock_tm):
    mock_ui.return_value.get_user_input.return_value = "1"
    mock_tm.return_value.mark_task_as_incompleted.return_value = True

    main.handle_mark_incompleted_task()
    mock_tm.return_value.mark_task_as_incompleted.assert_called_once_with(1)

@patch("main.FilterTask")
@patch("main.StorageManager")
@patch("main.UIManager")
def test_show_completed_tasks(mock_ui, mock_storage, mock_filter):
    mock_tasks = [{"id": 1, "title": "Done", "completed": True}]
    mock_storage.return_value.load_task.return_value = mock_tasks
    mock_filter.return_value.filter_completed_tasks.return_value = mock_tasks

    main.ui.show_message("\n------- All completed tasks -------\n")
    main.ui.show_tasks(mock_tasks)

    mock_filter.return_value.filter_completed_tasks.assert_called_once()
    mock_ui.return_value.show_tasks.assert_called_once_with(mock_tasks)

import pytest
from unittest.mock import patch, MagicMock
from task_manager import TaskManager

@pytest.fixture
def sample_tasks():
    return [
        {"id": 1, "title": "Test 1", "description": "Desc 1", "completed": False},
        {"id": 2, "title": "Test 2", "description": "Desc 2", "completed": True}
    ]

@patch("task_manager.StorageManager")
def test_get_task_id(mock_storage, sample_tasks):
    mock_storage.return_value.load_task.return_value = sample_tasks
    tm = TaskManager()
    assert tm.get_task_id() == 2

@patch("task_manager.StorageManager")
@patch("task_manager.UIManager")
def test_add_task(mock_ui, mock_storage, sample_tasks):
    mock_storage.return_value.load_task.return_value = sample_tasks.copy()
    tm = TaskManager()
    new_task = {"id": 3, "title": "New Task", "description": "Test", "completed": False}
    tm.add_task(new_task)
    assert new_task in tm.tasks
    mock_storage.return_value.save_task.assert_called_once()
    mock_ui.return_value.show_message.assert_called_once_with("Task Added successfully ✅")

@patch("task_manager.StorageManager")
@patch("task_manager.Search")
def test_update_task_success(mock_search, mock_storage, sample_tasks):
    updated_title = "Updated Title"
    updated_desc = "Updated Description"
    mock_storage.return_value.load_task.return_value = sample_tasks.copy()
    tm = TaskManager()
    task = sample_tasks[0]
    mock_search.return_value.search_task.return_value = task
    result = tm.update_task(1, updated_title, updated_desc)
    assert result is True
    assert task["title"] == updated_title
    assert task["description"] == updated_desc
    mock_storage.return_value.save_task.assert_called_once()

@patch("task_manager.StorageManager")
@patch("task_manager.Search")
def test_update_task_failure(mock_search, mock_storage):
    mock_storage.return_value.load_task.return_value = []
    tm = TaskManager()
    mock_search.return_value.search_task.return_value = None
    result = tm.update_task(99, "X", "Y")
    assert result is False

@patch("task_manager.StorageManager")
@patch("task_manager.Search")
def test_delete_task(mock_search, mock_storage, sample_tasks):
    task_to_delete = sample_tasks[0]
    mock_storage.return_value.load_task.return_value = sample_tasks.copy()
    tm = TaskManager()
    mock_search.return_value.search_task.return_value = task_to_delete
    result = tm.delete_task(1)
    assert result is True
    assert task_to_delete not in tm.tasks
    mock_storage.return_value.save_task.assert_called_once()

@patch("task_manager.StorageManager")
@patch("task_manager.Search")
def test_mark_task_as_completed(mock_search, mock_storage, sample_tasks):
    mock_storage.return_value.load_task.return_value = sample_tasks.copy()
    tm = TaskManager()
    task = sample_tasks[0]
    mock_search.return_value.search_task.return_value = task
    result = tm.mark_task_as_completed(1)
    assert result is True
    assert task["completed"] is True
    mock_storage.return_value.save_task.assert_called_once()

@patch("task_manager.StorageManager")
@patch("task_manager.Search")
def test_mark_task_as_incompleted(mock_search, mock_storage, sample_tasks):
    mock_storage.return_value.load_task.return_value = sample_tasks.copy()
    tm = TaskManager()
    task = sample_tasks[1]
    mock_search.return_value.search_task.return_value = task
    result = tm.mark_task_as_incompleted(2)
    assert result is True
    assert task["completed"] is False
    mock_storage.return_value.save_task.assert_called_once()

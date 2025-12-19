from src.task_manager import create_task, list_tasks

def test_create_task():
    task = create_task("Estudar Python", "CRUD de tarefas")
    assert task.title == "Estudar Python"
    assert len(list_tasks()) > 0

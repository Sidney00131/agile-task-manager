import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.task_manager import create_task, list_tasks, delete_task, tasks


def setup_function():
    tasks.clear()


def test_create_task():
    task = create_task("Estudar Python", "Criar CRUD")
    assert task.title == "Estudar Python"
    assert task.priority == "Média"
    assert len(list_tasks()) == 1


def test_delete_task():
    create_task("Teste", "Remover tarefa")
    delete_task(0)
    assert len(list_tasks()) == 0

class Task:
    def __init__(self, title, description, priority="Média"):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False


tasks = []

def create_task(title, description, priority="Média"):
    task = Task(title, description, priority)
    tasks.append(task)
    return task

def list_tasks():
    return tasks

def update_task(index, title, description, priority="Média"):
    tasks[index].title = title
    tasks[index].description = description
    tasks[index].priority = priority

def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)

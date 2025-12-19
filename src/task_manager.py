class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

tasks = []

def create_task(title, description):
    task = Task(title, description)
    tasks.append(task)
    return task

def list_tasks():
    return [task.title for task in tasks]


def update_task(index, title, description):
    tasks[index].title = title
    tasks[index].description = description

def delete_task(index):
    tasks.pop(index)

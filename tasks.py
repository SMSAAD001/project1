tasks = []

def add_task(task):
    if task:
        tasks.append(task)

def view_tasks():
    return tasks

def clear_tasks():
    tasks.clear()

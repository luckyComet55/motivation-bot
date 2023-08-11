from typing import Dict, List
from task import Task

__database: Dict[str, List[Task]] = {}

def save_task(username: str, task: Task) -> bool:
    if username not in __database:
        __database[username] = []
    __database[username].append(task)
    return True

def get_task(username: str) -> List[Task]:
    if username not in __database:
        __database[username] = []
    return __database[username]
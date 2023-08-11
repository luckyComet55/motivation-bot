from typing import Dict, List

__database: Dict[str, List] = {}

def save_task(username: str, task: List[str]) -> bool:
    if username not in __database:
        __database[username] = []
    __database[username].append(task)
    return True

def get_task(username: str) -> List[str]:
    if username not in __database:
        __database[username] = []
    return __database[username]
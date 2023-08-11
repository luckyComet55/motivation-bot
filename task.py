import datetime

class Task:
    name: str
    deadline: datetime.datetime
    reminder_delay: str

    def __init__(self, name: str, deadline: datetime.datetime, reminder_delay: str) -> None:
        self.name = name
        self.deadline = deadline
        self.reminder_delay = reminder_delay

    def __str__(self) -> str:
        return f'{self.name} finishes at {self.deadline}, delay {self.reminder_delay}'
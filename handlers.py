import strings
import datetime
from task import Task

def parse_new_task(args: list[str]) -> Task | None:
    args_len = len(args)
    if args_len < 3:
        return None
    task_name_end = args_len - 2
    name = ' '.join(args[:task_name_end])
    dt = args[task_name_end]
    delay = args[task_name_end + 1]
    deadline_parsed = datetime.datetime.strptime(dt, '%d.%m.%YT%H:%M')
    task = Task(name, deadline_parsed, delay)
    return task

def parse_help(args: list[str]) -> str:
    args_len = len(args)
    if args_len == 0:
        return strings.manual_general
    if args_len > 1:
        return 'Должна быть только одна команда'
    cmd = args[0]
    if cmd not in strings.manual_specific:
        return strings.err_no_such_command
    return strings.manual_specific[cmd]
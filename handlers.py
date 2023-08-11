import strings

def parse_new_task(args: list[str]) -> list | None:
    args_len = len(args)
    if args_len < 3:
        return None
    res = []
    task_name_end = args_len - 2
    res.append(' '.join(args[:task_name_end]))
    res += args[task_name_end:]
    print(res)
    return res

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
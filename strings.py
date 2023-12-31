hello_msg_sequence=[
    'Привет!',
    'Этот бот позволяет оставлять заметки для напоминаний',
    'Бот находится на стадии разработки, возможны ошибки и изменения функционала',
    'Для подробной инструкции пиши /help'
]

echo_msg_storage=[
    'Разговаривать обычными словами я не умею :('
]

manual_general='''
Чтобы увидеть подробную инструкцию для команды, введите /help <комманда>

/add_task <имя_задачи> <дедлайн> <частота_напоминаний> -- добавить задачу\n
/get_task -- получить все задачи
'''

manual_specific={
    'add_task': '''
/add_task <имя_задачи> <дедлайн> <частота_напоминаний> -- добавить задачу\n
<имя_задачи> -- может состоять из нескольких разделенных пробелами слов\n
<дедлайн> -- дата дедлайна задачи в формате "dd.mm.yyyyThh:mm". К примеру 11.08.2023T12:00\n
<частота_напоминаний> -- число+формат_времени. К примеру 30m -- 30 минут.
Поддериживаются форматы времени m, h, d (минута, час, день)
'''
}

# COMMANDS
ADD_ASSIGNMENT='add_task'
GET_ASSIGNMENTS='get_task'
HELP='help'
START='start'

# ERRORS!
err_incorrect_args='Аргументы переданы некорректно'
err_internal='Внутренняя ошибка'
err_no_such_command='Нет такой команды'
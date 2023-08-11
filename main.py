from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
from random import randint
import strings
import handlers
import config
import repository as repo
import os


if not os.path.exists('./.env'):
    print('.env file not found')
    exit(1)

load_dotenv()
api_key = os.environ['API_KEY']


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for msg in strings.hello_msg_sequence:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

async def handle_echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    idx = randint(0, len(strings.echo_msg_storage) - 1)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=strings.echo_msg_storage[idx])

async def handle_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    msg = handlers.parse_help(args)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


async def handle_new_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    parsed_args = handlers.parse_new_task(args)
    msg = ''
    if parsed_args is None:
        msg = strings.err_incorrect_args
    else:
        username = update.effective_user.username
        res = repo.save_task(username, parsed_args)
        if not res:
            msg = strings.err_internal
        else:
            msg = f'Имя задачи {parsed_args[0]}, дедлайн {parsed_args[1]}'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

async def handle_get_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    res = repo.get_task(username)
    msg = f'Всего задач {len(res)}'
    for r in res:
        msg += f'\nИмя задачи {r[0]}, дедлайн {r[1]}'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

if __name__ == '__main__':
    app = config.app_config(api_key)
    start_handler = CommandHandler(strings.START, handle_start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_echo)
    new_task_handler = CommandHandler(strings.ADD_ASSIGNMENT, handle_new_task)
    get_task_handler = CommandHandler(strings.GET_ASSIGNMENTS, handle_get_task)
    help_handler = CommandHandler(strings.HELP, handle_help)
    config.handlers_config(app,
                           start_handler,
                           echo_handler,
                           new_task_handler,
                           help_handler,
                           get_task_handler
                           )

    app.run_polling()
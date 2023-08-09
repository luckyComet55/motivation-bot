from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from random import randint
from config import hello_msg_sequence, echo_msg_storage, manual_general, manual_specific
import os

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()
api_key = os.environ['API_KEY']

async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for msg in hello_msg_sequence:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

async def handle_echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    idx = randint(0, len(echo_msg_storage) - 1)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=echo_msg_storage[idx])

def parse_help(args: list[str]):
    args_len = len(args)
    if args_len == 0:
        return manual_general
    if args_len > 1:
        return 'Должна быть только одна команда'
    cmd = args[0]
    if cmd not in manual_specific:
        return 'Нет такой команды'
    return manual_specific[cmd]

async def handle_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    msg = parse_help(args)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def parse_new_ass(args: list[str]):
    args_len = len(args)
    if args_len < 3:
        return None
    res = []
    assignment_name_end = args_len - 2
    res.append(' '.join(args[:assignment_name_end]))
    res += args[assignment_name_end:]
    print(res)
    return res

async def handle_assignment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    parsed_args = parse_new_ass(args)
    msg = ''
    if parsed_args is None:
        msg = 'Надо три (3!) аргумента'
    else:
        msg = f'Имя задачи {parsed_args[0]}'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def bot_initial_config(token: str):
    return ApplicationBuilder().token(token).build()

if __name__ == '__main__':
    app = bot_initial_config(api_key)
    start_handler = CommandHandler('start', handle_start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_echo)
    ass_handler = CommandHandler('add_assignment', handle_assignment)
    help_handler = CommandHandler('help', handle_help)
    app.add_handler(start_handler)
    app.add_handler(echo_handler)
    app.add_handler(ass_handler)
    app.add_handler(help_handler)

    app.run_polling()
from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from random import randint
from config import hello_msg_sequence, echo_msg_storage
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

def bot_initial_config(token: str):
    return ApplicationBuilder().token(token).build()

if __name__ == '__main__':
    app = bot_initial_config(api_key)
    start_handler = CommandHandler('start', handle_start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_echo)
    app.add_handler(start_handler)
    app.add_handler(echo_handler)

    app.run_polling()
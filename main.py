from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()
api_key = os.environ['API_KEY']

async def handleStart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='YOOOOOOO DO YOUR JOB MOZEFUCKAAAAA')


def bot_initial_config(token: str):
    return ApplicationBuilder().token(token).build()

if __name__ == '__main__':
    app = bot_initial_config(api_key)
    start_handler = CommandHandler('start', handleStart)
    app.add_handler(start_handler)

    app.run_polling()
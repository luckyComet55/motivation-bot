from telegram.ext import ApplicationBuilder, Application

def app_config(token: str) -> Application:
    return ApplicationBuilder().token(token).build()

def handlers_config(app: Application, *args):
    for handler in args:
        app.add_handler(handler)
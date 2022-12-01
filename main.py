# from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import *

app = ApplicationBuilder().token("YOUR_TELEGRAM_TOKEN_KEY").build()
                                # YOUR_TELEGRAM_TOKEN_KEY
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("calc", calc_command))
print('Server run')
app.run_polling()

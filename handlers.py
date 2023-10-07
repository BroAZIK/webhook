from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):

    print(update.effective_user.first_name)
    print(update.message.text)
    print("\n**************\n")

    update.message.reply_text(
        'Hello!, welcome to bot!'
    )
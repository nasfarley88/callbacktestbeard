import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async
from skybeard.beards import Beard


logger = logging.getLogger(__name__)

# Adapted from https://github.com/python-telegram-bot/python-telegram-bot/blob/46657afa95bd720bb1319fcb9bc1e8cae82e02b9/examples/inlinekeyboard.py


class CallbackTestBeard(Beard):
    """Simple callback button example for skybeard-2

    Type /callbackstart to begin."""

    def initialise(self):
        self.disp.add_handler(CommandHandler("callbackstart", self.start))
        self.disp.add_handler(CallbackQueryHandler(self.button))

        self.keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Option 1", callback_data='1'),
             InlineKeyboardButton("Option 2", callback_data='2')],
            [InlineKeyboardButton("Option 3", callback_data='3')],
        ])


    def start(self, bot, update):
        update.message.reply_text('Please choose:', reply_markup=self.keyboard)

    def button(self, bot, update):
        query = update.callback_query

        bot.editMessageText(text="Selected option: %s" % query.data,
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id,
                            reply_markup=self.keyboard)

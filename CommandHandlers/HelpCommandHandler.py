import logging

from telegram.ext import CommandHandler
from telegram import ParseMode


class HelpCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self):
        super().__init__('help', self.__handle)

    @staticmethod
    def __handle(bot, update):
        logging.info('/help: entered')

        text = '\n'.join([
            '/alias _<alias>_ - Add the specified alias so you can be called with it in the current chat',
            '/list - List all your aliases for the current chat',
            '/remove _<alias>_ - Remove the specified alias so you cannot be called with it in the current chat',
            '/clear - Remove all your aliases in the current chat',
            '/help - Show this help message'])
        bot.send_message(chat_id=update.message.chat_id,
                         text=text,
                         parse_mode=ParseMode.MARKDOWN)

        logging.info('/help: exited')

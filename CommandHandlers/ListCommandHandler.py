import logging

from telegram.ext import CommandHandler
from telegram.constants import MAX_MESSAGE_LENGTH


class ListCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, aliases_storage):
        super().__init__('list', self.__handle)
        self._aliases_storage = aliases_storage

    def __handle(self, bot, update):
        logging.info('/list: entered')

        message = update.message
        chat_id = message.chat_id
        from_username = message.from_user.username

        aliases = self._aliases_storage.get_aliases(from_username, chat_id)

        if not any(aliases):
            bot.send_message(chat_id=chat_id,
                             text="@%s, you have no aliases for this chat" % from_username)
        else:
            text = "@%s, your aliases for this chat are:\n%s" % (from_username, '\n'.join(aliases))
            while len(text) > MAX_MESSAGE_LENGTH:
                part = text[0:MAX_MESSAGE_LENGTH]
                bot.send_message(chat_id=chat_id, text=part)
                text = text[MAX_MESSAGE_LENGTH:]

            if len(text) > 0:
                bot.send_message(chat_id=chat_id, text=text)

        logging.info('/list: exited')

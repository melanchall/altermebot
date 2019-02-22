import logging

from telegram.ext import CommandHandler


class OffCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, aliases_storage):
        super().__init__('off', self.__handle)
        self._aliases_storage = aliases_storage

    def __handle(self, bot, update):
        logging.info('/off: entered')

        message = update.message
        chat_id = message.chat_id
        user_id = message.from_user.id

        self._aliases_storage.disable_aliasing(user_id, chat_id)

        logging.info('/off: exited')

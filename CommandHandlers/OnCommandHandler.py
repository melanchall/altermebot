import logging

from telegram.ext import CommandHandler


class OnCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, aliases_storage):
        super().__init__('on', self.__handle)
        self._aliases_storage = aliases_storage

    def __handle(self, bot, update):
        logging.info('/on: entered')

        message = update.message
        chat_id = message.chat_id
        user_id = message.from_user.id

        self._aliases_storage.enable_aliasing(user_id, chat_id)

        logging.info('/on: exited')

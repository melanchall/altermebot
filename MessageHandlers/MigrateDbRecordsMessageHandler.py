import logging

from telegram.ext import MessageHandler, Filters


class MigrateDbRecordsMessageHandler(MessageHandler):
    """description of class"""

    def __init__(self, aliases_storage, aliases_storage2):
        super().__init__(Filters.text, self.__handle)
        self._aliases_storage = aliases_storage
        self.aliases_storage2 = aliases_storage2

    def __handle(self, bot, update):
        logging.info('message to try migrate DB records: entered')

        message = update.message
        chat_id = message.chat_id
        username = message.from_user.username
        user_id = message.from_user.id

        if username:
            old_aliases = self._aliases_storage.get_aliases(username, chat_id)
            for old_alias in old_aliases:
                self.aliases_storage2.add_alias(user_id, chat_id, old_alias)

        logging.info('message to try migrate DB records: exited')

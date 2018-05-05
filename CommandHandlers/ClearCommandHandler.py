import logging

from telegram.ext import CommandHandler


class ClearCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, aliases_storage):
        super().__init__('clear', self.__handle)
        self._aliases_storage = aliases_storage

    def __handle(self, bot, update):
        logging.info('/clear: entered')

        message = update.message
        chat_id = message.chat_id
        from_username = message.from_user.username

        self._aliases_storage.remove_all_aliases(from_username, chat_id)

        bot.send_message(chat_id=chat_id,
                         text="@%s, all your aliases for this chat were successfully removed" % from_username)

        logging.info('/clear: exited')

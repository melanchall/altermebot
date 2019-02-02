import logging

from telegram.ext import CommandHandler
from telegram import ParseMode


class ClearCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, aliases_storage):
        super().__init__('clear', self.__handle)
        self._aliases_storage = aliases_storage

    def __handle(self, bot, update):
        logging.info('/clear: entered')

        message = update.message
        chat_id = message.chat_id
        user_id = message.from_user.id

        user = message.from_user
        mention = user.username
        parse_mode = None
        if not mention:
            mention = '[%s](tg://user?id=%d)' % (user.full_name, user_id)
            parse_mode = ParseMode.MARKDOWN
        else:
            mention = "@%s" % mention

        self._aliases_storage.remove_all_aliases(user_id, chat_id)

        bot.send_message(chat_id=chat_id,
                         text="%s, all your aliases for this chat were successfully removed" % mention,
                         parse_mode=parse_mode)

        logging.info('/clear: exited')

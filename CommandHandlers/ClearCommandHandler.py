from telegram.ext import CommandHandler
from telegram import ParseMode

from Localization.Strings import Strings


class ClearCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, db_manager, localizer):
        super().__init__('clear', self.__handle)
        self._db_manager = db_manager
        self._localizer = localizer

    def __handle(self, bot, update):
        message = update.message
        chat_id = message.chat_id
        user_id = message.from_user.id
        localizer = self._localizer.get_localizer(update)

        user = message.from_user
        mention = user.username
        parse_mode = None
        if not mention:
            mention = '[%s](tg://user?id=%d)' % (user.full_name, user_id)
            parse_mode = ParseMode.MARKDOWN
        else:
            mention = "@%s" % mention

        self._db_manager.remove_all_aliases(user_id, chat_id)

        bot.send_message(chat_id=chat_id,
                         text=localizer(Strings.ALL_ALIASES_REMOVED) % mention,
                         parse_mode=parse_mode)

        self._db_manager.log_command(user_id, chat_id, 'clear', 'OK')

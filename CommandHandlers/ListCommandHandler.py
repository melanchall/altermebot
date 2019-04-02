from telegram.ext import CommandHandler
from telegram.constants import MAX_MESSAGE_LENGTH
from telegram import ParseMode

from Localization.Strings import Strings


class ListCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, db_manager, localizer):
        super().__init__('list', self.__handle)
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

        aliases = self._db_manager.get_aliases(user_id, chat_id)

        if not any(aliases):
            bot.send_message(chat_id=chat_id,
                             text=localizer(Strings.ALIASES_LIST_IS_EMPTY) % mention,
                             parse_mode=parse_mode)
        else:
            text = localizer(Strings.ALIASES_LIST) % (mention, '\n'.join(aliases))
            while len(text) > MAX_MESSAGE_LENGTH:
                part = text[0:MAX_MESSAGE_LENGTH]
                bot.send_message(chat_id=chat_id, text=part, parse_mode=parse_mode)
                text = text[MAX_MESSAGE_LENGTH:]

            if len(text) > 0:
                bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode)

        self._db_manager.log_command(user_id, chat_id, 'list', 'OK')

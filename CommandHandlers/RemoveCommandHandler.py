from telegram.ext import CommandHandler
from telegram import ParseMode

from BotUtils import escape_markdown
from Localization.Strings import Strings


class RemoveCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, db_manager, localizer):
        super().__init__('remove', self.__handle, pass_args=True)
        self._db_manager = db_manager
        self._localizer = localizer

    def __handle(self, bot, update, args):
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

        if not any(args):
            bot.send_message(chat_id=chat_id,
                             text=localizer(Strings.ALIAS_TO_REMOVE_IS_NOT_SPECIFIED) % mention,
                             parse_mode=parse_mode)
            self._db_manager.log_command(user_id, chat_id, 'remove', 'Rejected due to no arguments provided')
            return

        alias = ' '.join(args)
        self._db_manager.remove_alias(user_id, chat_id, alias)

        bot.send_message(chat_id=chat_id,
                         text=localizer(Strings.ALIAS_REMOVED)
                         % (escape_markdown(mention) if parse_mode is None else mention, escape_markdown(alias)),
                         parse_mode=ParseMode.MARKDOWN)

        self._db_manager.log_command(user_id, chat_id, 'remove', 'OK')

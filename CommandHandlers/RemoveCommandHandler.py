from telegram.ext import CommandHandler
from telegram import ParseMode

from BotUtils import escape_markdown


class RemoveCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, db_manager):
        super().__init__('remove', self.__handle, pass_args=True)
        self._db_manager = db_manager

    def __handle(self, bot, update, args):
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

        if not any(args):
            bot.send_message(chat_id=chat_id,
                             text="%s, you should specify alias passing it as a parameter to the /remove command"
                                  % mention,
                             parse_mode=parse_mode)
            self._db_manager.log_command(user_id, chat_id, 'remove', 'Rejected due to no arguments provided')
            return

        alias = ' '.join(args)
        self._db_manager.remove_alias(user_id, chat_id, alias)

        bot.send_message(chat_id=chat_id,
                         text="%s, alias *%s* was successfully removed"
                              % (escape_markdown(mention) if parse_mode is None else mention, escape_markdown(alias)),
                         parse_mode=ParseMode.MARKDOWN)

        self._db_manager.log_command(user_id, chat_id, 'remove', 'OK')

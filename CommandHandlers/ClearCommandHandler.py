from telegram import ParseMode

from CommandHandlers.BaseCommandHandler import BaseCommandHandler


class ClearCommandHandler(BaseCommandHandler):
    """description of class"""

    def __init__(self, db_manager):
        super().__init__('clear', db_manager)

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

        self._db_manager.remove_all_aliases(user_id, chat_id)

        bot.send_message(chat_id=chat_id,
                         text="%s, all your aliases for this chat were successfully removed" % mention,
                         parse_mode=parse_mode)

        self._db_manager.log_command(user_id, chat_id, 'clear', 'OK')

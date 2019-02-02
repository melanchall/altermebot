import logging

from telegram.ext import CommandHandler
from telegram.constants import MAX_MESSAGE_LENGTH
from telegram import ParseMode


class ListCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, aliases_storage):
        super().__init__('list', self.__handle)
        self._aliases_storage = aliases_storage

    def __handle(self, bot, update):
        logging.info('/list: entered')

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

        aliases = self._aliases_storage.get_aliases(user_id, chat_id)

        if not any(aliases):
            bot.send_message(chat_id=chat_id,
                             text="%s, you have no aliases for this chat" % mention,
                             parse_mode=parse_mode)
        else:
            text = "%s, your aliases for this chat are:\n%s" % (mention, '\n'.join(aliases))
            while len(text) > MAX_MESSAGE_LENGTH:
                part = text[0:MAX_MESSAGE_LENGTH]
                bot.send_message(chat_id=chat_id, text=part, parse_mode=parse_mode)
                text = text[MAX_MESSAGE_LENGTH:]

            if len(text) > 0:
                bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode)

        logging.info('/list: exited')

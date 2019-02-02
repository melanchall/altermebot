import logging

from telegram.ext import CommandHandler
from telegram import ParseMode

from BotUtils import escape_markdown


class RemoveCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, aliases_storage):
        super().__init__('remove', self.__handle, pass_args=True)
        self._aliases_storage = aliases_storage

    def __handle(self, bot, update, args):
        logging.info('/remove: entered')

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
            logging.info('/remove: exited due to no arguments provided')
            return

        alias = ' '.join(args)
        self._aliases_storage.remove_alias(user_id, chat_id, alias)

        bot.send_message(chat_id=chat_id,
                         text="%s, alias *%s* was successfully removed"
                              % (escape_markdown(mention) if parse_mode is None else mention, escape_markdown(alias)),
                         parse_mode=ParseMode.MARKDOWN)

        logging.info('/remove: exited')

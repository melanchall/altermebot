import logging

from telegram.ext import MessageHandler, Filters
from telegram import ParseMode


class AliasMessageHandler(MessageHandler):
    """description of class"""

    def __init__(self, aliases_storage):
        super().__init__(Filters.text, self.__handle)
        self._aliases_storage = aliases_storage

    def __handle(self, bot, update):
        logging.info('message: entered')

        message = update.message
        chat_id = message.chat_id

        user_ids = self._aliases_storage.contains_alias(message.text, chat_id)
        if not any(user_ids):
            logging.info("message: exited due to message doesn't contain aliases")
            return

        from_user_id = message.from_user.id
        foreign_user_ids = set(filter(lambda u: u != from_user_id, user_ids))

        if not any(foreign_user_ids):
            logging.info("message: exited due to aliases are owned by message sender")
            return

        mentions = []
        parse_mode = None
        for user_id in foreign_user_ids:
            user = message.chat.get_member(user_id).user
            mention = user.username
            if not mention:
                mention = '[Unknown human](tg://user?id=%d)' % user_id
                parse_mode = ParseMode.MARKDOWN
            else:
                mention = "@%s" % mention
            mentions.append(mention)

        text = ' '.join(map(lambda u: "%s" % u, mentions))
        bot.send_message(chat_id=chat_id,
                         text=text,
                         reply_to_message_id=message.message_id,
                         parse_mode=parse_mode)

        logging.info('message: exited')

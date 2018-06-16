import logging

from telegram.ext import MessageHandler, Filters


class AliasMessageHandler(MessageHandler):
    """description of class"""

    def __init__(self, aliases_storage):
        super().__init__(Filters.text, self.__handle)
        self._aliases_storage = aliases_storage

    def __handle(self, bot, update):
        logging.info('message: entered')

        message = update.message
        chat_id = message.chat_id

        usernames = self._aliases_storage.contains_alias(message.text, chat_id)
        if not any(usernames):
            logging.info("message: exited due to message doesn't contain aliases")
            return

        from_username = message.from_user.username.lower()
        foreign_usernames = set(filter(lambda u: u.lower() != from_username, usernames))

        if not any(foreign_usernames):
            logging.info("message: exited due to aliases are owned by message sender")
            return

        text = ' '.join(map(lambda u: "@%s" % u, foreign_usernames))
        bot.send_message(chat_id=chat_id,
                         text=text,
                         reply_to_message_id=message.message_id)

        logging.info('message: exited')

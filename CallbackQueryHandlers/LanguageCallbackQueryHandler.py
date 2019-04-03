import logging

from telegram.ext import CallbackQueryHandler
from telegram import ParseMode

from BotUtils import escape_markdown
from Localization.Strings import Strings


class LanguageCallbackQueryHandler(CallbackQueryHandler):
    def __init__(self, db_manager, localizer):
        super().__init__(self.__handle, pattern='^(en|ru)$')
        self._db_manager = db_manager
        self._localizer = localizer

    def __handle(self, bot, update):
        logging.info('lang handler entered')

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

        logging.info(mention)

        callback_query = update.callback_query
        language = callback_query.data
        logging.info(language)

        self._db_manager.switch_language(user_id, chat_id, language)
        bot.send_message(chat_id=chat_id,
                         text=localizer(Strings.LANGUAGE_SWITCHED)
                         % (escape_markdown(mention) if parse_mode is None else mention),
                         parse_mode=ParseMode.MARKDOWN)

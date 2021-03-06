from telegram.ext import CommandHandler
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from BotUtils import escape_markdown
from Localization.Languages import Languages
from Localization.Strings import Strings


class LangCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, db_manager, localizer):
        super().__init__('lang', self.__handle, pass_args=True)
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

        #

        button_list = [
            InlineKeyboardButton("English", callback_data='en'),
            InlineKeyboardButton("Русский", callback_data='ru')
        ]
        reply_markup = InlineKeyboardMarkup([button_list])

        bot.send_message(chat_id=chat_id,
                         text='%s, select language:' % mention,
                         parse_mode=parse_mode,
                         reply_markup=reply_markup)

        return

        # Check that language is specified

        if not any(args):
            bot.send_message(chat_id=chat_id,
                             text=localizer(Strings.LANGUAGE_IS_NOT_SPECIFIED) % mention,
                             parse_mode=parse_mode)
            self._db_manager.log_command(user_id, chat_id, 'lang', 'Rejected due to no arguments provided')
            return

        # Check if language is available

        language = args[0]

        if language not in Languages.LANGUAGES:
            bot.send_message(chat_id=chat_id,
                             text=localizer(Strings.LANGUAGE_IS_INVALID) % (mention, ', '.join(Languages.LANGUAGES)),
                             parse_mode=parse_mode)
            self._db_manager.log_command(user_id, chat_id, 'lang', 'Rejected due to unknown language')
            return

        # Change language

        self._db_manager.switch_language(user_id, chat_id, language)
        bot.send_message(chat_id=chat_id,
                         text=localizer(Strings.LANGUAGE_SWITCHED)
                         % (escape_markdown(mention) if parse_mode is None else mention),
                         parse_mode=ParseMode.MARKDOWN)

        self._db_manager.log_command(user_id, chat_id, 'lang', 'OK')

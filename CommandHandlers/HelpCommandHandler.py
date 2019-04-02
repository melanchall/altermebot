from telegram.ext import CommandHandler
from telegram import ParseMode

from Localization.Strings import Strings


class HelpCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, localizer):
        super().__init__('help', self.__handle)
        self._localizer = localizer

    def __handle(self, bot, update):
        localizer = self._localizer.get_localizer(update)
        bot.send_message(chat_id=update.message.chat_id,
                         text=localizer(Strings.HELP),
                         parse_mode=ParseMode.MARKDOWN)

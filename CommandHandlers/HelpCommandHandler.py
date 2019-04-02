from telegram import ParseMode

from CommandHandlers.BaseCommandHandler import BaseCommandHandler
from Localization.Strings import Strings


class HelpCommandHandler(BaseCommandHandler):
    """description of class"""

    def __init__(self, db_manager):
        super().__init__('help', db_manager)

    def __handle(self, bot, update, args):
        localizer = self._localizer.get_localizer(update)

        bot.send_message(chat_id=update.message.chat_id,
                         text=localizer(Strings.HELP),
                         parse_mode=ParseMode.MARKDOWN)

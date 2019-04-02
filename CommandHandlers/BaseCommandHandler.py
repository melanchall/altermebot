from telegram.ext import CommandHandler

from Localization.Localizer import Localizer


class BaseCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, command, db_manager):
        super().__init__(command, self.__handle, pass_args=True)
        self._db_manager = db_manager
        self._localizer = Localizer(self._db_manager)

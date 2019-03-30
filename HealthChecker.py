import os


class HealthChecker:
    """description of class"""

    def __init__(self, bot, db_manager):
        self._bot = bot
        self._db_manager = db_manager
        self._health_check_chat_id = int(os.environ.get('HEALTH_CHECK_CHAT_ID'))

    def perform_health_check(self):
        self.__check_messaging()

    def __check_messaging(self):
        message = self._bot.send_message(chat_id=self._health_check_chat_id, text='Messaging check ping')
        if message:
            self._db_manager.update_health_info_messaging_ok()

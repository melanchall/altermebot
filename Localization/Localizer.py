from Localization.Strings import Strings


class Localizer:
    def __init__(self, db_manager):
        self._db_manager = db_manager

    def get_localizer(self, update):
        message = update.message
        chat_id = message.chat_id
        user_id = message.from_user.id
        language = self._db_manager.get_language(user_id, chat_id)

        def localize(string_id):
            return Strings.CONTENT[language][string_id]
        return localize

from Localization.Strings import Strings


class Localizer:
    def __init__(self, db_manager):
        self._db_manager = db_manager

    def get_localizer(self, update):
        message = update.effective_message
        chat = update.effective_chat
        chat_id = chat.id
        user = update.effective_user
        user_id = user.id

        def localize(string_id):
            language = self._db_manager.get_language(user_id, chat_id)
            return Strings.CONTENT[language][string_id]
        return localize

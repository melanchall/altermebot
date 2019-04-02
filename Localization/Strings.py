from Localization.Languages import Languages


class Strings:
    # help

    HELP = 100

    # lang

    LANGUAGE_IS_NOT_SPECIFIED = 200
    LANGUAGE_IS_INVALID = 201
    LANGUAGE_SWITCHED = 202

    # alias

    MAX_ALIASES_COUNT_REACHED = 300
    ALIAS_IS_NOT_SPECIFIED = 301
    ALIAS_CONTAINS_MENTION = 302
    ALIAS_CONTAINS_BOT_COMMAND = 303
    ALIAS_TOO_SHORT = 304
    ALIAS_TOO_LONG = 305

    #

    CONTENT = {
        Languages.EN: {
            HELP: '\n'.join([
                '/alias _<alias>_ - Add the specified alias so you can be called with it in the current chat',
                '/list - List all your aliases for the current chat',
                '/remove _<alias>_ - Remove the specified alias so you cannot be called with it in the current chat',
                '/clear - Remove all your aliases in the current chat',
                '/off - Disable mentioning you by your aliases in the current chat',
                '/on - Enable mentioning you by your aliases in the current chat',
                '/lang _<language>_ - Switch bot''s messages language',
                '/help - Show this help message']),

            LANGUAGE_IS_NOT_SPECIFIED: "%s, you should specify language passing it as a parameter to the /lang command",
            LANGUAGE_IS_INVALID: "%s, please specify one of the available languages: %s",
            LANGUAGE_SWITCHED: "%s, my messages will be in English for you in this chat"
        },
        Languages.RU: {
            HELP: '\n'.join([
                '/alias _<псевдоним>_ - Добавить указанный псевдоним, по которому вы будете упомянуты в этом чате',
                '/list - Перечислить все ваши псевдонимы для этого чата',
                '/remove _<псевдоним>_ - Удалить указанный псевдоним; вы больше не будете упомянуты по нему в этом чате',
                '/clear - Удалить все ваши псевдонимы для этого чата',
                '/off - Выключить упоминание вас по псевдонимам в этом чате',
                '/on - Включить упоминание вас по псевдонимам в этом чате',
                '/lang _<язык>_ - Переключить язык сообщений бота',
                '/help - Показать это справочное сообщение']),

            LANGUAGE_IS_NOT_SPECIFIED: "%s, вы должны указать язык, передав его команде /lang",
            LANGUAGE_IS_INVALID: "%s, пожалуйста, укажите один из доступных языков: %s",
            LANGUAGE_SWITCHED: "%s, мои сообщения будут для вас на русском языке в этом чате"
        }
    }

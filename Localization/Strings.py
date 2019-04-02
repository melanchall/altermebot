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
    ALIAS_ADDED = 306
    ALIAS_ALREADY_IN_USE = 307

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

            LANGUAGE_IS_NOT_SPECIFIED: "%s, you should specify language passing it as a parameter to the "
                                       "`/lang` command. Example: `/lang en`",
            LANGUAGE_IS_INVALID: "%s, please specify one of the available languages: %s",
            LANGUAGE_SWITCHED: "%s, my messages will be in English for you in this chat",

            MAX_ALIASES_COUNT_REACHED: "%s, you've reached max aliases count for this chat (%d). Please remove some "
                                       "aliases and try again",
            ALIAS_IS_NOT_SPECIFIED: "%s, you should specify alias passing it as a parameter to the `/alias` command. "
                                    "Example: `/alias Max`",
            ALIAS_CONTAINS_MENTION: "%s, alias cannot contain mentions",
            ALIAS_CONTAINS_BOT_COMMAND: "%s, alias cannot contain bot commands",
            ALIAS_TOO_SHORT: "%s, alias is too short. Min length is %d",
            ALIAS_TOO_LONG: "%s, alias is too long. Max length is %d",
            ALIAS_ADDED: "%s, alias *%s* was successfully added",
            ALIAS_ALREADY_IN_USE: "%s, alias *%s* is already in use by another user"
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

            LANGUAGE_IS_NOT_SPECIFIED: "%s, вы должны указать язык, передав его аргументом команде `/lang`. Пример: "
                                       "`/lang ru`",
            LANGUAGE_IS_INVALID: "%s, пожалуйста, укажите один из доступных языков: %s",
            LANGUAGE_SWITCHED: "%s, мои сообщения будут для вас на русском языке в этом чате",

            MAX_ALIASES_COUNT_REACHED: "%s, вы достигли максимального количества псевдонимов для этого чата (%d). "
                                       "Пожалуйста, удалите ненужные псевдонимы и попробуйте снова",
            ALIAS_IS_NOT_SPECIFIED: "%s, вы должны указать псевдоним, передав его аргументом команде `/alias`. Пример: "
                                    "`/alias Макс`",
            ALIAS_CONTAINS_MENTION: "%s, псевдоним не может содержать упоминания пользователей",
            ALIAS_CONTAINS_BOT_COMMAND: "%s, псевдоним не может содержать команды ботам",
            ALIAS_TOO_SHORT: "%s, псевдоним слишком короткий. Минимальная длина %d",
            ALIAS_TOO_LONG: "%s, псевдоним слишком длинный. Максимальная длина %d",
            ALIAS_ADDED: "%s, псевдоним *%s* успешно добавлен",
            ALIAS_ALREADY_IN_USE: "%s, псевдоним *%s* занят другим пользователем"
        }
    }

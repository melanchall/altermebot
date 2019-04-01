from Localization.Languages import Languages


class Strings:
    LANGUAGE_IS_NOT_SPECIFIED = 0
    LANGUAGE_IS_INVALID = 1
    LANGUAGE_SWITCHED = 2

    CONTENT = {
        Languages.EN: {
            LANGUAGE_IS_NOT_SPECIFIED: "%s, you should specify language passing it as a parameter to the /lang command",
            LANGUAGE_IS_INVALID: "%s, please specify one of the available languages: %s",
            LANGUAGE_SWITCHED: "%s, my messages will be in English for you in this chat"
        },
        Languages.RU: {
            LANGUAGE_IS_NOT_SPECIFIED: "%s, вы должны указать язык, передав его команде /lang",
            LANGUAGE_IS_INVALID: "%s, пожалуйста, укажите один из доступных языков: %s",
            LANGUAGE_SWITCHED: "%s, мои сообщения будут для вас на русском языке в этом чате"
        }
    }

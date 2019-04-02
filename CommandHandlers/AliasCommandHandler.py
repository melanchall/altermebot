from telegram.ext import CommandHandler
from telegram import ParseMode, MessageEntity

from BotUtils import escape_markdown, ALIAS_MAX_LENGTH, ALIAS_MIN_LENGTH, ALIASES_MAX_COUNT
from Localization.Strings import Strings


class AliasCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, db_manager, localizer):
        super().__init__('alias', self.__handle, pass_args=True)
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

        # Check if max aliases count reached

        if self._db_manager.get_aliases_count(user_id, chat_id) >= ALIASES_MAX_COUNT:
            bot.send_message(chat_id=chat_id,
                             text=localizer(Strings.MAX_ALIASES_COUNT_REACHED) % (mention, ALIASES_MAX_COUNT),
                             parse_mode=parse_mode)
            self._db_manager.log_command(user_id, chat_id, 'alias', 'Rejected due to max aliases count reached')
            return

        # Check that alias is  specified

        if not any(args):
            bot.send_message(chat_id=chat_id,
                             text=localizer(Strings.ALIAS_IS_NOT_SPECIFIED) % mention,
                             parse_mode=parse_mode)
            self._db_manager.log_command(user_id, chat_id, 'alias', 'Rejected due to no arguments provided')
            return

        # Check that alias doesn't contain mentions and bot commands

        entities = message.entities

        if any(e.type == MessageEntity.MENTION for e in entities):
            bot.send_message(chat_id=chat_id,
                             text=localizer(Strings.ALIAS_CONTAINS_MENTION) % mention,
                             parse_mode=parse_mode)
            self._db_manager.log_command(user_id, chat_id, 'alias', 'Rejected due to alias contains mention(s)')
            return

        if any(e.type == MessageEntity.BOT_COMMAND and e.offset > 0 for e in entities):
            bot.send_message(chat_id=chat_id,
                             text=localizer(Strings.ALIAS_CONTAINS_BOT_COMMAND) % mention,
                             parse_mode=parse_mode)
            self._db_manager.log_command(user_id, chat_id, 'alias', 'Rejected due to alias contains bot command(s)')
            return

        alias = ' '.join(args)

        # Check that alias has valid length

        if len(alias) < ALIAS_MIN_LENGTH:
            bot.send_message(chat_id=chat_id,
                             text=localizer(Strings.ALIAS_TOO_SHORT) % (mention, ALIAS_MIN_LENGTH),
                             parse_mode=parse_mode)
            self._db_manager.log_command(user_id, chat_id, 'alias', 'Rejected due to alias is too short')
            return

        if len(alias) > ALIAS_MAX_LENGTH:
            bot.send_message(chat_id=chat_id,
                             text=localizer(Strings.ALIAS_TOO_LONG) % (mention, ALIAS_MAX_LENGTH),
                             parse_mode=parse_mode)
            self._db_manager.log_command(user_id, chat_id, 'alias', 'Rejected due to alias is too long')
            return

        # Check that alias is not in use

        if not self._db_manager.check_alias_is_not_in_use(user_id, chat_id, alias):
            bot.send_message(chat_id=chat_id,
                             text=localizer(Strings.ALIAS_ALREADY_IN_USE)
                             % (escape_markdown(mention) if parse_mode is None else mention, escape_markdown(alias)),
                             parse_mode=ParseMode.MARKDOWN)
            self._db_manager.log_command(user_id, chat_id, 'alias', 'Rejected due to alias is already in use by another user')
            return

        # Add alias

        self._db_manager.add_alias(user_id, chat_id, alias)

        bot.send_message(chat_id=chat_id,
                         text=localizer(Strings.ALIAS_ADDED)
                         % (escape_markdown(mention) if parse_mode is None else mention, escape_markdown(alias)),
                         parse_mode=ParseMode.MARKDOWN)

        self._db_manager.log_command(user_id, chat_id, 'alias', 'OK')

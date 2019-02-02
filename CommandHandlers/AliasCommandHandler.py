import logging

from telegram.ext import CommandHandler
from telegram import ParseMode, MessageEntity

from BotUtils import escape_markdown, ALIAS_MAX_LENGTH, ALIAS_MIN_LENGTH, ALIASES_MAX_COUNT


class AliasCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, aliases_storage):
        super().__init__('alias', self.__handle, pass_args=True)
        self._aliases_storage = aliases_storage

    def __handle(self, bot, update, args):
        logging.info('/alias: entered')

        message = update.message
        chat_id = message.chat_id
        user_id = message.from_user.id

        user = message.from_user
        mention = user.username
        parse_mode = None
        if not mention:
            mention = '[Unknown human](tg://user?id=%d)' % user_id
            parse_mode = ParseMode.MARKDOWN
        else:
            mention = "@%s" % mention

        # Check if max aliases count reached

        if self._aliases_storage.get_aliases_count(user_id, chat_id) >= ALIASES_MAX_COUNT:
            bot.send_message(chat_id=chat_id,
                             text="%s, you've reached max aliases count for this chat (%d). Please remove some "
                                  "aliases and try again" % (mention, ALIASES_MAX_COUNT),
                             parse_mode=parse_mode)
            logging.info('/alias: exited due to max aliases count reached')
            return

        # Check that alias is  specified

        if not any(args):
            bot.send_message(chat_id=chat_id,
                             text="%s, you should specify alias passing it as a parameter to the /alias command"
                                  % mention,
                             parse_mode=parse_mode)
            logging.info('/alias: exited due to no arguments provided')
            return

        # Check that alias doesn't contain mentions and bot commands

        entities = message.entities

        if any(e.type == MessageEntity.MENTION for e in entities):
            bot.send_message(chat_id=chat_id,
                             text="%s, alias cannot contain mentions" % mention,
                             parse_mode=parse_mode)
            logging.info('/alias: exited due to message contains mentions')
            return

        if any(e.type == MessageEntity.BOT_COMMAND and e.offset > 0 for e in entities):
            bot.send_message(chat_id=chat_id,
                             text="%s, alias cannot contain bot commands" % mention,
                             parse_mode=parse_mode)
            logging.info('/alias: exited due to message contains bot commands')
            return

        alias = ' '.join(args)

        # Check that alias has valid length

        if len(alias) < ALIAS_MIN_LENGTH:
            bot.send_message(chat_id=chat_id,
                             text="%s, alias is too short. Min length is %d"
                                  % (mention, ALIAS_MIN_LENGTH),
                             parse_mode=parse_mode)
            logging.info('/alias: exited due to alias is too short')
            return

        if len(alias) > ALIAS_MAX_LENGTH:
            bot.send_message(chat_id=chat_id,
                             text="%s, alias is too long. Max length is %d"
                                  % (mention, ALIAS_MAX_LENGTH),
                             parse_mode=parse_mode)
            logging.info('/alias: exited due to alias is too long')
            return

        # Check that alias is not in use

        if not self._aliases_storage.check_alias_is_not_in_use(user_id, chat_id, alias):
            bot.send_message(chat_id=chat_id,
                             text="%s, alias *%s* is already in use by another user"
                                  % (escape_markdown(mention) if parse_mode is None else mention,
                                     escape_markdown(alias)),
                             parse_mode=ParseMode.MARKDOWN)
            logging.info('/alias: exited due to alias is already in use by another user')
            return

        # Add alias

        self._aliases_storage.add_alias(user_id, chat_id, alias)

        bot.send_message(chat_id=chat_id,
                         text="%s, alias *%s* was successfully added"
                              % (escape_markdown(mention) if parse_mode is None else mention, escape_markdown(alias)),
                         parse_mode=ParseMode.MARKDOWN)

        logging.info('/alias: exited')

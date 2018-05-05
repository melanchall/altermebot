import logging
import os

from telegram.ext import CommandHandler


class AdminCommandHandler(CommandHandler):
    """description of class"""

    def __init__(self, aliases_storage):
        super().__init__('admin', self.__handle, pass_args=True)
        self._aliases_storage = aliases_storage

    def __handle(self, bot, update, args):
        logging.info('/admin: entered')

        message = update.message
        chat_id = message.chat_id
        from_user_id = message.from_user.id

        if from_user_id != int(os.environ.get('ADMIN_USER_ID')):
            logging.info('/admin: exited due to no arguments provided')
            return

        if not any(args):
            logging.info('/admin: exited due to no arguments provided')
            return

        command = args[0]
        username = args[1][1:]

        logging.info('/admin (%s): entered' % command)

        if command == 'alias':
            alias = ' '.join(args[2:])
            self._aliases_storage.add_alias(username, chat_id, alias)
        elif command == 'clear':
            self._aliases_storage.remove_all_aliases(username, chat_id)
        elif command == 'list':
            self._aliases_storage.get_aliases(username, chat_id)
        elif command == 'remove':
            alias = ' '.join(args[2:])
            self._aliases_storage.remove_alias(username, chat_id, alias)

        logging.info('/admin (%s): exited' % command)
        logging.info('/admin: exited')

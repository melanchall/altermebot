import os
import logging

from telegram.ext import Updater, MessageQueue

from CommandHandlers.AliasCommandHandler import AliasCommandHandler
from CommandHandlers.ListCommandHandler import ListCommandHandler
from CommandHandlers.HelpCommandHandler import HelpCommandHandler
from CommandHandlers.RemoveCommandHandler import RemoveCommandHandler
from CommandHandlers.ClearCommandHandler import ClearCommandHandler
from CommandHandlers.OnCommandHandler import OnCommandHandler
from CommandHandlers.OffCommandHandler import OffCommandHandler

from MessageHandlers.AliasMessageHandler import AliasMessageHandler

from DbManager import DbManager

from MessageQueueBot import MessageQueueBot


class Bot(object):
    """description of class"""

    def __init__(self):
        token = os.environ.get('ALTER_ME_TOKEN')
        message_queue = MessageQueue(all_burst_limit=29, all_time_limit_ms=1017)
        bot = MessageQueueBot(token, message_queue=message_queue)

        self._updater = Updater(bot=bot)
        self._dispatcher = self._updater.dispatcher

        self._db_manager = DbManager()

        self.__setup_command_handlers()
        self.__setup_message_handlers()

    def start(self):
        logging.info('Starting the bot...')
        self._updater.start_polling()
        logging.info('Bot is started')
        self._updater.idle()

    def stop(self):
        logging.info('Stopping the bot...')
        self._updater.stop()
        logging.info('Bot is stopped')

    def __setup_command_handlers(self):
        handlers = [
            AliasCommandHandler(self._db_manager),
            ListCommandHandler(self._db_manager),
            HelpCommandHandler(),
            RemoveCommandHandler(self._db_manager),
            ClearCommandHandler(self._db_manager),
            OnCommandHandler(self._db_manager),
            OffCommandHandler(self._db_manager)
        ]

        for handler in handlers:
            self._dispatcher.add_handler(handler)

    def __setup_message_handlers(self):
        handlers = [
            AliasMessageHandler(self._db_manager)
        ]

        for handler in handlers:
            self._dispatcher.add_handler(handler)

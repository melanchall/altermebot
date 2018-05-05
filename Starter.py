import atexit
import logging
from logging.handlers import RotatingFileHandler

from Bot import Bot

# setup logging

log_file_handler = RotatingFileHandler('alter-me.log',
                                       mode='a',
                                       maxBytes=5*1024*1024,
                                       backupCount=2,
                                       encoding=None,
                                       delay=0)

logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    handlers=[log_file_handler])

# setup bot

bot = Bot()


def exit_handler():
    bot.stop()


atexit.register(exit_handler)

bot.start()

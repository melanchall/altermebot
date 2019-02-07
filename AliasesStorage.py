import sqlite3
import logging


class AliasesStorage(object):
    """description of class"""

    def __init__(self):
        self._connection = sqlite3.connect("aliases.db", check_same_thread=False)
        self._connection.set_trace_callback(logging.info)
        self._connection.create_function('eqnocase', 2, self.__eqnocase)

        self._cursor = self._connection.cursor()

    def get_aliases(self, username, chat_id):
        rows = self._cursor.execute('''SELECT aliases.alias
                                       FROM users, aliases
                                       WHERE EQNOCASE(username, ?) AND
                                             user_id = users.id AND
                                             chat_id = ?''', (username, chat_id)).fetchall()
        return list(map(lambda row: row[0], rows))

    @staticmethod
    def __eqnocase(x, y):
        return 1 if x.lower() == y.lower() else 0

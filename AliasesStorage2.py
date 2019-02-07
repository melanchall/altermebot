import sqlite3
import re
import logging


class AliasesStorage2(object):
    """description of class"""

    def __init__(self):
        self._connection = sqlite3.connect("aliases2.db", check_same_thread=False)
        self._connection.set_trace_callback(logging.info)
        self._connection.create_function('regexp', 2, self.__regexp)
        self._connection.create_function('eqnocase', 2, self.__eqnocase)

        self._cursor = self._connection.cursor()

        self.__create_tables()

    def get_aliases_count(self, user_id, chat_id):
        (count,) = self._cursor.execute('''SELECT COUNT(*)
                                           FROM aliases
                                           WHERE user_id = ? AND
                                                 chat_id = ?''', (user_id, chat_id)).fetchone()
        return count

    def check_alias_is_not_in_use(self, user_id, chat_id, alias):
        user_id_row = self._cursor.execute('''SELECT user_id
                                              FROM aliases
                                              WHERE chat_id = ? AND
                                                    EQNOCASE(alias, ?)''', (chat_id, alias)).fetchone()
        if user_id_row is None:
            return True

        return user_id_row[0] == user_id

    def add_alias(self, user_id, chat_id, alias):
        self._cursor.execute('''INSERT OR IGNORE INTO aliases(user_id, chat_id, alias)
                                VALUES (?, ?, ?)''', (user_id, chat_id, alias))
        self._connection.commit()

    def remove_alias(self, user_id, chat_id, alias):
        self._cursor.execute('''DELETE
                                FROM aliases
                                WHERE user_id = ? AND
                                      EQNOCASE(alias, ?) AND
                                      chat_id = ?''', (user_id, alias, chat_id))
        self._connection.commit()

    def remove_all_aliases(self, user_id, chat_id):
        self._cursor.execute('''DELETE
                                FROM aliases
                                WHERE user_id = ? AND
                                      chat_id = ?''', (user_id, chat_id))
        self._connection.commit()

    def get_aliases(self, user_id, chat_id):
        rows = self._cursor.execute('''SELECT alias
                                       FROM aliases
                                       WHERE user_id = ? AND
                                             chat_id = ?''', (user_id, chat_id)).fetchall()
        return list(map(lambda row: row[0], rows))

    def contains_alias(self, text, chat_id):
        rows = self._cursor.execute('''SELECT user_id
                                       FROM aliases
                                       WHERE chat_id = ? AND
                                             alias REGEXP ? ''', (chat_id, text)).fetchall()
        return list(map(lambda row: row[0], rows))

    @staticmethod
    def __regexp(text, alias):
        return 1 if alias and re.search(r'(?i)\b%s\b' % re.escape(alias), text) else 0

    @staticmethod
    def __eqnocase(x, y):
        return 1 if x.lower() == y.lower() else 0

    def __create_tables(self):
        self.__create_aliases_table()

    def __create_aliases_table(self):
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS aliases (
                                id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                user_id INTEGER NOT NULL,
                                chat_id INTEGER NOT NULL,
                                alias   TEXT NOT NULL,
                                UNIQUE (user_id, chat_id, alias))''')

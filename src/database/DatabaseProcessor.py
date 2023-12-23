import sqlite3
from src.exceptions.ErrorHandler import ErrorHandler

DB_FILE = ":memory:"


class DatabaseProcessor:
    def __init__(self, data, db_file=DB_FILE):
        try:
            self.conn = DatabaseProcessorUtilities.create_connection(db_file)
            self._create_tables(data)
            self.cursor = self.conn.cursor()
        except sqlite3.Error:
            ErrorHandler.handle_error("SQL Database Error")

    def _create_tables(self, data):
        data.users.to_sql("users", self.conn, if_exists="replace")
        data.children.to_sql("children", self.conn, if_exists="replace")

    def close_connection(self):
        self.conn.close()


class DatabaseProcessorUtilities:
    @staticmethod
    def create_connection(db_file):
        return sqlite3.connect(db_file)

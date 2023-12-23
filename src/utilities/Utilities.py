from src.user.UserRole import UserRole
from src.database.DatabaseProcessor import DatabaseProcessor


class Utilities:
    @staticmethod
    def get_login_type(login):
        return "email" if "@" in login else "telephone_number"

    @staticmethod
    def get_role_type(role):
        return UserRole.ADMIN if role == "admin" else UserRole.USER

    @staticmethod
    def get_piece_of_data_from_users(piece, login, data):
        login_type = Utilities.get_login_type(login)
        if isinstance(data, DatabaseProcessor):
            sql_query = "SELECT " + piece + " FROM users WHERE " + login_type + " == '" + login + "'"
            return data.cursor.execute(sql_query).fetchone()[0]
        return data.users.loc[data.users[login_type] == login, piece].iloc[0]

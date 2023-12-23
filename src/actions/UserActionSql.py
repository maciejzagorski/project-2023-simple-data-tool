from src.utilities.Utilities import Utilities
from src.utilities.Printer import Printer


class UserActionSql:
    @staticmethod
    def print_children(login, data):
        user_children = UserActionSql._get_children_by_user_login(login, data)
        if not len(user_children) == 0:
            Printer.user_all_children_sql(user_children)

    @staticmethod
    def find_similar_children_by_age(login, data):
        users_with_similar_children = UserActionSql._get_users_with_similar_children(login, data)
        if not len(users_with_similar_children) == 0:
            for user in users_with_similar_children:
                UserActionSql._get_user_and_children(user, data)

    @staticmethod
    def _get_children_by_user_login(login, data):
        user_index = Utilities.get_piece_of_data_from_users("id", login, data)
        sql_query = "SELECT id, name, age FROM children WHERE id == " + str(user_index) + " ORDER BY name ASC"
        return data.cursor.execute(sql_query).fetchall()

    @staticmethod
    def _get_similar_children(login, data):
        user_children = UserActionSql._get_children_by_user_login(login, data)
        if not len(user_children) == 0:
            user_children_age_list = UserActionSql._column_to_list(user_children)
            sql_query = "SELECT name, age, id FROM children WHERE age IN (" + user_children_age_list + ") AND NOT id == " \
                        + str(user_children[0][0])
            return data.cursor.execute(sql_query).fetchall()
        return []

    @staticmethod
    def _get_users_with_similar_children(login, data):
        similar_children = UserActionSql._get_similar_children(login, data)
        if not len(similar_children) == 0:
            similar_children_id_list = UserActionSql._column_to_list(similar_children)
            sql_query = "SELECT firstname, telephone_number FROM users WHERE id IN (" + \
                        similar_children_id_list + ")"
            return data.cursor.execute(sql_query).fetchall()
        return []

    @staticmethod
    def _get_user_and_children(user, data):
        Printer.user_for_children(user[0], user[1])
        user_children = UserActionSql._get_children_by_user_login(user[1], data)
        Printer.user_all_children_sql(user_children, True)

    @staticmethod
    def _column_to_list(data):
        list_from_column = [row[-1] for row in data]
        return ', '.join(str(data) for data in list_from_column)

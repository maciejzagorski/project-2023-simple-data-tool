from src.utilities.Utilities import Utilities
from src.utilities.Printer import Printer


class UserAction:
    @staticmethod
    def print_children(login, data):
        user_children = UserAction._get_children_by_user_login(login, data)
        if not user_children.empty:
            Printer.user_all_children(user_children)

    @staticmethod
    def find_similar_children_by_age(login, data):
        users_with_similar_children = UserAction._get_users_with_similar_children(login, data)
        for index, user in users_with_similar_children.iterrows():
            UserAction._get_user_and_children(user, data)

    @staticmethod
    def _get_children_by_user_login(login, data):
        user_index = Utilities.get_piece_of_data_from_users("id", login, data)
        return data.children.loc[data.children.index == user_index].sort_values(['name'])

    @staticmethod
    def _get_similar_children(login, data):
        user_children = UserAction._get_children_by_user_login(login, data)
        return data.children[data.children['age'].isin(user_children['age'])].drop(user_children.index)

    @staticmethod
    def _get_users_with_similar_children(login, data):
        similar_children = UserAction._get_similar_children(login, data)
        return data.users[data.users.index.isin(similar_children.index)]

    @staticmethod
    def _get_user_and_children(user, data):
        Printer.user_for_children(user['firstname'], user['telephone_number'])
        user_children = UserAction._get_children_by_user_login(user['email'], data)
        Printer.user_all_children(user_children, True)

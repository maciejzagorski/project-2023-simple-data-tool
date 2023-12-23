from src.utilities.Utilities import Utilities
from src.utilities.ArgsParser import ACTIONS_ADMIN
from src.exceptions.AuthorizationError import AuthorizationError


class Authorizator:

    @staticmethod
    def authorize(login, action, data):
        role = Utilities.get_role_type(Utilities.get_piece_of_data_from_users("role", login, data))
        if action in ACTIONS_ADMIN and not role.value:
            raise AuthorizationError()

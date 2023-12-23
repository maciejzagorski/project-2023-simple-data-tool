from src.utilities.Utilities import Utilities
from src.exceptions.AuthenticationError import AuthenticationError


class Authenticator:
    @staticmethod
    def authenticate(login, password, data):
        if login is None or password is None:
            raise AuthenticationError()
        try:
            password_to_compare = Utilities.get_piece_of_data_from_users("password", login, data)
        except IndexError:
            raise AuthenticationError()
        if password != password_to_compare:
            raise AuthenticationError()

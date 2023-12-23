from src.user.UserCredentials import UserCredentials
from src.database.DatabaseProcessor import DatabaseProcessor
from src.user.Authenticator import Authenticator
from src.user.Authorizator import Authorizator
from src.actions.ActionProcessor import ActionProcessor
from src.exceptions.AuthenticationError import AuthenticationError
from src.exceptions.AuthorizationError import AuthorizationError
from src.exceptions.ErrorHandler import ErrorHandler


class UserProcessor(UserCredentials):
    def __init__(self, data):
        super().__init__()
        self.data = data if not self.create_database else DatabaseProcessor(data)
        self._process_user()
        if self.create_database:
            self.data.close_connection()

    def _process_user(self):
        try:
            Authenticator.authenticate(self.login, self.password, self.data)
            Authorizator.authorize(self.login, self.action, self.data)
            ActionProcessor(self.login, self.action, self.create_database, self.data)
        except AuthenticationError as auth_err:
            ErrorHandler.handle_error(auth_err)
        except AuthorizationError as authz_err:
            ErrorHandler.handle_error(authz_err)

from src.utilities.ArgsParser import ArgParser
from src.exceptions.ArgsParsingError import ArgsParsingError
from src.exceptions.ErrorHandler import ErrorHandler


class UserCredentials:
    def __init__(self):
        try:
            self.parsed_arguments = ArgParser().arguments
        except ArgsParsingError as args_err:
            ErrorHandler.handle_error(args_err)
        self.login = self.parsed_arguments.login
        self.password = self.parsed_arguments.password
        self.action = self.parsed_arguments.action
        self.create_database = self.parsed_arguments.create_database

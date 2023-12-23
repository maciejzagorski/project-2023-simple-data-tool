import argparse
from src.exceptions.ArgsParsingError import ArgsParsingError

ACTIONS_ADMIN = ['print-all-accounts', 'print-oldest-account', 'group-by-age']
ACTIONS_USER = ['create-database', 'print-children', 'find-similar-children-by-age']


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self._initialize_parser()
        self.arguments = self.parser.parse_args()
        self._parse_create_database_argument()
        self._validate_arguments()

    def _initialize_parser(self):
        self.parser.add_argument('--login', type=str, default=None)
        self.parser.add_argument('--password', type=str, default=None)
        self.parser.add_argument('action', choices=ACTIONS_ADMIN + ACTIONS_USER, nargs='?')
        self.parser.add_argument('additional_action', choices=ACTIONS_ADMIN + ACTIONS_USER, nargs='?')

    def _validate_arguments(self):
        if (self.arguments.action is None and self.arguments.additional_action is None) \
                or (self.arguments.action == 'create-database' and self.arguments.additional_action is None):
            actions_list = ', '.join(f"'{action}'" for action in ACTIONS_ADMIN + ACTIONS_USER[1:])
            raise ArgsParsingError(f"No action to perform; choose from: {actions_list}")

    def _parse_create_database_argument(self):
        if self.arguments.action == 'create-database':
            setattr(self.arguments, "create_database", True)
            setattr(self.arguments, "action", self.arguments.additional_action)
        elif self.arguments.additional_action == 'create-database':
            setattr(self.arguments, "create_database", True)
        else:
            setattr(self.arguments, "create_database", False)

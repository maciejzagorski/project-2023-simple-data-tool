from src.actions.AdminAction import AdminAction
from src.actions.AdminActionSql import AdminActionSql
from src.actions.UserAction import UserAction
from src.actions.UserActionSql import UserActionSql


class ActionProcessor:
    def __init__(self, login, action, create_database, data):
        self.actions = {
            "print-all-accounts": (lambda _: AdminAction.print_all_accounts(data),
                                   lambda _: AdminActionSql.print_all_accounts(data)),
            "print-oldest-account": (lambda _: AdminAction.print_oldest_account(data),
                                     lambda _: AdminActionSql.print_oldest_account(data)),
            "group-by-age": (lambda _: AdminAction.group_by_age(data),
                             lambda _: AdminActionSql.group_by_age(data)),
            "print-children": (lambda _: UserAction.print_children(login, data),
                               lambda _: UserActionSql.print_children(login, data)),
            "find-similar-children-by-age": (lambda _: UserAction.find_similar_children_by_age(login, data),
                                             lambda _: UserActionSql.find_similar_children_by_age(login, data))
        }
        self._process_action(action, create_database)

    def _process_action(self, action, create_database):
        processor_function = self.actions.get(action)[create_database]
        return processor_function(action)

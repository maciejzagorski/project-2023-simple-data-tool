from src.utilities.Printer import Printer


class AdminAction:
    @staticmethod
    def print_all_accounts(data):
        user_data = data.users
        print(len(user_data.index))

    @staticmethod
    def print_oldest_account(data):
        user_data = data.users
        oldest_account = user_data.sort_values(by='created_at', ascending=True).iloc[0]
        Printer.user(oldest_account['firstname'], oldest_account['email'], oldest_account['created_at'])

    @staticmethod
    def group_by_age(data):
        children_data = data.children
        age_counts = children_data.groupby(['age'])['age'].count().reset_index(name='count').sort_values(
            ['count', 'age'], ascending=[True, False])
        for _, row in age_counts.iterrows():
            Printer.children_group(row['age'], row['count'])

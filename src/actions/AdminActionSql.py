from src.utilities.Printer import Printer


class AdminActionSql:
    @staticmethod
    def print_all_accounts(data):
        cursor = data.cursor
        sql_query = "SELECT count(*) FROM users"
        print(cursor.execute(sql_query).fetchone()[0])

    @staticmethod
    def print_oldest_account(data):
        cursor = data.cursor
        sql_query = "SELECT firstname, email, created_at FROM users ORDER BY created_at ASC"
        results = cursor.execute(sql_query).fetchone()
        Printer.user(*results)

    @staticmethod
    def group_by_age(data):
        cursor = data.cursor
        sql_query = "SELECT age, COUNT(*) FROM children GROUP BY age ORDER BY COUNT(*) ASC, age DESC"
        results = cursor.execute(sql_query).fetchall()
        for row in results:
            Printer.children_group(*row)

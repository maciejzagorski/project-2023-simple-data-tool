class Printer:
    @staticmethod
    def user(firstname, email, created_at):
        print(f"name: {firstname}\n"
              f"email_address: {email}\n"
              f"created_at: {created_at}")

    @staticmethod
    def children_group(age, count):
        print(f"age: {int(age)}, count: {count}")

    @staticmethod
    def user_all_children(children, without_end_of_line=False):
        children.reset_index(inplace=True)
        last_index = children.index[-1]
        for index, row in children.iterrows():
            Printer._children(row['name'], row['age'])
            Printer._format_line(without_end_of_line, index, last_index)

    @staticmethod
    def user_all_children_sql(children, without_end_of_line=False):
        last_index = len(children) - 1
        for i, child in enumerate(children):
            Printer._children(child[1], child[2])
            Printer._format_line(without_end_of_line, i, last_index)

    @staticmethod
    def _children(name, age):
        print(f"{name}, {int(age)}", end="")

    @staticmethod
    def _format_line(without_end_of_line, index, last_index):
        if without_end_of_line and index != last_index:
            print("; ", end="")
        else:
            print()

    @staticmethod
    def user_for_children(firstname, telephone_number):
        print(f"{firstname}, {telephone_number}: ", end="")

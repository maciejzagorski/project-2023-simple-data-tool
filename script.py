from src.data.DataValidator import DataValidator
from src.user.UserProcessor import UserProcessor


def main():
    UserProcessor(DataValidator())


if __name__ == '__main__':
    main()

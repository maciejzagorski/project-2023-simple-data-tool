import sys


class ErrorHandler:
    @staticmethod
    def handle_error(e):
        print(e)
        sys.exit(-1)

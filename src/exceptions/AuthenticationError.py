class AuthenticationError(Exception):
    def __init__(self, message="Invalid Login"):
        self.message = message
        super().__init__(self.message)

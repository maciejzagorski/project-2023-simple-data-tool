class AuthorizationError(Exception):
    def __init__(self, message="Unauthorized User"):
        self.message = message
        super().__init__(self.message)

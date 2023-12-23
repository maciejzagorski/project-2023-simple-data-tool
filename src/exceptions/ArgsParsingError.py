class ArgsParsingError(Exception):
    def __init__(self, message="Invalid Arguments"):
        self.message = message
        super().__init__(self.message)

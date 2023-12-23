class DataProcessingError(Exception):
    def __init__(self, message="Invalid Data"):
        self.message = message
        super().__init__(self.message)

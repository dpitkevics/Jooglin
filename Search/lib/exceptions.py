

class PurchaseException(Exception):
    def __init__(self, message):
        self.message = message

        # Call the base class constructor with the parameters it needs
        super(PurchaseException, self).__init__(message)
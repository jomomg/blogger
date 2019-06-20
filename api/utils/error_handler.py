from .response import error_


class ValidationError(Exception):
    status_code = 400

    def __init__(self, message, data=None, status_code=None):
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.data = data

    def to_dict(self):
        return error_(self.message, self.data)

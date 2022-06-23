from flask import jsonify

class CommonError(Exception):
    def __init__(self, code_error):
        self.code_error = str(code_error)
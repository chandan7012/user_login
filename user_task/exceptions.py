
# Written by Chandan Sharma on 19/03/2025
# ---------------------------------------
# Custom Exceptions

class ConfigurationError(Exception):
    def __init__(self, message: object) -> None: 
        super().__init__(message)
        self.message = message
        
class CommonError(Exception):
    def __init__(self, message: object) -> None:
        super().__init__(message)
        self.message = message
        
class AuthorizationError(Exception):
    def __init__(self, message: object) -> None:
        super().__init__(message)
        self.message = message
        
class ParameterError(Exception):
    def __init__(self, message: object) -> None:
        super().__init__(message)
        self.message = message
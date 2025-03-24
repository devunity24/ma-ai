

class Utility:
    
    @staticmethod
    def isStringEmptyOrNull(input):
        return input is None or len(input) == 0

    @staticmethod
    def isStringNonEmpty(input):
        return input is not None and len(input) > 0

class ValidationResult:
    def __init__(self, is_valid: bool, obj=None):
        self.obj = obj
        self.is_valid = is_valid

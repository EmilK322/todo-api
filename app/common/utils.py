def get_self_if_true_or_default(check_obj, default_val):
    ret_val = check_obj if check_obj else default_val
    return ret_val


class FuncDTO:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs


class ValidationResult:
    def __init__(self, is_valid, message):
        self.is_valid = is_valid
        self.message = message

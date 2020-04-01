def get_self_if_true_or_default(check_obj, default_val):
    ret_val = check_obj if check_obj else default_val
    return ret_val

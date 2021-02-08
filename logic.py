def wd_sum(val_1, val_2):
    if not val_1 or not (type(val_1) == int or float):
        raise Exception('val_1 has to be a number')

    if not val_2 or not (type(val_2) == int or float):
        raise Exception('val_2 has to be a number')

    return val_1 + val_2
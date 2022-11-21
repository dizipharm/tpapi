
def field_setter(value):
    if value and type(value) is str:
        return value.strip()
    elif value and type(value) is int:
        return float(value)
    else:
        return value

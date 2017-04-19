def data_type(value):
    if type(value) == str:
        return len(value)

    if value is None:
        return 'no value'

    if type(value) == bool:
        return value

    if type(value) == int:
        if value < 100:
            return 'less than 100'

        if value == 100:
            return 'equal to 100'

        if value > 100:
            return 'more than 100'

    if type(value) == list:
        if len(value) < 3:
            return None
        else:
            return value[2]

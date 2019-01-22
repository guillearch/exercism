def slices(series, length):
    if 0 < length <= len(series):
        substrings = []
        for i in range(len(series)):
            num = series[i:i+length]
            if len(num) == length:
                substrings.append(num)
        return substrings
    else:
        raise ValueError('Invalid length.')

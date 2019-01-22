def is_armstrong(number):
    return number == sum([pow(int(i), len(str(number))) for i in str(number)])

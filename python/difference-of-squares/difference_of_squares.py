def square_of_sum(count):
    return pow(sum(n for n in range(count+1)), 2)


def sum_of_squares(count):
    return sum(pow(n, 2) for n in range(count+1))


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)

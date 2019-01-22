from functools import reduce

def largest_product(series, size):

    if size == 0:
        return 1

    elif size > (len(series)) or size < 0:
        raise ValueError('Invalid size.')

    else:
        products = {}
        for i in range(len(series)):
            value = series[i:i+size]
            if len(value) == size:
                key = reduce(lambda x,y:x*y, [int(a) for a in value])
                products.update({key:value})
                print(f"{value}:{key}")
        return max(products)

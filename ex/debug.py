def funcA(first_val, second_val):
    result = (first_val * 2) - (second_val / 2)
    return result




def functionB(first_val=23, last_val=72):
    # we would place our break point here
   

    response = funcA(first_val, last_val)
    result = response * first_val / 7
    return result


functionB(33, 88)

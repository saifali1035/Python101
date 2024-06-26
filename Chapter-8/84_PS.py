def sum_of_nat(range):
    if range <= 1:
        return range
    return range + sum_of_nat(range-1)




print(sum_of_nat(7))
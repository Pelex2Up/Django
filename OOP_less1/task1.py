arr2 = [1, 2, 3, 4, 5, 6]


def sum_array(array, summa=0):
    for i in array:
        summa += i
    return summa


print(sum_array(arr2))
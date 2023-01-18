# Write a function that will get a non-negative number matrix. Calculate the sum of the elements in each column.
# Determine which column contains the maximum amount. Find the smallest element of that column, the function must
# return the value of that element.

def func(matrix: list) -> int:
    value = 0
    max = 0
    for i in matrix:
        for j in i:
            value += j
        if max < value:
            max = value
        value = 0
        i.append(max)
    min = max
    for i in matrix:
        if max in i:
            for j in i:
                if min > j:
                    min = j
    return min


# Write a function that will get a non-negative number matrix. Calculate the sum of the elements in each column.
# Determine which column contains the maximum amount. The function must return the largest sum regular the column serial number.

from random import randint
bigg = []
matrix = []
size = int(input("Enter matrix size"))

for i in range(size):
    matrix.append([randint(1, 100)]*size)
sum = 0
max = 0
for i in matrix:
    for j in i:
       sum += j
    if sum > max:
        max = sum
    bigg = i


print(matrix)

print("{} is max in line {}".format(max, i))

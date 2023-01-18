#In the entered interval of natural numbers, find those whose number of divisors is not less than the entered value.
#  For the found numbers, display the number of divisors and all divisors.

interval = int(input("Enter interval: "))
value = int(input("Enter value: "))
divisors = []
count = 0

for i in range(1, interval + 1):
    j = 1
    while j <= i:
        if i % j == 0:
            count += 1
            divisors.append(j)
            j += 1
    if count < value:
        print("{} s divisors are {}".format(i, divisors))
    j = 0
    divisors = []
    count = 0

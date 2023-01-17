# Ten natural numbers greater than 2 are entered. Calculate how many primes are among them.
def run():
    list = []
    n = int(input("Enter number: "))
    while n > 2:
        list.append(n)
        n = int(input("Enter number: "))
        if len(list) == 10:
            break
    count = 0

    for i in list:
        if i % 2 == 0:
            count += 1

    print(count)

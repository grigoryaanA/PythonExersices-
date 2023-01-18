# Write a function that determines the number of digits entered.

def func():
    num = input("Enter a number: ")

    count = 0

    for i in num:
        count += 1

    return count

# Write a function that will get a list. Find the greatest common divisors for any two numbers in the list. The function
# must return a list containing the largest common divisors of all the numbers in the received list.

def find_divisors(array: list) -> list:
    divisors = []

    for i in range(len(array)):
        for j in range(i, len(array)):
            divisor = min(array[i], array[j])

            while divisor > 0:
                if array[i] % divisor == 0 and array[j] % divisor == 0:
                    divisors.append(divisor)
                    break
                divisor -= 1

    return divisors

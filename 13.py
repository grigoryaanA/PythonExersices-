# Write a function that will get the matrix to sort the sequence of columns so
# that the elements in their first column are in ascending order.
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def sort(array: list) -> list:
    for i in array:
        bubbleSort(i)
    return array

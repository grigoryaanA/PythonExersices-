
def func(number: int):
    if number < 0:
        print("Namber has to be positiv")
    num = number.__str__()
    for i in num:
        if int(i) % 2 != 0:
            num.replace(i, "")
            print(num)
    print(num)
    return int(num)

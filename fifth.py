 size = 10
    rectangle = []

    for i in range(size):
        rectangle.append(["*"] * size)


    for i in range(size):
        for j in range(size):
            if i == 0 or j == 0 or i == size - 1 or j == size -1 :
                rectangle[i][j] = "o"

    for i in range(size):
        for j in range(size):
            print(rectangle[i][j], end=" ")
        print()

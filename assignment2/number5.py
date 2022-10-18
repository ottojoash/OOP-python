hat = [1, 2, 3, 4, 5]


number = int(input())


hat[len(hat) // 2] = number


hat.pop(-1)


print(len(hat))
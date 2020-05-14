n = input("Введите числа через пробел: ").split()
num = [int(i) for i in n]
for k in num:
    count = 0
    for j in num:
        if k == j:
            count += 1
    if count == 1:
        print(k)

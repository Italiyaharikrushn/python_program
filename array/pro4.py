a = [20, 10, 40, 30, 60, 50]

for i in range(len(a)) :
    for j in range(i+1, len(a)):
        # temp = 0
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

    print(a[i], end = " ")

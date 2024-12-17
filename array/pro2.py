a = [1,5,3,2,6,4,9,8,10,7]

for x in a :
    if x % 2 != 0 :
        print(x)

for x in range(len(a)):
    for y in range(x+1, len(a)):
        if a[x]>a[y]:
            z = a[x]
            a[x] = a[y]
            a[y] = z
            # break
    
    print(a[x], end=' ')

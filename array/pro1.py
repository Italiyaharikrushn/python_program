# a = [1,2,3,4,5,6]
# sum = 0

# for x in a : 
#     sum = sum + x

# print(sum)

a = [2,3,4,5,6,7]
min = a[0]
max = a[0]
sum = 0
for x in range(len(a)):
    sum += a[x]
    
    if min>a[x]:
        min=a[x]
        
    if max<a[x]:
        max=a[x]
print(sum-min,sum-max)
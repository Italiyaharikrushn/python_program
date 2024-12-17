n = 12345
m = str(n)

def getSum():
    sum = 0
    for x in m: 
      sum = sum + int(x)
    return sum

print(getSum())

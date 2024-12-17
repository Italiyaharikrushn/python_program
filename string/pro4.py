a = "Hello World!"

def rev(a):
    b = ''
    for x in a:
        b = x + b
    return b
print(rev(a), end="")

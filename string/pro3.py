# a = input()
# b = input()
# c = input()
# result = ''
# for x in a:
#     if x == b :
#         x = c
#     result = result + x
# print(result)

a = "Hello"
b = "H"
c = "J"
result = ""

for x in a:
    if x == b:
        x = c
    result += x

print(result)

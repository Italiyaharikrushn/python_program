b = "madam"
p = ''
for x in b:
    if x not in p:
        p = p + x

print(p, end = " ")


# a = 5
# for x in range(a):
#     for y in range(x,a):
#         print("#",  end=" ")
#     print("")

# a = 5
# for x in range(a):
#     for y in range(1, a-x):
#         print(" ", end="")
    
#     for z in range(x+1):
#         print("#", end=" ")
#     print()
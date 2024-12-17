a = "abcbamnoonm"

def palindrome(a):
    return a == a[::-1]
    
def pali(a):
    b = []
    
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            c = a[i:j]
            
            if palindrome(c) and len(c)>1 :
                b.append(c)
                
    return b

pali_list = pali(a)
print(pali_list)

y = 0
for x in pali_list:
    if len(x) > y:
        y = len(x)
        res = x
print("-----------------------")
print("Max Palindrome : ",[res])
# -------------------------------------------------------------
# a = [
#     [1,2,3],
#     [4,5,6],
#     [9,8,9]
# ]

# def dia_sum(a):
#     n = len(a)
#     sum = 0
#     anti_sum = 0

#     for i in range(n):
#         sum = sum + a[i][i]
#         anti_sum += a[i][n-1-i]

#     return sum, anti_sum

# sum, anti_sum = dia_sum(a)
# # print(sum)
# # print(anti_sum)

# total = sum - anti_sum
# print(total)
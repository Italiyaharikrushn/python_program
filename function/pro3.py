# call by value
# string =  "geeks"

# def test(string) :
#     string = "geeksforgeeks"
#     print("Inside function : ", string)

# test(string)
# print("Outside Function : ", string)

list1 = [2,4,6]
list2 = list1

print(list1)
print(list2)

list1.append(8)

print(list1)
print(list2)

list1 = list1 + [10] 
print(list1)
print(list2)

list1.append(12)

print(list1)
print(list2)
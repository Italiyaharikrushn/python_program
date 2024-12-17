a = 10
b = str(a)
rev = ''

for i in b:
    rev = i + rev

if(b==rev):
    print("Palindrome")

else:
    print("Not Palindrome")

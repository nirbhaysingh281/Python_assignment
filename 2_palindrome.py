#python program that takes a string n as user input and prints whether the string is a palindrome or not

n = input("Enter String: ")
w = "" 
for i in n: 
    w = i + w 
if (n==w): 
    print("yes, It is Pelindrome")
else:
    print("It is not Pelindrome")
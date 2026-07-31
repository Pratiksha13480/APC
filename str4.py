# Check whether the entered string is a palindrome
string = input("Enter a string: ")

rev = ""
for ch in string:
    rev = ch + rev

if string == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
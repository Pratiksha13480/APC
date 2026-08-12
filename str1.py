# 1. Write a program to input a string and display its length without using the len() function. 

s = input("enter string:")

count = 0
for i in s:
    count += 1
print("length: ", count)    


# 2. Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 

s = input("enter string:")

for ch in s:
    vowels = consonants = digits = spaces = specialCharcter = 0
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch ==  " ":  
        spaces += 1
    else:
        specialCharcter += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", specialCharcter)


# 3.Reverse the given string without using built-in reverse functions. 

s = input("Enter a string: ")

rev = ""
for ch in s:
    rev = ch + rev

print("Reverse:", rev)

# 4. Check whether the entered string is a palindrome
string = input("Enter a string: ")

rev = ""
for ch in string:
    rev = ch + rev

if string == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# 5.Count the number of uppercase and lowercase letters in a string. 

string  = input("Enter a string: ")

upper = lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)


# 6.replace all occurrences of a given character with another character

s = input("Enter a string: ")
old = input("Character to replace: ")
new = input("New character: ")

result = ""

for ch in s:
    if ch == old:
        result += new
    else:
        result += ch

print(result)

# 7.Remove all spaces from the input string. 

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print(result)

# 8.Find the number of times a specified character appears in a string. 

s = input("Enter a string: ")
ch = input("Enter character: ")

count = 0

for i in s:
    if i == ch:
        count += 1

print("Frequency:", count)


# 9. Print the first and last character of a string. 

s = input("Enter a string: ")

if s:
    print("First:", s[0])
    print("Last:", s[-1])
else:
    print("Empty String")


# 10. Display each character of a string along with its ASCII value.

s = input("Enter a string: ")

for ch in s:
    print(ch, ":", ord(ch))
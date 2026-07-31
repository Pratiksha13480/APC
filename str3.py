# 21. •	Validate a password based on these conditions: 
# Validate a password based on these conditions: 
# Minimum 8 characters 
# At least one uppercase letter 
# One lowercase letter 
# One digit 
# One special character

password = input("Enter password: ")

upper = lower = digit = special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")


# 22. Compress a string by counting consecutive repeated characters. 

s = input("Enter string: ")

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += s[i - 1] + str(count)
        count = 1

result += s[-1] + str(count)

print(result)


# 23.Compress repeated characters and return the original string if compression does not reduce the length. 
s = input("Enter string: ")

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += s[i - 1] + str(count)
        count = 1

result += s[-1] + str(count)

if len(result) < len(s):
    print(result)
else:
    print(s)

# 24.Find the character with the highest frequency.    

s = input("Enter string: ")

max_char = ""
max_count = 0

for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_char = ch

print(max_char)

# 25. Find the second most frequently occurring character. 
s = input("Enter string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

if len(items) >= 2:
    print(items[1][0])
else:
    print("Not Available")

# 26.Encrypt and decrypt a message using the Caesar Cipher algorithm.     

text = input("Enter message: ")
shift = int(input("Enter shift: "))

encrypted = ""

for ch in text:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        encrypted += chr((ord(ch) - base + shift) % 26 + base)
    else:
        encrypted += ch

print("Encrypted:", encrypted)


# 27. Validate whether a given email address follows a valid format.

email = input("Enter email: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid Email")
else:
    print("Invalid Email")

# 28.Count the frequency of every word in a paragraph.
      
text = input("Enter paragraph: ")

words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

for key, value in freq.items():
    print(key, ":", value)


# 29. •	Reverse the order of words in a sentence without changing the words themselves. 
# Example:
# Input: Python is easy
# Output: easy is Python

s = input("Enter sentence: ")

words = s.split()

for i in range(len(words) - 1, -1, -1):
    print(words[i], end=" ")


# 30. Check whether one string is a rotation of another. 
# Example: ABCD, CDAB
# Output: Yes

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes")
else:
    print("No")


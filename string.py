#1.Write a program to input a string and display its length without using the len() function. 
s = input("Enter a string: ")

count = 0
for ch in s:
    count += 1

print("Length:", count)

#2.Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 
s = input("Enter a string: ")

vowels = consonants = digits = spaces = special = 0

for ch in s:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

#3.Reverse the given string without using built-in reverse functions.  
s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

print("Reversed string:", reverse)

#4.Check whether the entered string is a palindrome. 
s = input("Enter a string: ")
reverse = ""

for ch in s:
    reverse = ch + reverse

if s == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

#5.Count the number of uppercase and lowercase letters in a string. 
s = input("Enter a string: ")

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)

#6.Replace all occurrences of a given character with another character. 
 s = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for ch in s:
    if ch == old:
        result += new
    else:
        result += ch

print("Result:", result)

#7.Remove all spaces from the input string. 
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print("Without spaces:", result)

#8.Find the number of times a specified character appears in a string. 
s = input("Enter a string: ")
target = input("Enter character: ")

count = 0

for ch in s:
    if ch == target:
        count += 1

print("Frequency:", count)

#9.Print the first and last character of a string. 
s = input("Enter a string: ")

if len(s) > 0:
    print("First character:", s[0])
    print("Last character:", s[-1])
else:
    print("String is empty")

#10.Display each character of a string along with its ASCII value.
s = input("Enter a string: ")

for ch in s:
    print(ch, "=", ord(ch))

# 11.Count the total number of words in a sentence. 
s = input("Enter a sentence: ")
words = s.split()
print("Number of words:", len(words))

# 12.Find the longest word in a given sentence. 
s = input("Enter a sentence: ")

words = s.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

#13.Find the shortest word in a sentence. 
s = input("Enter a sentence: ")
words = s.split()

if words:
    shortest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word

    print("Shortest word:", shortest)

#14.Convert the first letter of every word to uppercase. 
s = input("Enter a sentence: ")
words = s.split()
result = ""

for word in words:
    result += word[0].upper() + word[1:] + " "

print("Title Case:", result.strip())

#15.Print all duplicate characters in a string. 
s = input("Enter a string: ")
duplicates = ""

for ch in s:
    if s.count(ch) > 1 and ch not in duplicates:
        duplicates += ch

print("Duplicate characters:", duplicates)

#16.Display the frequency of every character in a string. 
s = input("Enter a string: ")
frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch in frequency:
    print(ch, ":", frequency[ch])

#17.Check whether two strings are anagrams.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not anagrams")


#18.Remove duplicate characters while maintaining the original order. 
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("After removing duplicates:", result)

#19. Check whether a given substring exists in the main string. 
main_string = input("Enter main string: ")
substring = input("Enter substring: ")

if substring in main_string:
    print("Substring exists")
else:
    print("Substring does not exist")

# 20.Count how many times a specific word appears in a sentence. 
sentence = input("Enter a sentence: ")
word = input("Enter word to search: ")
words = sentence.split()
count = 0

for w in words:
    if w == word:
        count += 1

print("Occurrences:", count)

#21.Validate a password based on these conditions:Minimum 8 characters,At least one uppercase letter 
#One lowercase letter,One digit,One special character
password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Valid Password")
else:
    print("Invalid Password")

#22. Compress a string by counting consecutive repeated characters.Example Input: aaabbcccc Output: a3b2c4d1
s = input("Enter a string: ")
result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += s[i - 1] + str(count)
        count = 1

if len(s) > 0:
    result += s[-1] + str(count)

print("Compressed:", result)

#23.Compress repeated characters and return the original string if compression does not reduce the length. 
s = input("Enter a string: ")
compressed = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        compressed += s[i - 1] + str(count)
        count = 1

if len(s) > 0:
    compressed += s[-1] + str(count)

if len(compressed) < len(s):
    print("Compressed:", compressed)
else:
    print("Original:", s)

#24.Find the character with the highest frequency. 
s = input("Enter a string: ")
frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

most_frequent = ""
max_count = 0

for ch in frequency:
    if frequency[ch] > max_count:
        max_count = frequency[ch]
        most_frequent = ch

print("Most frequent character:", most_frequent)
print("Frequency:", max_count)

#25.Find the second most frequently occurring character. 
s = input("Enter a string: ")
frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

values = sorted(frequency.values(), reverse=True)

if len(values) >= 2:
    second_count = values[1]

    for ch in frequency:
        if frequency[ch] == second_count:
            print("Second most frequent character:", ch)
            print("Frequency:", second_count)
            break
else:
    print("Not enough different characters")

#26.Encrypt and decrypt a message using the Caesar Cipher algorithm. 
s = input("Enter message: ")
shift = int(input("Enter shift: "))
encrypted = ""

for ch in s:
    if ch.isupper():
        encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    elif ch.islower():
        encrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    else:
        encrypted += ch

print("Encrypted:", encrypted)
decrypted = ""

for ch in encrypted:
    if ch.isupper():
        decrypted += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
    elif ch.islower():
        decrypted += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
    else:
        decrypted += ch

print("Decrypted:", decrypted)

#27.Validate whether a given email address follows a valid format. 
email = input("Enter email: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid Email")
else:
    print("Invalid Email")

#28.Count the frequency of every word in a paragraph
paragraph = input("Enter a paragraph: ")
words = paragraph.lower().split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word in frequency:
    print(word, ":", frequency[word])

#29.Reverse the order of words in a sentence without changing the words themselves.Example:Input: Python is easy
#Output: easy is Python
sentence = input("Enter a sentence: ")
words = sentence.split()
result = ""

for i in range(len(words) - 1, -1, -1):
    result += words[i] + " "

print("Reversed sentence:", result.strip())


#30.Check whether one string is a rotation of another. Example:ABCD CDA Output: Yes
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in s1 + s1:
    print("Yes, strings are rotations")
else:
    print("No, strings are not rotations")
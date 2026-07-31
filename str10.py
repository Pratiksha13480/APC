# •	Display each character of a string along with its ASCII value.

s = input("Enter a string: ")

for ch in s:
    print(ch, ":", ord(ch))
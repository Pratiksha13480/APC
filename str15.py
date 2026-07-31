# Print all duplicate characters in a string. 

s = input("Enter a string: ")

printed = ""

for ch in s:
    if s.count(ch) > 1 and ch not in printed:
        print(ch)
        printed += ch
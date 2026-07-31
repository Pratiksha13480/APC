#  Convert the first letter of every word to uppercase. 
s = input("Enter a sentence: ")

words = s.split()

result = ""

for word in words:
    result += word[0].upper() + word[1:].lower() + " "

print(result)
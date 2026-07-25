#check whether a character is a vowel or consonant

ch = input("Enter a character: ")

if ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print("Vowel")
else:
    print("Consonant")
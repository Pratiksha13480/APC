# 11.Count the total number of words in a sentence

s = input("Enter a sentence: ")

words = s.split()

print("Word Count:", len(words))


# 12. Find the longest word in a given sentence. 
s = input("Enter a sentence: ")

words = s.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)


# 13.Find the shortest word in a sentence. 

s = input("Enter a sentence: ")

words = s.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest Word:", shortest)


# 14.Convert the first letter of every word to uppercase. 
s = input("Enter a sentence: ")

words = s.split()

result = ""

for word in words:
    result += word[0].upper() + word[1:].lower() + " "

print(result)

# 15.Print all duplicate characters in a string. 

s = input("Enter a string: ")

printed = ""

for ch in s:
    if s.count(ch) > 1 and ch not in printed:
        print(ch)
        printed += ch


# 16. Display the frequency of every character in a string. 

s = input("Enter a string: ")

done = ""

for ch in s:
    if ch not in done:
        print(ch, ":", s.count(ch))
        done += ch


# 17. Check whether two strings are anagrams.    
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")     


# 18. Remove duplicate characters while maintaining the original order.  

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)   


# 19. Check whether a given substring exists in the main string. 

s = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in s:
    print("Found")
else:
    print("Not Found")


# 20. Count how many times a specific word appears in a sentence. 
s = input("Enter sentence: ")
word = input("Enter word: ")

words = s.split()

count = 0

for w in words:
    if w == word:
        count += 1

print("Occurrences:", count)


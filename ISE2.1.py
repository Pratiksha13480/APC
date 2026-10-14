import string 
from collections import Counter

with open("sample.py", "r") as file:
    text = file.read()
    text = text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")
        words = text.split()
        print("total words: ", len(words))
        count = Counter(words)
        print("\ntop frequent words")
        for word, frequecy in count.mostCommon(10):
            print(word, ":", frequecy)

    
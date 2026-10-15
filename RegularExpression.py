
import re

# 1. Write a Python program using regular expressions to extract all digits from a given string.
text = input("1. Enter a string: ")
print("Digits:", re.findall(r'\d', text))

# 2. Accept a sentence and display all words beginning with A or a.
text = input("2. Enter a sentence: ")
print("Words:", re.findall(r'\b[Aa]\w*', text))

# 3. Count the occurrences of vowels in a given string using regular expressions.
text = input("3. Enter a string: ")
vowels = re.findall(r'[aeiouAEIOU]', text)
print("Vowels:", vowels, "Count:", len(vowels))

# 4. Extract all uppercase letters from a given string.
text = input("4. Enter a string: ")
print("Uppercase letters:", re.findall(r'[A-Z]', text))

# 5. Identify all spaces, tabs, and newline characters in a text.
text = input("5. Enter text: ")
print("Whitespace:", re.findall(r'[ \t\n]', text))

# 6. Replace multiple consecutive spaces with a single space.
text = input("6. Enter text: ")
print("Result:", re.sub(r' +', ' ', text))

# 7. Display all words containing exactly five characters.
text = input("7. Enter a sentence: ")
print("Five-character words:", re.findall(r'\b[A-Za-z]{5}\b', text))

# 8. Identify all words ending with the letter s.
text = input("8. Enter a sentence: ")
print("Words ending with s:", re.findall(r'\b\w+s\b', text))

# 9. Remove special characters but retain letters, digits, and spaces.
text = input("9. Enter a string: ")
print("Clean text:", re.sub(r'[^A-Za-z0-9 ]', '', text))

# 10. Count the number of words in a sentence.
text = input("10. Enter a sentence: ")
print("Word count:", len(re.findall(r'\b\w+\b', text)))

# 11. Validate a 10-digit Indian mobile number.
mobile = input("11. Enter mobile number: ")
print("Valid" if re.fullmatch(r'[6-9]\d{9}', mobile) else "Invalid")

# 12. Check whether an email address follows a reasonable format.
email = input("12. Enter email address: ")
pattern = r'[\w.-]+@[\w.-]+\.[A-Za-z]{2,}'
print("Valid" if re.fullmatch(pattern, email) else "Invalid")

# 13. Extract dates in DD-MM-YYYY format from a paragraph.
text = input("13. Enter a paragraph: ")
print("Dates:", re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text))

# 14. Identify web addresses beginning with http:// or https://.
text = input("14. Enter text containing URLs: ")
print("URLs:", re.findall(r'https?://[^\s]+', text))

# 15. Extract all hashtags from a social media post.
text = input("15. Enter a social media post: ")
print("Hashtags:", re.findall(r'#[A-Za-z0-9_]+', text))

# 16. Check password length, uppercase, lowercase, digit, and special character.
password = input("16. Enter password: ")
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9])\S{8,}'
print("Strong password" if re.fullmatch(pattern, password) else "Weak password")

# 17. Identify consecutive repeated words, ignoring case differences.
text = input("17. Enter a sentence: ")
print("Repeated words:", re.findall(r'\b(\w+)\s+\1\b', text, re.IGNORECASE))

# 18. Extract six-digit Indian PIN codes from a paragraph.
text = input("18. Enter a paragraph: ")
print("PIN codes:", re.findall(r'\b[1-9]\d{5}\b', text))

# 19. Validate a common Indian vehicle registration number.
number = input("19. Enter vehicle number: ")
pattern = r'[A-Z]{2}\d{2}[A-Z]{1,3}\d{4}'
print("Valid" if re.fullmatch(pattern, number) else "Invalid")

# 20. Extract file extensions from filenames in a string.
text = input("20. Enter filenames: ")
print("Extensions:", re.findall(r'\.([A-Za-z0-9]+)\b', text))

# 21. Remove HTML tags, extra whitespace, and unwanted punctuation.
text = input("21. Enter HTML text: ")
text = re.sub(r'<[^>]*>', '', text)        # Remove HTML tags
text = re.sub(r'\s+', ' ', text)           # Replace extra whitespace
text = re.sub(r'[^\w\s]', '', text)         # Remove punctuation
print("Clean text:", text.strip())

# 22. Extract invoice numbers, dates, and monetary amounts from invoice text.
text = input("22. Enter invoice text: ")
print("Invoice:", re.findall(r'INV-\d+', text))
print("Dates:", re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text))
print("Amounts:", re.findall(r'Rs\.?\s*\d+(?:\.\d{1,2})?', text))

# 23. Identify single-line comments in Python source code.
# Regex alone may not correctly handle # inside strings or multiline cases.
text = input("23. Enter Python source code: ")
print("Comments:", re.findall(r'(?m)^\s*#.*$', text))
# Note: tokenize is more accurate for analysing Python source code.

# 24. Validate product codes in the format ABC-1234-XY.
code = input("24. Enter product code: ")
pattern = r'[A-Z]{3}-\d{4}-[A-Z]{2}'
print("Valid" if re.fullmatch(pattern, code) else "Invalid")

# 25. Extract student names, roll numbers, and marks from a paragraph.
text = input("25. Enter student details: ")
pattern = r'Name:\s*(\w+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)'
students = re.findall(pattern, text)
for name, roll, marks in students:
    print("Name:", name, "Roll:", roll, "Marks:", marks)

# 26. Extract DOI identifiers, publication years, emails, and URLs.
text = input("26. Enter research paper reference: ")
print("DOI:", re.findall(r'\b10\.\d{4,9}/[^\s]+', text))
print("Years:", re.findall(r'\b(?:19|20)\d{2}\b', text))
print("Emails:", re.findall(r'[\w.-]+@[\w.-]+\.[A-Za-z]{2,}', text))
print("URLs:", re.findall(r'https?://[^\s]+', text))

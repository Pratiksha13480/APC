#1.Create a dictionary containing student details such as roll number, name, department, and marks. Display all key-value pairs.
student = {
    "roll_no": 31,
    "name": "Pratiksha",
    "department": "CSE",
    "marks": 99
}

for key, value in student.items():
    print(key, ":", value)

#2.	Create a dictionary containing employee information and display the value associated with a specified key.
employee = {
    "id": 101,
    "name": "Rahul",
    "department": "IT",
    "salary": 50000
}

key = input("Enter key: ")

if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found")

#3.	Create a dictionary of five products and their prices. Add a new product and price to the dictionary.
products = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1000,
    "Monitor": 10000,
    "Printer": 8000
}

products["Headphones"] = 1500

print(products)

#4.	Create a dictionary containing student marks. Update the marks of a specified student.
marks = {
    "Rahul": 75,
    "Priya": 82,
    "Amit": 68
}

marks["Rahul"] = 90

print(marks)

#5.	Create a dictionary of cities and their populations. Remove a specified city from the dictionary.
cities = {
    "Mumbai": 20000000,
    "Pune": 7000000,
    "Delhi": 19000000,
    "Sangli": 500000
}

del cities["Sangli"]

print(cities)

#6.	Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.
employees = {
    101: "Rahul",
    102: "Priya",
    103: "Amit"
}

emp_id = int(input("Enter employee ID: "))
if emp_id in employees:
    print("Employee exists:", employees[emp_id])
else:
    print("Employee does not exist")

#7.	Create a dictionary containing student records and find the total number of key-value pairs.
students = {
    "Rahul": 80,
    "Priya": 90,
    "Amit": 75,
    "Sneha": 85
}

print("Total key-value pairs:", len(students))

#8.Create a dictionary and display:All keys,All values ,All key-value pairs
data = {
    "name": "Pratiksha",
    "age": 20,
    "department": "CSE"
}

print("Keys:", data.keys())
print("Values:", data.values())
print("Key-Value pairs:", data.items())

#9.Create a dictionary of programming languages and their creators. Display each key and value using a loop.
languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "JavaScript": "Brendan Eich"
}

for language, creator in languages.items():
    print(language, ":", creator)

#10.Accept five student names and their marks from the user and store them in a dictionary.
students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

print(students)

#11.Create a dictionary containing student names and marks. Find the student who has scored the highest marks.
students = {
    "Rahul": 75,
    "Priya": 92,
    "Amit": 85,
    "Sneha": 88
}

highest = max(students, key=students.get)
print("Highest marks:", highest)
print("Marks:", students[highest])

#12.Create a dictionary containing student names and marks. Find the student with the lowest marks.
students = {
    "Rahul": 75,
    "Priya": 92,
    "Amit": 65,
    "Sneha": 88
}

lowest = min(students, key=students.get)
print("Lowest marks:", lowest)
print("Marks:", students[lowest])

#13.Create a dictionary containing student names and marks. Calculate the average marks of all students.
students = {
    "Rahul": 75,
    "Priya": 92,
    "Amit": 85,
    "Sneha": 88
}

average = sum(students.values()) / len(students)
print("Average marks:", average)

#14.Accept a string from the user and create a dictionary containing each character and its frequency.
text = input("Enter a string: ")
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)

#15.Accept a sentence and create a dictionary containing each word and the number of times it occurs.
sentence = input("Enter a sentence: ")
words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

#16.Create two dictionaries and merge them into a single dictionary.
dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}
merged = {**dict1, **dict2}
print(merged)

#17.Given two dictionaries, find the keys that are common to both dictionaries.
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 40, "c": 50, "d": 60}
common = dict1.keys() & dict2.keys()
print("Common keys:", common)

#18.	Given two dictionaries, identify the values that are common to both dictionaries.
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"x": 20, "y": 30, "z": 40}
common = set(dict1.values()) & set(dict2.values())
print("Common values:", common)

#19.Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

result = {}
for key, value in data.items():
    if value not in result.values():
        result[key] = value

print(result)

#20.Create a dictionary and display its elements in ascending order of keys.
data = {
    30: "C",
    10: "A",
    20: "B",
    5: "D"
}

for key in sorted(data):
    print(key, ":", data[key])

#21.Create a dictionary containing numbers from 1 to 10 as keys and their squares as values.
squares = {}
for i in range(1, 11):
    squares[i] = i * i

print(squares)
#22.Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.
squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i * i

print(squares)

#23.Given a list of numbers, create a dictionary containing each unique number and its frequency.
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)

#24.Create a dictionary containing integers from 1 to 10 and their cubes.
cubes = {}

for i in range(1, 11):
    cubes[i] = i ** 3

print(cubes)

#25.Create a dictionary containing student names and marks. Develop a program to:Add a student,Update marks
#Delete a student,Search for a student,Display all students,Find the highest marks,Calculate the average
students = {
    "Rahul": 75,
    "Priya": 90,
    "Amit": 82
}

while True:
    print("\n1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All")
    print("6. Highest Marks")
    print("7. Average")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks

    elif choice == 2:
        name = input("Enter name: ")
        if name in students:
            students[name] = float(input("Enter new marks: "))
        else:
            print("Student not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in students:
            del students[name]
        else:
            print("Student not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found")

    elif choice == 5:
        print(students)

    elif choice == 6:
        if students:
            name = max(students, key=students.get)
            print(name, students[name])

    elif choice == 7:
        if students:
            print("Average:", sum(students.values()) / len(students))

    elif choice == 8:
        break

    else:
        print("Invalid choice")

#26.Create a dictionary containing employee names and salaries. Find:Highest salary,Lowest salary 
#Average salary,Employees earning more than ₹50,000
employees = {
    "Rahul": 45000,
    "Priya": 65000,
    "Amit": 55000,
    "Sneha": 40000
}

print("Highest salary:", max(employees.values()))
print("Lowest salary:", min(employees.values()))
print("Average salary:", sum(employees.values()) / len(employees))

print("Employees earning more than 50000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)

#27.Create a dictionary containing product names and quantities.Perform:Add a product,Update quantity 
#Delete a product,Search for a product,Display products with quantity below 10
products = {
    "Laptop": 15,
    "Mouse": 5,
    "Keyboard": 8
}

products["Monitor"] = 12
products["Mouse"] = 20
del products["Keyboard"]

name = input("Search product: ")

if name in products:
    print("Quantity:", products[name])
else:
    print("Product not found")

print("Products with quantity below 10:")
for name, quantity in products.items():
    if quantity < 10:
        print(name, quantity)

#28.Create a dictionary containing names and phone numbers Implement:Add contact,Search contact,Update contact 
#Delete contact,Display all contacts
contacts = {
    "Rahul": "9876543210",
    "Priya": "9123456780"
}

contacts["Amit"] = "9876501234"

name = input("Search contact: ")
if name in contacts:
    print("Phone:", contacts[name])
else:
    print("Contact not found")

contacts["Rahul"] = "9999999999"

del contacts["Amit"]

print("All contacts:")
for name, phone in contacts.items():
    print(name, ":", phone)

#29.Create a dictionary containing book IDs and book names Implement:Add a book,Search a book,Remove a book,Display all books,Count total books
books = {
    101: "Python Programming",
    102: "Java Programming",
    103: "Data Structures"
}

books[104] = "Web Development"

book_id = int(input("Enter book ID to search: "))

if book_id in books:
    print("Book:", books[book_id])
else:
    print("Book not found")

del books[104]

print("All books:")
for book_id, name in books.items():
    print(book_id, ":", name)

print("Total books:", len(books))

#30.Take a dictionary containing student names and their departments; create a new dictionary that groups students according to their department.
students = {
    "Rahul": "CSE",
    "Priya": "IT",
    "Amit": "CSE",
    "Sneha": "ENTC",
    "Riya": "IT"
}

groups = {}

for name, department in students.items():
    if department not in groups:
        groups[department] = []

    groups[department].append(name)

print(groups)

#31.Take a list of words, create a dictionary where the key is the word length and the value is a list of words having that length.
words = ["cat", "dog", "apple", "banana", "sun", "book"]

result = {}

for word in words:
    length = len(word)

    if length not in result:
        result[length] = []

    result[length].append(word)

print(result)

#32.Take a list of integers and a target value, find two numbers whose sum is equal to the target using a dictionary.
numbers = [2, 7, 11, 15]
target = 9

seen = {}

for num in numbers:
    required = target - num

    if required in seen:
        print("Numbers:", required, num)
        break

    seen[num] = True

#33.Take a string, use a dictionary to find the first character that occurs only once.
text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] == 1:
        print("First non-repeating character:", char)
        break

#34.Take a string, use a dictionary to find the first character that occurs more than once.
text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] > 1:
        print("First repeating character:", char)
        break

#35.Accept a paragraph and create a dictionary where Key = word length,Value = number of words having that length.
paragraph = input("Enter a paragraph: ")

words = paragraph.split()
result = {}

for word in words:
    length = len(word)
    result[length] = result.get(length, 0) + 1

print(result)

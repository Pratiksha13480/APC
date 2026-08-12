# 1) Write a Python program to create a list of five fruits and display the list.
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print(fruits)

# 2) Create a list of five integers. Display:
# First element, Last element, Third element

numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])


# 3) Create a list of colors. Replace the third color with another color and 
# display the updated list.
color = ["white", "pink", "red", "blue", "black"]
print(color)
color[2] = "purple"
print(color)


# 4) Create a list of numbers. Add: One element at the end, One element at the beginning, 
# One element at a specified position.Display the updated list.
number = [1, 2, 3, 4, 5]
print(number)
number.append(8)
number.insert(0, 1)
number.insert(4, 9)
print(number)


# 5) Create a list of student names. Remove:First student, Last student, A specific student by name.
# Display the remaining list.
student = ["Yash", "Pratik", "Neha", "Sameer", "piya"]
print(student)
student.remove("Yash")
student.remove("piya")
student.remove("Sameer")
print(student)


# 6)Write a program to find the largest and smallest number in a list without using max() or min().
list = [10, 74, 53, 23, 83, 62]
largest = list[0]
smallest = list[0]
for i in list:
    if(i > largest):
        largest = i
    if(i < smallest):
        smallest = i    
print("largest", largest)
print("smallest", smallest)   


# 7)Accept 10 numbers from the user and store them in a list. Calculate:Sum,Average 
numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Numbers:", numbers)
total = 0

for num in numbers:
    total = total + num

print("Sum:", total)

average = total / 10
print("Average:", average)


# 8)Store 15 integers in a list. Count how many numbers are:Even, Odd
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)


# 9)Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.
cities = ["Pune", "Mumbai", "Sangli", "Kolhapur", "Nashik"]

city = input("Enter city name: ")

if city in cities:
    print("City exists in the list")
else:
    print("City does not exist in the list")


#10) Write a program to reverse a list without using the `reverse()` method.
numbers = [10, 20, 30, 40, 50]
reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Original list:", numbers)
print("Reversed list:", reversed_list)


#11) Create a list of 10 numbers and display:First 5 elements, Last 5 elements, Middle 4 elements,
# Alternate elements, Reverse list using slicing
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[5:])
print("Middle 4 elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse list:", numbers[::-1])


#12) Display all elements present at even index positions
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print("Elements at even index positions:")

for i in range(0, len(numbers), 2):
    print(numbers[i])


#13) Accept 10 numbers and sort them in:   
numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers.sort()
print("Ascending order:", numbers)
numbers.sort(reverse=True)
print("Descending order:", numbers)

# 14)Create a list containing duplicate values and display only unique elements. 
numbers = [10, 20, 10, 30, 20, 40, 30]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Unique elements:", unique)


# 15) Find the second largest element in a list.
numbers = [10, 50, 30, 40, 20]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

unique.sort()
print("Second largest:", unique[-2])


# 16) Create a nested list storing:Student Name, Roll Number,Marks .Display all student details.
students = [
    ["piya", 101, 85],
    ["Priya", 102, 90],
    ["komal", 103, 78]
]

for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()

# 17) Create two 3 × 3 matrices using nested lists and perform matrix addition    
matrix1 = [ 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] 
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Matrix Addition:")

for row in result:
    print(row)

# 18)Create a shopping cart using a list.Perform:Add item, Remove item, 
# Search item, Display cart, Count total items
cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

cart.remove("Mouse")

if "Laptop" in cart:
    print("Laptop is available")
else:
    print("Laptop is not available")

print("Cart:", cart)
print("Total items:", len(cart))


# 19) Store names of students present in class.Display:Total students, 
# Search a student's attendance, Add a new student,
# Remove an absent student 
students = ["Amit", "Priya", "Rahul", "Sneha"]
print("Total students:", len(students))
name = input("Search student: ")

if name in students:
    print("Student is present")
else:
    print("Student is absent")

students.append("Neha")
students.remove("Rahul")
print("Updated attendance list:", students)


# 20) Create a list of books.Implement:Add a new book, Search a book,Remove 
# a book,Display all books,Count total books
books = ["Python", "Java", "C++"]
books.append("JavaScript")
book = input("Search book: ")

if book in books:
    print("Book found")
else:
    print("Book not found")

books.remove("Java")

print("Books:", books)
print("Total books:", len(books))


# 21) Accept two lists and merge them into a single list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print("Merged list:", merged)


# 22) Find common elements between two lists
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
common = []

for num in list1:
    if num in list2:
        common.append(num)

print("Common elements:", common)


# 23) Count the frequency of each element in a list.
numbers = [10, 20, 10, 30, 20, 10]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency:", frequency)


# 24) Rotate a list:Left by one position,Right by one position
numbers = [10, 20, 30, 40, 50]
left = numbers[1:] + numbers[:1]
right = numbers[-1:] + numbers[:-1]
print("Left rotation:", left)
print("Right rotation:", right)


# 25) Remove all duplicate elements while preserving the original order.
numbers = [10, 20, 10, 30, 20, 40, 30]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("After removing duplicates:", unique)


# 26) Store marks of 20 students in a list and determine:Highest marks, Lowest marks, 
# Average marks, Number of students scoring above average,Number of students scoring below average
marks = [75, 80, 65, 90, 55, 70, 85, 60, 95, 88,
         72, 68, 77, 82, 91, 63, 74, 86, 58, 79]

highest = marks[0]
lowest = marks[0]
total = 0

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

total += mark
average = total / len(marks)
above = 0
below = 0

for mark in marks:
    if mark > average:
        above += 1
    elif mark < average:
        below += 1

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Above average:", above)
print("Below average:", below)


# 27) Store salaries of employees and determine:Highest salary, Lowest salary, Average salary, 
# Employees earning above ₹50,000 , Employees earning below ₹30,000 
salaries = [25000, 55000, 70000, 30000, 45000, 80000, 28000]
highest = salaries[0]
lowest = salaries[0]
total = 0

for salary in salaries:
    if salary > highest:
        highest = salary

    if salary < lowest:
        lowest = salary

    total += salary

average = total / len(salaries)

above_50000 = 0
below_30000 = 0

for salary in salaries:
    if salary > 50000:
        above_50000 += 1

    if salary < 30000:
        below_30000 += 1

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Above ₹50,000:", above_50000)
print("Below ₹30,000:", below_30000)


# 28) Store scores of a batsman in 10 matches and calculate:Highest score, Lowest score,Total runs 
#Average runs ,Number of centuries (≥100),Number of half-centuries (50–99)
scores = [45, 102, 75, 120, 34, 89, 150, 55, 99, 40]
highest = scores[0]
lowest = scores[0]
total = 0
centuries = 0
half_centuries = 0

for score in scores:
    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

    total += score

    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

average = total / len(scores)

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)


# 29) Store the temperature of 30 days and determine:Hottest day ,Coldest day ,Average temperature 
# Days above average temperature, Days below average temperature
temperatures = [
    30, 32, 29, 35, 31, 33, 28, 36, 34, 30,
    29, 31, 37, 33, 32, 35, 30, 28, 34, 36,
    31, 33, 29, 38, 35, 32, 30, 34, 37, 31
]

hottest = temperatures[0]
coldest = temperatures[0]
total = 0

for temp in temperatures:
    if temp > hottest:
        hottest = temp

    if temp < coldest:
        coldest = temp

    total += temp

average = total / len(temperatures)

above = 0
below = 0

for temp in temperatures:
    if temp > average:
        above += 1
    elif temp < average:
        below += 1

print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above)
print("Days below average:", below)


# 30) Store patient names and ages using lists.Perform:Add a patient, Delete a patient 
#Search a patient, Display all patients, Count total patients
patients = ["Amit", "Priya", "Rahul"]
patients.append("Sneha")
patients.remove("Rahul")
name = input("Enter patient name to search: ")

if name in patients:
    print("Patient found")
else:
    print("Patient not found")
print("All patients:")

for patient in patients:
    print(patient)

print("Total patients:", len(patients))

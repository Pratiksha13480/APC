# 33. Write a lambda function to calculate the square of a given number.
square = lambda x: x * x
n = int(input("Enter number: "))
print("Square =", square(n))

# 34. Create a lambda function that returns the cube of a number.
cube = lambda x: x ** 3
n = int(input("Enter number: "))
print("Cube =", cube(n))

# 35. Write a lambda function that returns True if a number is even and False otherwise.
even = lambda x: x % 2 == 0
n = int(input("Enter number: "))
print(even(n))

# 36. Use a lambda function to find the maximum of two numbers.
maximum = lambda a, b: a if a > b else b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum =", maximum(a, b))

# 37. Create a lambda function to calculate simple interest using principal, rate and time.
simple_interest = lambda p, r, t: (p * r * t) / 100
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
print("Simple Interest =", simple_interest(p, r, t))

# 38. Take a list of numbers and use map() and lambda to generate a list containing their squares.
numbers = list(map(int, input("Enter numbers: ").split()))
squares = list(map(lambda x: x * x, numbers))
print("Squares =", squares)

# 39. Use map() with lambda to calculate the cube of every element in a list.
numbers = list(map(int, input("Enter numbers: ").split()))
cubes = list(map(lambda x: x ** 3, numbers))
print("Cubes =", cubes)

# 40. Take two lists and use map() and lambda to create a third list containing the sum of corresponding elements.
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
result = list(map(lambda x, y: x + y, list1, list2))
print("Result =", result)

# 41. Take a list of integers and use filter() and lambda to extract all even numbers.
numbers = list(map(int, input("Enter numbers: ").split()))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers =", even_numbers)

# 42. Take a list of integers and use filter() with lambd to identify prime numbers.
def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True
numbers = list(map(int, input("Enter numbers: ").split()))
prime_numbers = list(filter(lambda x: prime(x), numbers))
print("Prime numbers =", prime_numbers)

# 43. Use filter() and lambda to extract positive numbers from a list.
numbers = list(map(int, input("Enter numbers: ").split()))
positive = list(filter(lambda x: x > 0, numbers))
print("Positive numbers =", positive)

# 44. Take a list of numbers and use filter() and lambda to find numbers greater than 50.
numbers = list(map(int, input("Enter numbers: ").split()))
result = list(filter(lambda x: x > 50, numbers))
print("Numbers greater than 50 =", result)

# 45. Take a list of words and use filter() and lambda to find words having more than five characters.
words = input("Enter words: ").split()
result = list(filter(lambda word: len(word) > 5, words))
print("Words =", result)


# 46. Take a list of words and sort them according to their length using lambda.
words = input("Enter words: ").split()
result = sorted(words, key=lambda word: len(word))
print("Sorted words =", result)

# 47. Take a list of tuples containing student names and marks and sort students according to their marks.
students = [
    ("Pratiksha", 85),
    ("Sneha", 92),
    ("Riya", 75),
    ("Amit", 88)
]

result = sorted(students, key=lambda x: x[1])
print("Students sorted by marks:")
for student in result:
    print(student)

# 48. Take employee records containing name and salary and sort them according to salary using lambda.
employees = [
    ("Amit", 45000),
    ("Riya", 60000),
    ("Sneha", 50000),
    ("Rahul", 75000)
]

result = sorted(employees, key=lambda x: x[1])
print("Employees sorted by salary:")

for employee in result:
    print(employee)

# 49. Take a list containing student names and marks.a) Calculate average marks.
# b) Filter students scoring above 75.c) Sort students according to marks.
students = [
    ("Pratiksha", 85),
    ("Sneha", 92),
    ("Riya", 72),
    ("Amit", 80)
]
def average_marks(students):
    marks = list(map(lambda x: x[1], students))
    return sum(marks) / len(marks)

# a) Calculate average marks
print("Average marks =", average_marks(students))

# b) Filter students scoring above 75
above_75 = list(filter(lambda x: x[1] > 75, students))

print("Students scoring above 75:")

for student in above_75:
    print(student)

# c) Sort students according to marks
sorted_students = sorted(students, key=lambda x: x[1])
print("Students sorted by marks:")
for student in sorted_students:
    print(student)

# 50. Take employee records containing name, department and salary.
#     a) Find employees earning more than 50000.
#     b) Increase salaries by 10%.
#     c) Sort employees according to salary.
employees = [
    ("Amit", "IT", 60000),
    ("Riya", "HR", 45000),
    ("Sneha", "IT", 75000),
    ("Rahul", "Sales", 50000)
]
# a) Employees earning more than 50000
high_salary = list(
    filter(lambda x: x[2] > 50000, employees)
)
print("Employees earning more than 50000:")
for employee in high_salary:
    print(employee)

# b) Increase salaries by 10%
increased_salary = list(
    map(lambda x: (x[0], x[1], x[2] * 1.10), employees)
)
print("Salaries after 10% increase:")
for employee in increased_salary:
    print(employee)

# c) Sort employees according to salary
sorted_employees = sorted(
    employees,
    key=lambda x: x[2]
)
print("Employees sorted by salary:")

for employee in sorted_employees:
    print(employee)

# 51. Take a list of products with names, prices and quantities.
#     a) Calculate total value of each product.
#     b) Filter products costing more than 1000.
#     c) Sort products according to total value.
products = [
    ("Laptop", 50000, 2),
    ("Mouse", 800, 3),
    ("Keyboard", 1500, 2),
    ("Monitor", 12000, 1)
]

# a) Calculate total value of each product
total_values = list(
    map(lambda x: (x[0], x[1], x[2], x[1] * x[2]), products)
)
print("Total value of products:")
for product in total_values:
    print(product)

# b) Filter products costing more than 1000
expensive = list(
    filter(lambda x: x[1] > 1000, products)
)
print("Products costing more than 1000:")

for product in expensive:
    print(product)

# c) Sort products according to total value
sorted_products = sorted(
    total_values,
    key=lambda x: x[3]
)

print("Products sorted by total value:")

for product in sorted_products:
    print(product)

# 52. Write a program using functions, map(), filter() and
#     lambda expressions to process a list of words.
#     a) Find length of every word.
#     b) Extract words having more than five characters.
#     c) Sort words according to their length

words = input("Enter words: ").split()
def word_lengths(words):
    return list(map(lambda word: len(word), words))

def long_words(words):
    return list(filter(lambda word: len(word) > 5, words))

def sort_words(words):
    return sorted(words, key=lambda word: len(word))

# a) Find length of every word
print("Length of words =", word_lengths(words))

# b) Extract words having more than five characters
print("Words having more than five characters =",
      long_words(words))

# c) Sort words according to their length
print("Words sorted by length =", sort_words(words))








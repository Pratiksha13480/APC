# 1. Write a function factorial(n) that accepts an integer and returns its factorial.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

n = int(input("Enter number: "))
print("Factorial =", factorial(n))

# 2. Write a function check_even_odd(n) that determines whether a given number is even or odd.
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter number: "))
print(check_even_odd(n))

# 3. Define a function that accepts two numbers and returns the greater number.
def greater(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Greater number =", greater(a, b))

# 4. Create a function simple_interest(p, r, t) to calculate simple interest.
def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
print("Simple Interest =", simple_interest(p, r, t))

# 5. Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter number: "))
print(is_prime(n))

# 6. Define a function to calculate the area of a circle using its radius.
def area_circle(radius):
    return 3.14 * radius * radius

radius = float(input("Enter radius: "))
print("Area of Circle =", area_circle(radius))

# 7. Write a function that accepts n and returns the sum of the first n natural numbers.
def natural_sum(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter n: "))
print("Sum =", natural_sum(n))

# 8. Create a function power(base, exponent) to calculate base raised to exponent.
def power(base, exponent):
    return base ** exponent

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Result =", power(base, exponent))

# 9. Write a function that accepts a list of numbers and returns the largest element without using max().
def largest(numbers):
    large = numbers[0]

    for num in numbers:
        if num > large:
            large = num

    return large

numbers = list(map(int, input("Enter numbers: ").split()))
print("Largest =", largest(numbers))

# 10. Define a function that accepts a string and returns the number of vowels present in it.
def count_vowels(s):
    count = 0

    for ch in s.lower():
        if ch in "aeiou":
            count = count + 1

    return count

s = input("Enter string: ")
print("Number of vowels =", count_vowels(s))

# 11. Write a function that accepts a string and returns its reverse.
def reverse_string(s):
    return s[::-1]

s = input("Enter string: ")
print("Reverse =", reverse_string(s))

# 12. Create a function that checks whether a given string or number is a palindrome.
def palindrome(value):
    value = str(value)

    if value == value[::-1]:
        return True
    else:
        return False

value = input("Enter string or number: ")
print(palindrome(value)) 

# 13. Write a function that accepts a list of numbers and returns their average.
def average(numbers):
    return sum(numbers) / len(numbers)

numbers = list(map(int, input("Enter numbers: ").split()))
print("Average =", average(numbers))

# 14. Define a function that accepts a list and an element and returns the number of times that element occurs.
def count_occurrence(lst, element):
    count = 0

    for x in lst:
        if x == element:
            count = count + 1

    return count

lst = list(map(int, input("Enter list elements: ").split()))
element = int(input("Enter element: "))
print("Occurrences =", count_occurrence(lst, element))

# 15. Write a function that accepts a list and returns a new list containing only unique elements.
def unique_elements(lst):
    result = []

    for x in lst:
        if x not in result:
            result.append(x)

    return result

lst = list(map(int, input("Enter elements: ").split()))
print("Unique elements =", unique_elements(lst))

# 16. Create a function to find the second-largest number in a list.
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()

    return unique[-2]

lst = list(map(int, input("Enter numbers: ").split()))

if len(set(lst)) < 2:
    print("Second largest does not exist")
else:
    print("Second largest =", second_largest(lst))

# 17. Write a function that accepts n and returns the first mn Fibonacci numbers.
def fibonacci(n):
    result = []
    a = 0
    b = 1

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

n = int(input("Enter n: "))
print("Fibonacci =", fibonacci(n))

# 18. Create a function that accepts marks in five subjects and returns percentage and grade.
def percentage_grade(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

marks = []

for i in range(5):
    marks.append(float(input("Enter marks: ")))

percentage, grade = percentage_grade(marks)
print("Percentage =", percentage)
print("Grade =", grade)

# 19. Write a function that accepts units consumed and calculates electricity bill according to slabs.
def electricity_bill(units):
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = 100 * 1.5 + (units - 100) * 2.5
    elif units <= 500:
        bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    else:
        bill = (100 * 1.5 + 100 * 2.5 +
                300 * 4 + (units - 500) * 6)

    return bill

units = float(input("Enter units consumed: "))
print("Electricity Bill =", electricity_bill(units))

# 20. Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10

    gross = basic + hra + da

    return gross

basic = float(input("Enter basic salary: "))
print("Gross Salary =", gross_salary(basic))

# 21. Create a function that accepts item prices and quantities and returns total bill after discount.
def total_bill(prices, quantities, discount):
    total = 0

    for i in range(len(prices)):
        total = total + prices[i] * quantities[i]

    discount_amount = total * discount / 100

    return total - discount_amount

prices = list(map(float, input("Enter prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))
discount = float(input("Enter discount percentage: "))
print("Final Bill =", total_bill(prices, quantities, discount))

# 22. Write a function that accepts a list and returns minimum, maximum, sum and average.
def calculate(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0

    for num in numbers:
        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

        total = total + num

    avg = total / len(numbers)

    return minimum, maximum, total, avg

numbers = list(map(int, input("Enter numbers: ").split()))
minimum, maximum, total, avg = calculate(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Sum =", total)
print("Average =", avg)

# 23. Write a program using separate functions to process student records. Calculate total, percentage, grade,
#class average, highest scorer and lowest scorer.
def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return total_marks(marks) / 5

def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "F"


students = []
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = list(map(float, input("Enter 5 marks: ").split()))

    total = total_marks(marks)
    per = percentage(marks)
    gr = grade(per)

    students.append({
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": per,
        "grade": gr
    })

class_average = sum(s["percentage"] for s in students) / n
highest = max(students, key=lambda x: x["percentage"])
lowest = min(students, key=lambda x: x["percentage"])

for s in students:
    print("\nName:", s["name"])
    print("Roll:", s["roll"])
    print("Total:", s["total"])
    print("Percentage:", s["percentage"])
    print("Grade:", s["grade"])

print("\nClass Average =", class_average)
print("Highest Scorer =", highest["name"])
print("Lowest Scorer =", lowest["name"])

# 24. Create functions for deposit, withdrawal, balance enquiry and transaction history.
balance = 0
transactions = []

def deposit(amount):
    global balance

    balance = balance + amount
    transactions.append("Deposited: " + str(amount))
    print("Deposit successful")


def withdrawal(amount):
    global balance

    if amount > balance:
        print("Insufficient balance")
    else:
        balance = balance - amount
        transactions.append("Withdrawn: " + str(amount))
        print("Withdrawal successful")


def balance_enquiry():
    print("Balance =", balance)

def transaction_history():
    print("Transaction History:")

    for transaction in transactions:
        print(transaction)

while True:
    print("\n1. Deposit")
    print("2. Withdrawal")
    print("3. Balance Enquiry")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Enter amount: "))
        deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount: "))
        withdrawal(amount)

    elif choice == 3:
        balance_enquiry()

    elif choice == 4:
        transaction_history()

    elif choice == 5:
        break

    else:
        print("Invalid choice")

# 25. Create functions to add books, issue books, return books, search books and display available books.
#Maintain book availability using dictionaries.
books = {}
def add_book(book_id, title):
    books[book_id] = {
        "title": title,
        "available": True
    }
    print("Book added")

def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book issued")
    else:
        print("Book not available")

def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned")
    else:
        print("Book not found")

def search_book(title):
    for book in books.values():
        if book["title"].lower() == title.lower():
            print("Book found:", book["title"])
            return

    print("Book not found")

def display_available():
    print("Available Books:")

    for book in books.values():
        if book["available"]:
            print(book["title"])

add_book(1, "Python")
add_book(2, "Java")
add_book(3, "C++")

issue_book(1)
return_book(1)
search_book("Java")
display_available()

# 26. Develop a modular program using functions to calculate electricity bills using slabs, fixed charges, taxe and discounts.
def calculate_units_charge(units):
    if units <= 100:
        return units * 1.5
    elif units <= 200:
        return 100 * 1.5 + (units - 100) * 2.5
    elif units <= 500:
        return 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    else:
        return (100 * 1.5 + 100 * 2.5 +
                300 * 4 + (units - 500) * 6)
    
def fixed_charge():
    return 100

def calculate_tax(amount):
    return amount * 0.05

def calculate_discount(amount):
    if amount > 5000:
        return amount * 0.10
    return 0

def final_bill(units):
    charge = calculate_units_charge(units)
    fixed = fixed_charge()

    subtotal = charge + fixed
    tax = calculate_tax(subtotal)
    discount = calculate_discount(subtotal)

    return subtotal + tax - discount

units = float(input("Enter units: "))
print("Final Electricity Bill =", final_bill(units))

# 27. Create functions to calculate consultation, laboratory,medicine, room charges and final bill. Apply discount
# based on patient category.
def consultation_charges(amount):
    return amount

def laboratory_charges(amount):
    return amount

def medicine_charges(amount):
    return amount

def room_charges(amount):
    return amount

def final_hospital_bill(consultation, laboratory,
                        medicine, room, category):
    total = (consultation_charges(consultation) +
             laboratory_charges(laboratory) +
             medicine_charges(medicine) +
             room_charges(room))

    if category.lower() == "senior":
        discount = total * 0.20
    elif category.lower() == "child":
        discount = total * 0.10
    else:
        discount = 0

    return total - discount

c = float(input("Consultation charges: "))
l = float(input("Laboratory charges: "))
m = float(input("Medicine charges: "))
r = float(input("Room charges: "))
category = input("Patient category: ")

print("Final Bill =",
      final_hospital_bill(c, l, m, r, category))

# 28. Implement functions to add/remove products, calculatem subtotal, apply coupon discounts, calculate GST and
# generate final invoice.
products = {}
def add_product(name, price, quantity):
    products[name] = {
        "price": price,
        "quantity": quantity
    }

def remove_product(name):
    if name in products:
        del products[name]

def subtotal():
    total = 0

    for product in products.values():
        total = total + product["price"] * product["quantity"]

    return total

def coupon_discount(amount, coupon):
    if coupon == "SAVE10":
        return amount * 0.10
    elif coupon == "SAVE20":
        return amount * 0.20
    else:
        return 0

def calculate_gst(amount):
    return amount * 0.18

def generate_invoice(coupon):
    sub = subtotal()
    discount = coupon_discount(sub, coupon)
    taxable = sub - discount
    gst = calculate_gst(taxable)
    final = taxable + gst

    print("Subtotal =", sub)
    print("Discount =", discount)
    print("GST =", gst)
    print("Final Amount =", final)

add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)
generate_invoice("SAVE10")

# 29. Write a recursive function to search for an element in a sorted list using binary search.
def binary_search(arr, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)

    else:
        return binary_search(arr, mid + 1, high, key)

arr = list(map(int, input("Enter sorted list: ").split()))
key = int(input("Enter element to search: "))

result = binary_search(arr, 0, len(arr) - 1, key)

if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)

# 30. Convert a decimal number into binary using recursion without using Python's built-in conversion functions.
def decimal_to_binary(n):
    if n == 0:
        return ""

    return decimal_to_binary(n // 2) + str(n % 2)

n = int(input("Enter decimal number: "))
if n == 0:
    print("Binary = 0")
else:
    print("Binary =", decimal_to_binary(n))

# 31. Check whether a string is a palindrome using recursion.
def recursive_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return recursive_palindrome(s[1:-1])
s = input("Enter string: ")

if recursive_palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")

# 32. Create separate functions for addition, subtraction,multiplication and division. Pass these functions as
# arguments to another function called calculate().
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(operation, a, b):
    return operation(a, b)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", calculate(add, a, b))
print("Subtraction =", calculate(subtract, a, b))
print("Multiplication =", calculate(multiply, a, b))

if b != 0:
    print("Division =", calculate(divide, a, b))
else:
    print("Division not possible")



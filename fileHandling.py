# Q1. Write a Python program to create a file named student.txt 
# and write the student's name, roll number, branch, and semester into the file.

with open("student.txt", "w") as file:
    file.write("Name: Pratiksha\n")
    file.write("Roll No: 31\n")
    file.write("Branch: Computer Science Engineering\n")
    file.write("Semester: V\n")


# Q2. Write a program to open a text file and display its complete contents.

with open("student.txt", "r") as file:
    print(file.read())


# Q3. Write a program to append additional student information to an existing
# file without deleting its previous contents.

with open("student.txt", "a") as file:
    file.write("College: D.Y. Patil College of Engineering & Technology\n")


# Q4. Write a program to read a text file line by line and display each line separately.

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())


# Q5. Write a program to count and display the total number of lines present in a text file.

with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))


# Q6. Write a program to count the total number of words present in a text file.

with open("student.txt", "r") as file:
    text = file.read()

words = text.split()
print("Total words:", len(words))


# Q7. Write a program to count the total number of characters in a text file,
# including spaces.

with open("student.txt", "r") as file:
    text = file.read()

print("Total characters:", len(text))


# Q8. Write a program to read a text file and display its lines in reverse order.

with open("student.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.strip())


# Q9. Read a text file and count the number of vowels and consonants present in the file.

with open("student.txt", "r") as file:
    text = file.read().lower()

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


# Q10. Read a text file and calculate the number of alphabets, digits,
# spaces, and special characters.

with open("student.txt", "r") as file:
    text = file.read()

alphabets = digits = spaces = special = 0

for ch in text:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)


# Q11. Read a text file and find the longest word present in the file.

with open("student.txt", "r") as file:
    text = file.read()

words = text.split()
longest_word = max(words, key=len)

print("Longest word:", longest_word)


# Q12. Read a text file and count how many times each word occurs.
# Display the result using a dictionary.

with open("student.txt", "r") as file:
    text = file.read().lower()

words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)


# Q13. Accept a word from the user and search for it in a text file.
# Display the number of occurrences and the line numbers where it appears.

search_word = input("Enter word to search: ").lower()
count = 0
line_numbers = []

with open("student.txt", "r") as file:
    for line_no, line in enumerate(file, start=1):
        words = line.lower().split()
        line_count = words.count(search_word)

        if line_count > 0:
            count += line_count
            line_numbers.append(line_no)

print("Occurrences:", count)
print("Line numbers:", line_numbers)


# Q14. Read a text file and replace all occurrences of a specified word
# with another word. Save the modified text in the same file or a new file.

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open("student.txt", "r") as file:
    text = file.read()

text = text.replace(old_word, new_word)

with open("student_modified.txt", "w") as file:
    file.write(text)

print("Modified file created successfully.")


# Q15. Read a Python source file and create another file after removing
# single-line comments.

source_file = input("Enter Python source file name: ")
output_file = "without_comments.py"

with open(source_file, "r") as source:
    with open(output_file, "w") as output:
        for line in source:
            stripped = line.lstrip()
            if not stripped.startswith("#"):
                output.write(line)

print("File without single-line comments created.")


# Q16. Read a text file and create another file containing the same text in uppercase.

with open("student.txt", "r") as file:
    text = file.read()

with open("uppercase.txt", "w") as file:
    file.write(text.upper())

print("Uppercase file created.")


# Q17. Create a file containing student records in the format:
# RollNo,Name,Marks
# 101,Amit,85
# 102,Priya,92
# 103,Rahul,78
# Write a program to:
# Display all records.
# Find the student with the highest marks.
# Calculate average marks.
# Display students who scored more than 80.

with open("students.csv", "w") as file:
    file.write("RollNo,Name,Marks\n")
    file.write("101,Amit,85\n")
    file.write("102,Priya,92\n")
    file.write("103,Rahul,78\n")

students = []

with open("students.csv", "r") as file:
    next(file)
    for line in file:
        roll, name, marks = line.strip().split(",")
        students.append((roll, name, int(marks)))

print("All records:")
for student in students:
    print(student)

highest = max(students, key=lambda x: x[2])
print("Highest marks:", highest)

average = sum(s[2] for s in students) / len(students)
print("Average marks:", average)

print("Students scoring more than 80:")
for student in students:
    if student[2] > 80:
        print(student)


# Q18. Store employee ID, name, department, and salary in a file.
# Write functions to:
# Display all employees.
# Find the highest-paid employee.
# Calculate average salary.
# Display employees earning above a given salary.

with open("employees.csv", "w") as file:
    file.write("ID,Name,Department,Salary\n")
    file.write("1,Amit,IT,50000\n")
    file.write("2,Priya,HR,60000\n")
    file.write("3,Rahul,IT,75000\n")

def read_employees():
    employees = []
    with open("employees.csv", "r") as file:
        next(file)
        for line in file:
            emp_id, name, dept, salary = line.strip().split(",")
            employees.append((emp_id, name, dept, float(salary)))
    return employees

def display_employees():
    for employee in read_employees():
        print(employee)

def highest_paid():
    return max(read_employees(), key=lambda x: x[3])

def average_salary():
    employees = read_employees()
    return sum(e[3] for e in employees) / len(employees)

def above_salary(amount):
    return [e for e in read_employees() if e[3] > amount]

display_employees()
print("Highest paid:", highest_paid())
print("Average salary:", average_salary())
print("Employees above 55000:", above_salary(55000))


# Q19. Store student attendance records in a file. Calculate the attendance
# percentage and display students having attendance below 75%.

with open("attendance.csv", "w") as file:
    file.write("RollNo,Name,Present,Total\n")
    file.write("101,Amit,70,80\n")
    file.write("102,Priya,60,80\n")
    file.write("103,Rahul,55,80\n")

with open("attendance.csv", "r") as file:
    next(file)
    for line in file:
        roll, name, present, total = line.strip().split(",")
        percentage = int(present) / int(total) * 100
        print(name, "Attendance:", percentage, "%")

        if percentage < 75:
            print(name, "has attendance below 75%.")


# Q20. Store deposits and withdrawals in a file. Read the file and calculate:
# Total deposits, Total withdrawals, Final balance, Largest transaction.

with open("transactions.txt", "w") as file:
    file.write("D 5000\n")
    file.write("W 1000\n")
    file.write("D 3000\n")
    file.write("W 500\n")

total_deposits = 0
total_withdrawals = 0
transactions = []

with open("transactions.txt", "r") as file:
    for line in file:
        transaction_type, amount = line.split()
        amount = float(amount)
        transactions.append(amount)

        if transaction_type == "D":
            total_deposits += amount
        elif transaction_type == "W":
            total_withdrawals += amount

final_balance = total_deposits - total_withdrawals
largest_transaction = max(transactions)

print("Total deposits:", total_deposits)
print("Total withdrawals:", total_withdrawals)
print("Final balance:", final_balance)
print("Largest transaction:", largest_transaction)


# Q21. Maintain book records containing book ID, title, author, and availability status.
# Implement operations to:
# Add a book, Search for a book, Issue a book, Return a book, Display available books.

books = []

def add_book(book_id, title, author):
    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    })

def search_book(book_id):
    for book in books:
        if book["id"] == book_id:
            print(book)
            return
    print("Book not found.")

def issue_book(book_id):
    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                print("Book issued.")
            else:
                print("Book is already issued.")
            return
    print("Book not found.")

def return_book(book_id):
    for book in books:
        if book["id"] == book_id:
            book["available"] = True
            print("Book returned.")
            return
    print("Book not found.")

def display_available_books():
    for book in books:
        if book["available"]:
            print(book)

add_book(1, "Python Programming", "John")
add_book(2, "Data Structures", "Robert")

search_book(1)
issue_book(1)
return_book(1)
display_available_books()


# Q22. Read the contents of two text files and create a third file
# containing the contents of both files.

with open("file1.txt", "r") as f1:
    text1 = f1.read()

with open("file2.txt", "r") as f2:
    text2 = f2.read()

with open("file3.txt", "w") as f3:
    f3.write(text1)
    f3.write("\n")
    f3.write(text2)

print("Files merged successfully.")


# Q23. Write a program to compare two text files and display whether their
# contents are identical. If different, identify the first line where they differ.

with open("file1.txt", "r") as f1:
    lines1 = f1.readlines()

with open("file2.txt", "r") as f2:
    lines2 = f2.readlines()

if lines1 == lines2:
    print("Files are identical.")
else:
    print("Files are different.")

    min_length = min(len(lines1), len(lines2))
    found = False

    for i in range(min_length):
        if lines1[i] != lines2[i]:
            print("First different line:", i + 1)
            print("File 1:", lines1[i].strip())
            print("File 2:", lines2[i].strip())
            found = True
            break

    if not found:
        print("Difference is because one file has extra lines.")






# 1. Create a Python module calculator.py containing functions for addition, subtraction, multiplication, and division. Create another program that imports the module and performs calculations based on user input.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# 2. Create a module student.py containing functions to calculate total marks, percentage, and grade. Import the module into another Python program and generate a student's result.

def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / len(marks)

def grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 75:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    else:
        return "F"


# 3. Create a module number_utils.py containing functions to check whether a number is prime, palindrome, Armstrong, or perfect. Import the required functions into a main program.

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == n

def is_perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


# 4. Create a module string_utils.py containing functions to count vowels, reverse a string, check palindrome, count words, and remove spaces.

def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count

def reverse_string(text):
    return text[::-1]

def is_palindrome_string(text):
    return text == text[::-1]

def count_words(text):
    return len(text.split())

def remove_spaces(text):
    return text.replace(" ", "")


# 5. Create a module containing functions to calculate gross salary, deductions, and net salary for an employee.

def gross_salary(basic_salary, allowance):
    return basic_salary + allowance

def deductions(gross, deduction_rate):
    return gross * deduction_rate / 100

def net_salary(gross, deduction):
    return gross - deduction


# 6. Create a module containing recursive functions for factorial, Fibonacci series, sum of digits, and binary conversion. Import and use these functions from another program.

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_digits(n):
    if n == 0:
        return 0

    return (n % 10) + sum_digits(n // 10)

def binary(n):
    if n == 0:
        return "0"

    if n == 1:
        return "1"

    return binary(n // 2) + str(n % 2)


# 7. Create a package named mathutils containing: a) basic.py – arithmetic operations b) number.py – prime, Armstrong, palindrome functions c) statistics.py – mean, maximum, minimum Create a main program that imports functions from each module.
def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b

# mathutils/number.py
def prime(n):
    return n>1 and all(n%i for i in range(2,n))
def armstrong(n):
    s=str(n); return sum(int(x)**len(s) for x in s)==n
def palindrome(n):
    return str(n)==str(n)[::-1]

# mathutils/statistics.py
def mean(a): return sum(a)/len(a)
def maximum(a): return max(a)
def minimum(a): return min(a)

# main.py
from mathutils.basic import *
from mathutils.number import *
from mathutils.statistics import *
print(add(10,5),sub(10,5),mul(10,5),div(10,5))
print(prime(7),armstrong(153),palindrome(121))
print(mean([10,20,30]),maximum([10,20,30]),minimum([10,20,30]))


# 8. Create a package student containing: a) marks.py – total and percentage b) grade.py – grade calculation c) attendance.py – attendance eligibility Write a main program that uses all three modules to generate a student report.

# student/marks.py
def total(m): return sum(m)
def percentage(m): return sum(m)/len(m)

# student/grade.py
def grade(p):
    if p>=90:return "A"
    if p>=75:return "B"
    if p>=60:return "C"
    if p>=50:return "D"
    return "F"

# student/attendance.py
def eligible(a): return a>=75

# main.py
from student.marks import *
from student.grade import *
from student.attendance import *
m=[85,90,80,88,92]; p=percentage(m)
print(total(m),p,grade(p),eligible(82))


# 9. Develop a package banking containing: a) account.py – account creation and balance b) transaction.py – deposit and withdrawal c) loan.py – loan calculation Create a main program to use the package.

# banking/account.py
class Account:
    def __init__(self,no,name,balance):
        self.no=no; self.name=name; self.balance=balance

# banking/transaction.py
def deposit(a,x): a.balance+=x
def withdraw(a,x):
    if x<=a.balance:a.balance-=x

# banking/loan.py
def loan(p,r,t): return p+(p*r*t/100)

# main.py
from banking.account import Account
from banking.transaction import *
from banking.loan import loan
a=Account(101,"Pratiksha",10000)
deposit(a,5000); withdraw(a,2000)
print(a.balance,loan(50000,8,2))


# 10. Create a package texttools containing: a) cleaning.py – remove punctuation and extra spaces b) tokenization.py – tokenize text c) frequency.py – word-frequency analysis Create a main program to use the package.

# texttools/cleaning.py
import string
def clean(s): return " ".join(s.translate(str.maketrans("","",string.punctuation)).split())

# texttools/tokenization.py
def tokenize(s): return s.split()

# texttools/frequency.py
def frequency(a):
    d={}
    for x in a:d[x]=d.get(x,0)+1
    return d

# main.py
from texttools.cleaning import clean
from texttools.tokenization import tokenize
from texttools.frequency import frequency
s=clean("Python, is easy. Python is powerful!")
w=tokenize(s)
print(s,w,frequency(w))


# 11. Create the following directory structure: a) college_project/ b) main.py c) student/ d) __init__.py e) details.py f) marks.py g) faculty/ h) __init__.py i) details.py Write a program that imports functions from both packages and displays student and faculty information.

# student/details.py
def student_details(): print("Name: Pratiksha, Roll No: 31")

# student/marks.py
def marks(): print("Marks: 450, Percentage: 90%")

# faculty/details.py
def faculty_details(): print("Faculty: Dr. Patil, Department: CSE")

# main.py
from student.details import student_details
from student.marks import marks
from faculty.details import faculty_details
student_details(); marks(); faculty_details()


# 12. Create a directory structure for a library application with separate packages for: a) Books b) Members c) Transactions Each package should contain suitable modules and a main program should combine all functionality.

# books/book.py
def book(): print("Python Programming")

# members/member.py
def member(): print("Member: Pratiksha")

# transactions/transaction.py
def issue(): print("Book issued")

def return_book(): print("Book returned")

# main.py
from books.book import book
from members.member import member
from transactions.transaction import issue,return_book
book(); member(); issue(); return_book()


# 13. Create a directory named ecommerce containing packages for: a) Products b) Customers c) Orders d) Payments Each package should contain at least two modules.

# products/product.py
def product(): print("Laptop - 70000")

# products/category.py
def category(): print("Electronics")

# customers/customer.py
def customer(): print("Pratiksha")

# customers/address.py
def address(): print("Sangli")

# orders/order.py
def order(): print("Order created")

# orders/status.py
def status(): print("Confirmed")

# payments/payment.py
def payment(): print("Payment successful")

# payments/invoice.py
def invoice(): print("Invoice generated")

# main.py
from products.product import product
from products.category import category
from customers.customer import customer
from customers.address import address
from orders.order import order
from orders.status import status
from payments.payment import payment
from payments.invoice import invoice
product();category();customer();address();order();status();payment();invoice()


# 14. Create a project directory containing packages for: a) Patient management b) Doctor management c) Billing d) Medical records Implement simple functions in each module and access them from main.py.

# patient/patient.py
def patient(): print("Patient: Pratiksha")

# doctor/doctor.py
def doctor(): print("Doctor: Dr. Patil")

# billing/bill.py
def bill(): return 1500

# medical_records/record.py
def record(): print("Disease: Fever")

# main.py
from patient.patient import patient
from doctor.doctor import doctor
from billing.bill import bill
from medical_records.record import record
patient();doctor();print("Bill:",bill());record()
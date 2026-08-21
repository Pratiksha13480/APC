# 1.check whether a number is zero or non-zero
n = int(input("Enter a number: "))

if n == 0:
    print("The number is Zero.")
else:
    print("The number is Non-Zero.")

# 2.find the largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)

# 3. check whether a number is positive or negative
n = int(input("Enter a number: "))

if n > 0:
    print("Positive number")
elif n < 0:
    print("Negative number")
else:
    print("Zero")

# 4.check whether a character is a vowel or consonant
ch = input("Enter character: ")

if ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print("character is vowel")
else:
    print("character is constant")    

# 5.evaluate student performance
per = float(input("Enter percentage: "))

if per >= 90:
    print("Excellent performance")
elif per >= 80:
    print("Very Good performance")
elif per >= 70:
    print("Good performance")
elif per >= 60:
    print("Average performance")
else:
    print("Poor performance")

# 6.find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# 7.find the smallest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest number is:", a)
elif b <= a and b <= c:
    print("Smallest number is:", b)
else:
    print("Smallest number is:", c)

# 8.check whether a number is even or odd
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 9.check whether a year is a leap year
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


# 10. determine whether the driver is insured or not
married = input("Is the driver married? (yes/no): ")
gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if married.lower() == "yes":
    print("Driver is Insured")
elif married.lower() == "no":
    if gender.lower() == "male" and age > 30:
        print("Driver is Insured")
    elif gender.lower() == "female" and age > 25:
        print("Driver is Insured")
    else:
        print("Driver is Not Insured")

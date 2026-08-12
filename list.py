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
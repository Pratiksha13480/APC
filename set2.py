# 1.Write a Python program to create a set containing five integers and display all its elements.
numbers = {10, 23, 93, 36, 50}
for num in numbers:
    print(num)

# 2.Create a list containing duplicate values. Convert the list into a set and display the resulting set    
number = [12, 73, 74, 63]
ans = set(number)
print(number)

# 3.Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
fruits = {"Apple", "Mango", "Banana", "Orange", "Grapes"}
fruits.add("Pineapple")
fruits.add("Watermelon")
print(fruits)

# 4.Create a set of numbers and remove a specified number from the set.
numbers = {10, 20, 30, 40, 50}
num = int(input("Enter number to remove: "))
if num in numbers:
    numbers.remove(num)
    print("Updated set:", numbers)
else:
    print("Number not found")

# 5.Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
students = {"Pratiksha", "Vidyadhar", "Shivraj"}
name = input("Enter student name: ")
if name in students:
    print("Student exists")
else:
    print("Student does not exist")

# 6.Create a set of cities and determine the total number of cities using an appropriate function.
cities = {"Mumbai", "Dehli", "Kolhapur", "Sangli"}
print("total cities:", len(cities))

# 7.Create a set of programming languages and display each language using a for loop.
languages = {"Java", "C++" "Python", "JavaScript", "C"}
for language in languages:
    print(language)

# 8.Create a list containing duplicate numbers, use a set to remove the duplicates.
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_numbers = set(numbers)
print(unique_numbers)

# 9.Create two sets of integers and find their union.
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
result = set1.union(set2)
print("Union:", result)

# 10. Create two sets and find the elements common to both sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common = set1.intersection(set2)
print("Common elements:", common)

# 11.Create two sets and find:Elements present in the first set but not the second,Elements present in the second set but not the first 
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.symmetric_difference(set2)
print("Symmetric difference:", result)

# 1.Write a Python program to create a set containing five integers and display all its elements.
numbers = {10, 23, 93, 36, 50}
for num in numbers:
    print(num)

# 2.Create a list containing duplicate values. Convert the list into a set and display the resulting set    
number = [12, 73, 74, 63]
ans = set(number)
print(number)

# 3.Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
fruits = {"Apple", "Mango", "Banana", "Orange", "Grapes"}
fruits.add("Pineapple")
fruits.add("Watermelon")
print(fruits)

# 4.Create a set of numbers and remove a specified number from the set.
numbers = {10, 20, 30, 40, 50}
num = int(input("Enter number to remove: "))
if num in numbers:
    numbers.remove(num)
    print("Updated set:", numbers)
else:
    print("Number not found")

# 5.Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
students = {"Pratiksha", "Vidyadhar", "Shivraj"}
name = input("Enter student name: ")
if name in students:
    print("Student exists")
else:
    print("Student does not exist")

# 6.Create a set of cities and determine the total number of cities using an appropriate function.
cities = {"Mumbai", "Dehli", "Kolhapur", "Sangli"}
print("total cities:", len(cities))

# 7.Create a set of programming languages and display each language using a for loop.
languages = {"Java", "C++" "Python", "JavaScript", "C"}
for language in languages:
    print(language)

# 8.Create a list containing duplicate numbers, use a set to remove the duplicates.
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_numbers = set(numbers)
print(unique_numbers)

# 9.Create two sets of integers and find their union.
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
result = set1.union(set2)
print("Union:", result)

# 10. Create two sets and find the elements common to both sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common = set1.intersection(set2)
print("Common elements:", common)

# 11.Create two sets and find:Elements present in the first set but not the second,Elements present in the second set but not the first 
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.symmetric_difference(set2)
print("Symmetric difference:", result)

# 12.Create two sets of numbers and find the elements that are present in either set but not in both.
set1 = {3, 8, 5, 9, 2}
set2 = {8, 6, 8, 3, 1}
result = set1.symmetric_difference(set2)
print(result)

# 14 Create two sets and determine whether the first set is a superset of the second set.
set1 = {1, 2, 3, 5, 6}
set2 = {2, 3, 4, 1, 7}
if set1.issuperset(set2):
    print("first set is a superset of second set")
else:
    print("first set is a not superset of second set")    
# 14 Create two sets and determine whether the first set is a superset of the second set.
set1 = {1, 2, 3, 5, 6}
set2 = {2, 3, 4, 1, 7}
if set1.issuperset(set2):
    print("first set is a superset of second set")
else:
    print("first set is a not superset of second set")    

# 15 Write a program to determine whether two sets have no elements in common
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 5, 6, 7}
if set1.isdisjoint(set2):
    print("two set have common element")
else:
    print("two set have not common element")    
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
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.symmetric_difference(set2)
print("Symmetric difference:", result)

# 13.Create two sets and determine whether the first set is a subset of the second set.
set1 = {1, 2}
set2 = {1, 2, 3, 4}
if set1.issubset(set2):
    print("first set is subset of second set")
else:
    print("First set is not a subset of second set")

# 14.Create two sets and determine whether the first set is a superset of the second set.
set1 = {1, 2, 3, 4}
set2 = {1, 2}
if set1.issuperset(set2):
    print("First set is a superset of second set")
else:
    print("First set is not a superset of second set")

# 15.Write a program to determine whether two sets have no elements in common.
set1 = {1, 2, 3}
set2 = {4, 5, 6}

if set1.isdisjoint(set2):
    print("Sets have no elements in common")
else:
    print("Sets have common elements")

# 16.Create two sets and check whether they are equal.
set1 = {1, 2, 3, 4}
set2 = {4, 3, 2, 1}

if set1 == set2:
    print("Sets are equal")
else:
    print("Sets are not equal")

# 17.create two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.
student1 = {"Python", "Java", "DBMS", "OS"}
student2 = {"Java", "Python", "CN", "Maths"}
common = student1.intersection(student2)
print("Subjects studied by both:", common)

# 18.Accept a sentence from the user and use a set to display all unique words.
sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print("Unique words:", unique_words)

# 19.Create two sets:Students present in the morning session,Students present in the afternoon session 
# Find:Students present in both sessions,Students present only in the morning,Students present only in the afternoon
# Students present in at least one session
morning = {"Amit", "Rahul", "Sneha", "Pooja"}
afternoon = {"Rahul", "Pooja", "Kiran", "Neha"}
print("Both sessions:", morning & afternoon)
print("Only morning:", morning - afternoon)
print("Only afternoon:", afternoon - morning)
print("At least one session:", morning | afternoon)

# 20.Create sets representing students enrolled in:Python, Java 
python_students = {"Amit", "Rahul", "Sneha", "Pooja"}
java_students = {"Rahul", "Pooja", "Kiran", "Neha"}

print("Python students:", python_students)
print("Java students:", java_students)

# 21.Find students enrolled in both courses and students enrolled in only one course.
python_students = {"Amit", "Rahul", "Sneha", "Pooja"}
java_students = {"Rahul", "Pooja", "Kiran", "Neha"}
both = python_students & java_students
only_one = python_students ^ java_students

print("Students in both courses:", both)
print("Students in only one course:", only_one)

# 22 .Create two sets representing technical skills of two employees. Find:Common skills ,
# Skills unique to Employee 1, Skills unique to Employee 2 
#All available skills
employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Java", "Python", "React", "Docker"}
print("Common skills:", employee1 & employee2)
print("Unique to Employee 1:", employee1 - employee2)
print("Unique to Employee 2:", employee2 - employee1)
print("All skills:", employee1 | employee2)

# 23.Create a set containing available books and another set containing requested books. 
# Determine which requested books are available.
available_books = {
    "Python Programming",
    "Java Programming",
    "Data Structures",
    "DBMS"
}
requested_books = {
    "Python Programming",
    "DBMS",
    "Operating Systems"
}
available_requested = available_books & requested_books
print("Requested books that are available:")
print(available_requested)

# 24.Store visitor IDs from two different days in separate sets. Determine:Unique visitors across both days 
#Returning visitors,Visitors who came only on the first day,Visitors who came only on the second day
#Create sets representing products belonging to different categories. Find products that belong to both categories.
day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Only first day:", day1 - day2)
print("Only second day:", day2 - day1)

# 25. Represent the friends of two users using sets. Find:Mutual friends ,Friends unique to User 1 
# Friends unique to User 2 ,Total unique friends
user1 = {"Amit", "Rahul", "Sneha", "Pooja", "Kiran"}
user2 = {"Rahul", "Pooja", "Neha", "Kiran", "Rohit"}

print("Mutual friends:", user1 & user2)
print("Friends unique to User 1:", user1 - user2)
print("Friends unique to User 2:", user2 - user1)
print("Total unique friends:", len(user1 | user2))









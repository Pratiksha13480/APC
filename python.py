#1: Read the contents from a file and display on console 
f = open("sample.txt", "w")
f.write("Python program")
f.close()

f = open("sample.txt", "r")
data = f.read()
print("file content: ", data)



#2 Read contents from one file and write into another file
f = open("sample.txt", "w")
f.write("Hi")
f.close()

f = open("sample.txt", "r")
data = f.read()
f.close()

f = open("destination.txt", "w")
f.write(data)
f.close()

f = open("destination.txt", "r")
print("copy content: ", f.read())
f.close()



#3 program to demonstrating 10 functions for handling directory
import os
# get current directory
print("current directory: ", os.getcwd())  

# create directory
#os.mkdir("MyFolder")
# Create directory if it does not exist
if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("MyFolder created")
else:
    print("MyFolder already exists")

# change directoey
os.chdir("MyFolder")
# get current directory
print("changed directory: ", os.getcwd())
# create another directory
os.mkdir("Test")
#list directory content
print("content: ", os.listdir())
#rename directory
os.rename("Test", "NewTest")
#check directory exists
print("exist: ", os.path.exists("NewTest"))
# it is directory
print("it id directory: ", os.path.isdir("NewTest"))
# remove directory
os.rmdir("NewTest")
print("directory removed")



# NOTE - install matplotlib library => python -m pip install matplotlib
# 4 Python program to display a horizontal bar chart of the popularity of programming Languages. Sample data: 
# Programming languages: Java, Python, PHP, JavaScript, C#, C++ Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
import matplotlib.pyplot as plt

language = ["Java", "C++", "Python"]
popularity = [22.2, 17.6, 8.8]

plt.barh(language, popularity)

plt.xlabel("Popularity")
plt.ylabel("Language")

plt.title("Popularity of Programming Languages")

plt.show()

#RUN Directly => python -c "import matplotlib.pyplot as plt; plt.barh(['Java','C++','Python'],[22.2,17.6,8.8]); plt.show()"


#5. Python program to create a pie chart.
import matplotlib.pyplot as plt

language = ["Java", "c++", "python"]
popularity = [50, 40, 30]

plt.pie(popularity, labels = language)
plt.title("Programming Language Popularity")
plt.show()


#6.program for designing a GUI using Tkinter
import tkinter as tk

#create window
root = tk.Tk()

root.title("My first GUI")
root.geometry("300x200")

#Add label
label = tk.Label(root, text="Welcome to Python")
label.pack()

#Add button
button = tk.Button(root, text="Click me")
button.pack()

#run application
root.mainloop()


# 7.program for class, object and constructor using suitable data
class Student:
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo

    def Display(self):
        print("name:",self.name)
        print("roll no:",self.rollNo)
s = Student("piya", 54)
s.Display()    



#8.program for Method overloading
class Addition:
    def add(self, a, b, c=0):
        return a+b+c

obj = Addition()
print("add 2 number:", obj.add(10, 20))
print("add 3 number:", obj.add(10, 20, 10))



#9.program for Method overriding
class Parent:
    def show(self):
        print("this is parent class")

class Child(Parent):
    def show(self):
        print("this is child class")

c = Child()
c.show()

# Method 2
class Person:
    def info(self, name):
        self.name = name
        print("name:", self.name)

class Student:
    def info(self, rollNo):
        self.rollNo = rollNo
        print("roll:", self.rollNo)

s = Student()
s.info(90)


# #10. program for Single inheritance
class Parent:
    def show(self):
        print("this is parent")
class Child(Parent):
    def Display(self):
        print("child")
c = Child()
c.show()
c.Display()

#Method 2
class Parent:
    def __init__(self,name):
        self.name = name

class Child(Parent):
    def __init__(self, name, rollNo):
        super().__init__(name)
        self.rollNo = rollNo
        
    def Display(self):
        print(self.name, self.rollNo)

c = Child("siya", 53)
c.Display()


#11. program for multilevel inheritance
class GrandFather:
    def show1(self):
        print("GrandFather")

class Father(GrandFather):
    def show2(self):
        print("Father")

class Son(Father):
    def show3(self):
        print("son")

c = Son()
c.show1()
c.show2()
c.show3()

#Method 2
class GrandFather:
    def __init__(self, name):
        self.name = name

class Father(GrandFather):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Son(Father):
    def __init__(self, name, age,rollNo):
        super().__init__(name,age)
        self.rollNo = rollNo

    def Display(self):
        print(self.name, self.age, self.rollNo)

c = Son("piya", 23, 43)
c.Display()

#12. program for multiple inheritance
class Father:
    def Display1(self):
        print("this is father")

class Mather:
    def Display2(self):
        print("this is Mather")

class Son(Father, Mather):
    def Display3(self):
        print("chold")

c = Son()
c.Display1()
c.Display2()
c.Display3()

# Method 2
class Father:
    def __init__(self, name):
        self.name = name

class Mother:
    def __init__(self, age):
        self.age = age

class Son(Father, Mother):
    def __init__(self, name, age, rollNo):
        Father.__init__(self, name)
        Mother.__init__(self, age)
        self.rollNo = rollNo

    def Display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.rollNo)

c = Son("piya", 32, 54)
c.Display()

    
#13. program for Hybrid inheritance
class A:
    def show(self):
        print("class A")
class B(A):
    def show2(self):
        print("class B")
class C(A):
    def show3(self):
        print("class c")
class D(B, C):
    def show4(self):
        print("class D")

d = D()
d.show()
d.show2()
d.show3()
d.show4()


#14. program for Hierarchical inheritance
class Parent:
    def Display(self):
        print("parent")
class Child1(Parent):
    def Display2(self):
        print("child 1")
class Child2(Parent):
    def Display3(self):
        print("child 2")
c1 = Child1()
c2 = Child2()
c1.Display()
c1.Display2()

c2.Display()
c2.Display3()


#15.program for demonstrating any 10 functions of Array
import array

a = array.array('i', [10, 20, 30, 40])

# 1. append()
a.append(50)
print("Append:", a)

# 2. insert()
a.insert(1, 15)
print("Insert:", a)

# 3. remove()
a.remove(30)
print("Remove:", a)

# 4. pop()
a.pop()
print("Pop:", a)

# 5. index()
print("Index:", a.index(20))

# 6. count()
print("Count:", a.count(10))

# 7. reverse()
a.reverse()
print("Reverse:", a)

# 8. tolist()
print("List:", a.tolist())

# 9. buffer_info()
print("Buffer Info:", a.buffer_info())

# 10. itemsize
print("Item Size:", a.itemsize)

#16.program for demonstrating any 10 functions of list
import array
a = [10, 20, 30, 40]

# 1. append()
a.append(50)
print("Append:", a)

# 2. insert()
a.insert(1, 15)
print("Insert:", a)

# 3. extend()
a.extend([60, 70])
print("Extend:", a)

# 4. remove()
a.remove(30)
print("Remove:", a)

# 5. pop()
a.pop()
print("Pop:", a)

# 6. index()
print("Index:", a.index(20))

# 7. count()
print("Count:", a.count(10))

# 8. sort()
a.sort()
print("Sort:", a)

# 9. reverse()
a.reverse()
print("Reverse:", a)

# 10. copy()
b = array.array('i',a)
print("Copy:", b)



#17.program for demonstrating any 10 functions of dictionary
Student = {"name":"piya", "age":23}

# 1.keys()
print("keys:", Student.keys())
# 2.values()
print("values:", Student.values())

# 3.items()
print("items:",Student.items())

# 4.get
print("get:",Student.get("name"))

# 5.update()
Student.update({"age":21})
print("update:",Student)

#6.pop()
Student.pop("age")
print("pop:", Student)

#7.setdefault()
Student.setdefault("city","Sangli")
print("setdefault:", Student)

# 8. copy()
newDict = Student.copy()
print("newDict:", newDict)

# 9.fromkeys()
d = dict.fromkeys(["a","b"], 0)
print("fromkey:", d)

# 10. clear()
Student.clear()
print("clear:", Student)


#18.program for demonstrating any 10 functions of string
s = "python programming"

#upper
print("upper:", s.upper())

#lower
print("lower:", s.lower)

#capitalize
print("capitalize:", s.capitalize())

#title
print("title:", s.title())

#len
print("length:", len(s))

#replace
print("replace:", s.replace("python", "java"))

#find
print("fond:", s.find("programming"))

#count
print("count:", s.count("p"))

#startwith
print("start with:", s.startswith("python"))

#endwith
print("end with:", s.endswith("ing"))


#19.program for demonstrating any 10 functions of tuple
t = (10,20,30,40,50)

#len()
print("length:", len(t))

#max()
print("max:", max(t))

#min()
print("min:", min(t))

#sum()
print("sum:", sum(t))

#count()
print("count:",t.count(20))

#index()
print("index:", t.index(10))

#sorted()
print("sorted:", sorted(t))

#any()
print("any:", any(t))

#all()
print("all:", all(t))

#tuple()
a = [60,70,80]
print("tuple:", tuple(a))


#20.program for demonstrating any 10 functions of set
s = {10,20,30,40,50}

#add()
s.add(60)
print("add:", s)

#update()
s.update([60,70])
print("update:", s)

#remove()
s.remove(20)
print("remove:",s)

#discard()
s.discard(70)
print("discard:",s)

#pop()
s.pop()
print("pop:",s)

#copy()
b = s.copy()
print("copy:", b)

#union()
a = {1,2,3}
b = {3,4,5}
print("union:", a.union(b))

#intersection
print("intersection:", a.intersection(b))

#difference()
print("difference:", a.difference(b))

#clear()
s.clear()
print("clear:",s)


#21. program for creating function and lambda function
#normal function
def add(a,b):
    return a+b
print("addition:", add(10,30))

#lambda function
square = lambda x: x * x
print("square using lambda:", square(5))



#22.program for Creating a new package for addition and multiplication operation and use it in another program.
from mymath import add, multiply

a = 10
b = 5

print("Addition:", add(a, b))
print("Multiplication:", multiply(a, b))

# NOTE => python -m pip install nltk
#23.program for applying the stemming operation using NLTK
import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()

words = ["playing", "play", "played", "running"]

print("original word:")
for word in words:
    print(word, "->", ps.stem(word))


#24.Write a program for tokenization using NLTK
import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer data if required
nltk.download('punkt_tab')
text = "python is an easy programming language"
tokens = word_tokenize(text, preserve_line=True)
print("original sentence:", text)
print("Token:", tokens)



#25. program for use of Numpy library
import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50])
print("array:", arr)

# Addition
print("addition:", arr + 5)

# Multiplication
print("multiplication:", arr * 2)

# Minimum
print("minimum:", np.min(arr))

# Maximum
print("maximum:", np.max(arr))

# Sum
print("sum:", np.sum(arr))

# Mean
print("mean:", np.mean(arr))

# Shape
print("shape:", arr.shape)

# Sort
b = np.array([20, 40, 10, 30])
print("sorted:", np.sort(b))

# Reshape
c = np.array([1, 2, 3, 4])
print("reshape:")
print(c.reshape(2, 2))


# NOTE => pip install pandas
#26. program using Pandas to read student records from a CSV file and display the contents in tabular format.

import pandas as pd

# Read CSV file
df = pd.read_csv("student.csv")

# Display student records
print("Student Records:")
print(df)


#27. Write a program for demonstrating abstract class and methods using python.
from abc import ABC, abstractmethod

#abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
#child class
class Rectangle(Shape):
    def area(self):
        l = 10
        b = 4
        print("area of reactangle:", l*b)

obj = Rectangle()
obj.area()


#28.Write a program for creating user-defined exception
# Create user-defined exception
class AgeError(Exception):
    pass


age = int(input("Enter your age: "))

try:
    if age < 18:
        raise AgeError("Age must be 18 or above")
    else:
        print("You are eligible")

except AgeError as e:
    print("Error:", e)



#29. Write a program for exception handling using python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))


    result = a / b

    print("Division:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter valid numbers")

finally:
    print("Program completed")


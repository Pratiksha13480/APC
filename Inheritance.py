# Inheritance
# 1. Create a class Employee with attributes emp_id, name, and salary. Create a derived class Manager that inherits from Employee and contains an 
# additional attribute department. Display all employee and manager details and calculate the manager's annual salary.
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.emp_id, self.name, self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)
        print("Annual Salary:", self.salary * 12)


m = Manager(101, "Pratiksha", 9000000, "IT")
m.display()

# 2. Create a base class Vehicle with attributes brand and model. Create a derived class Car with additional attributes fuel_type and price. Define methods to display vehicle details and calculate the discounted price of the car.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)


car = Car("Toyota", "Innova", "Petrol", 2000000)
car.display()
print("Discounted Price:", car.discounted_price(10))


# 3. Create two classes Academic and Sports. The Academic class should store marks obtained by a student, while the Sports class should store sports points. Create a class Student that inherits from both classes and calculates the student's overall performance.

class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student(Academic, Sports):
    def __init__(self, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)

    def performance(self):
        return sum(self.marks) + self.sports_points


s = Student([80, 85, 90], 20)
print("Overall Performance:", s.performance())


# 4. Create classes PersonalDetails and ProfessionalDetails. Store personal information such as name and age in the first class and employee ID, designation, and salary in the second class. Create an Employee class that inherits from both classes and displays complete employee information.

class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


e = Employee("Pratiksha", 20, 101, "Developer", 50000)
e.display()


# 5. Create a class Person containing name and age. Derive a class Student from Person with roll number and course. Further derive a class ResearchStudent from Student with research topic and guide name. Display all details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print(self.name, self.age, self.roll_no, self.course)
        print(self.topic, self.guide)


r = ResearchStudent("Pratiksha", 20, 31, "CSE", "AI", "Dr. Patil")
r.display()


# 6. Create a base class BankAccount with account number and balance. Derive SavingsAccount from it with an interest rate. Further derive PremiumSavingsAccount with additional benefits. Define methods to calculate interest and display account details.

class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)
        print("Interest:", self.calculate_interest())
        print("Benefits:", self.benefits)


p = PremiumSavingsAccount(12345, 100000, 7, "Free Insurance")
p.display()


# 7. Create a base class Shape containing a method to display the name of the shape. Create three derived classes Circle, Rectangle, and Triangle. Each class should implement its own method to calculate the area.

class Shape:
    def display(self):
        print("Shape")


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius


class Rectangle(Shape):
    def area(self, length, breadth):
        return length * breadth


class Triangle(Shape):
    def area(self, base, height):
        return 0.5 * base * height


print(Circle().area(5))
print(Rectangle().area(10, 5))
print(Triangle().area(10, 5))


# 8. Create a base class Employee containing employee ID, name, and basic salary. Create derived classes Manager, Developer, and Tester. Each derived class should calculate salary differently based on its respective allowances.

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class Manager(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.30


class Developer(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.20


class Tester(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.15


print("Manager Salary:", Manager(1, "A", 50000).salary())
print("Developer Salary:", Developer(2, "B", 50000).salary())
print("Tester Salary:", Tester(3, "C", 50000).salary())


# 9. Create a class Person. Derive Student and Faculty from Person. Create another class TeachingAssistant that inherits from both Student and Faculty. Display the details and demonstrate the use of multiple and hierarchical inheritance together.

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def student_details(self):
        print("Student:", self.name)


class Faculty(Person):
    def faculty_details(self):
        print("Faculty:", self.name)


class TeachingAssistant(Student, Faculty):
    def display(self):
        print("Teaching Assistant:", self.name)


ta = TeachingAssistant("Pratiksha")
ta.display()


# 10. Create a base class Vehicle. Derive Car and Bike from Vehicle. Create a class SportsCar that inherits from Car and another class ElectricBike that inherits from Bike. Add suitable attributes and methods to demonstrate a combination of inheritance types.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


class SportsCar(Car):
    def speed(self):
        print("Sports car is very fast")


class ElectricBike(Bike):
    def charge(self):
        print("Electric bike is charging")


sc = SportsCar("BMW")
sc.drive()
sc.speed()

eb = ElectricBike("Ola")
eb.ride()
eb.charge()


# 11. Create a base class Student with attributes roll_no, name, and course. Derive a class Result that stores marks in three subjects and calculates total marks, percentage, and grade.

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 3

    def grade(self):
        p = self.percentage()
        if p >= 90:
            return "A"
        elif p >= 75:
            return "B"
        elif p >= 60:
            return "C"
        else:
            return "D"


result = Result(31, "Pratiksha", "CSE", [85, 90, 80])
print(result.total())
print(result.percentage())
print(result.grade())


# 12. Create a class Product with product ID, name, and price. Derive ElectronicProduct with additional attributes such as brand and warranty. Calculate the final price after applying a discount.

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount):
        return self.price - self.price * discount / 100


product = ElectronicProduct(101, "Laptop", 70000, "HP", 2)
print("Final Price:", product.final_price(10))


# 13. Create classes Printer and Scanner with suitable methods for printing and scanning documents. Create a MultifunctionDevice class that inherits from both and supports both operations.

class Printer:
    def print_document(self):
        print("Printing document")


class Scanner:
    def scan_document(self):
        print("Scanning document")


class MultifunctionDevice(Printer, Scanner):
    pass


device = MultifunctionDevice()
device.print_document()
device.scan_document()


# 14. Create classes Camera and Phone. The Camera class should provide methods for taking photographs, while Phone should provide methods for making calls. Create a Smartphone class inheriting from both.

class Camera:
    def take_photo(self):
        print("Photograph taken")


class Phone:
    def make_call(self):
        print("Calling")


class Smartphone(Camera, Phone):
    pass


smartphone = Smartphone()
smartphone.take_photo()
smartphone.make_call()


# 15. Create a class Person with name and age. Derive Student with roll number and course. Further derive ResearchStudent with research topic and guide name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print(self.name, self.age, self.roll_no, self.course)
        print(self.topic, self.guide)


rs = ResearchStudent("Pratiksha", 20, 31, "CSE", "Machine Learning", "Dr. Patil")
rs.display()


# 16. Create a class Person with name and age. Derive Student with roll number and course. Further derive ResearchStudent with research topic and guide name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print(self.name, self.age, self.roll_no, self.course)
        print(self.topic, self.guide)


rs = ResearchStudent("Pratiksha", 20, 31, "CSE", "Artificial Intelligence", "Dr. Patil")
rs.display()


# 17. Create a base class Animal with common attributes and methods. Derive Dog, Cat, and Cow classes and implement their specific sounds and behaviors.

class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal:", self.name)


class Dog(Animal):
    def sound(self):
        print("Dog: Bark")


class Cat(Animal):
    def sound(self):
        print("Cat: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow: Moo")


Dog("Tommy").sound()
Cat("Kitty").sound()
Cow("Gauri").sound()


# 18. Create a class Person and derive Doctor and Patient. Create additional classes representing Surgeon and MedicalResearcher. Design the hierarchy so that the program demonstrates multiple inheritance along with hierarchical inheritance.

class Person:
    def __init__(self, name):
        self.name = name


class Doctor(Person):
    def doctor_work(self):
        print("Doctor treats patients")


class Patient(Person):
    def patient_work(self):
        print("Patient receives treatment")


class Surgeon(Doctor):
    def surgery(self):
        print("Surgeon performs surgery")


class MedicalResearcher(Doctor, Patient):
    def research(self):
        print("Medical researcher performs research")


s = Surgeon("Dr. Patil")
s.doctor_work()
s.surgery()

mr = MedicalResearcher("Dr. Sharma")
mr.doctor_work()
mr.patient_work()
mr.research()



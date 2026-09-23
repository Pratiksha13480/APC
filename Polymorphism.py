# Polymorphism

# 1. Create a base class Shape with a method area(). Derive Circle, Rectangle, and Triangle classes and override the area() method in each class. Create objects of each class and demonstrate runtime polymorphism.
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5


class Rectangle(Shape):
    def area(self):
        return 10 * 5


class Triangle(Shape):
    def area(self):
        return 0.5 * 10 * 5


shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    print(shape.area())

# 2. Create a base class Employee with a method calculate_salary(). Derive Manager, Developer, and Tester classes. Override the method in each class to calculate salary according to the employee's role.
class Employee:
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return 65000

class Developer(Employee):
    def calculate_salary(self):
        return 55000

class Tester(Employee):
    def calculate_salary(self):
        return 45000

employees = [Manager(), Developer(), Tester()]

for employee in employees:
    print(employee.calculate_salary())


# 3. Create a base class Vehicle with a method start(). Derive Car, Bike, and Bus classes and override start() to display the starting behavior of each vehicle.
class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with self-start")

class Bus(Vehicle):
    def start(self):
        print("Bus starts with ignition")

vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()


# 4. Create a base class Animal with a method sound(). Create subclasses Dog, Cat, Cow, and Lion. Override sound() in each class to display the appropriate sound.
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")

class Lion(Animal):
    def sound(self):
        print("Roar")

animals = [Dog(), Cat(), Cow(), Lion()]

for animal in animals:
    animal.sound()


# 5. Create a base class Notification with a method send(). Derive EmailNotification, SMSNotification, and PushNotification. Override send() to display the appropriate notification method.
class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Email notification sent")


class SMSNotification(Notification):
    def send(self):
        print("SMS notification sent")


class PushNotification(Notification):
    def send(self):
        print("Push notification sent")


notifications = [EmailNotification(), SMSNotification(), PushNotification()]

for notification in notifications:
    notification.send()


# 6. Create a base class Student with a method calculate_grade(). Derive EngineeringStudent, MedicalStudent, and ManagementStudent. Override the method according to different grading criteria.
class Student:
    def calculate_grade(self, marks):
        pass

class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        return "A" if marks >= 80 else "B"

class MedicalStudent(Student):
    def calculate_grade(self, marks):
        return "A" if marks >= 75 else "B"


class ManagementStudent(Student):
    def calculate_grade(self, marks):
        return "A" if marks >= 70 else "B"


students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

for student in students:
    print(student.calculate_grade(80))


# 7. Create a base class BankAccount with a method calculate_interest(). Derive SavingsAccount, CurrentAccount, and FixedDepositAccount. Override the method to calculate interest differently for each account type.

class BankAccount:
    def calculate_interest(self, balance):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.04


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.02


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.07


accounts = [SavingsAccount(), CurrentAccount(), FixedDepositAccount()]

for account in accounts:
    print(account.calculate_interest(100000))


# 8. Create a base class Report with a method generate(). Derive PDFReport, ExcelReport, and HTMLReport. Override generate() in each class. Write a function that accepts any report object and calls generate().

class Report:
    def generate(self):
        pass


class PDFReport(Report):
    def generate(self):
        print("PDF report generated")


class ExcelReport(Report):
    def generate(self):
        print("Excel report generated")


class HTMLReport(Report):
    def generate(self):
        print("HTML report generated")


def generate_report(report):
    report.generate()


generate_report(PDFReport())
generate_report(ExcelReport())
generate_report(HTMLReport())


# 9. Create a class Distance with feet and inches. Overload the + operator to add two distance objects and display the result in normalized form.

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        feet = self.feet + other.feet + total_inches // 12
        inches = total_inches % 12
        return Distance(feet, inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(3, 7)

d3 = d1 + d2
d3.display()


# 10. Create a class Student containing the student's name and total marks. Overload the > and < operators to compare the marks of two students.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student("Pratiksha", 450)
s2 = Student("Rahul", 400)

print(s1 > s2)
print(s1 < s2)


# 11. Create a class Product with product name and price. Overload the == and > operators to compare two products based on their prices.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Laptop", 70000)
p2 = Product("Mobile", 30000)

print(p1 == p2)
print(p1 > p2)


# 12. Develop an online shopping payment module using polymorphism. Create a base class Payment and derived classes UPIPayment, CardPayment, and WalletPayment. Each class should implement its own make_payment() method. Demonstrate polymorphism using a common function.

class Payment:
    def make_payment(self, amount):
        pass


class UPIPayment(Payment):
    def make_payment(self, amount):
        print("UPI payment:", amount)


class CardPayment(Payment):
    def make_payment(self, amount):
        print("Card payment:", amount)


class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Wallet payment:", amount)


def process_payment(payment, amount):
    payment.make_payment(amount)


process_payment(UPIPayment(), 1000)
process_payment(CardPayment(), 2000)
process_payment(WalletPayment(), 1500)


# 13. Create a base class Person with a method display_role(). Derive Student, Faculty, and Administrator. Override the method to display the respective role. Store all objects in a list and invoke the same method using a loop.

class Person:
    def display_role(self):
        pass


class Student(Person):
    def display_role(self):
        print("Student")


class Faculty(Person):
    def display_role(self):
        print("Faculty")


class Administrator(Person):
    def display_role(self):
        print("Administrator")


people = [Student(), Faculty(), Administrator()]

for person in people:
    person.display_role()


# 14. Create a base class Media with a method play(). Derive Audio, Video, and Podcast. Override play() according to the media type.

class Media:
    def play(self):
        pass


class Audio(Media):
    def play(self):
        print("Playing audio")


class Video(Media):
    def play(self):
        print("Playing video")


class Podcast(Media):
    def play(self):
        print("Playing podcast")


media = [Audio(), Video(), Podcast()]

for item in media:
    item.play()


# 15. Create a base class SmartDevice with methods turn_on() and turn_off(). Derive Light, Fan, AC, and TV. Override the methods according to each device.

class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(SmartDevice):
    def turn_on(self):
        print("Light turned on")

    def turn_off(self):
        print("Light turned off")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan turned on")

    def turn_off(self):
        print("Fan turned off")


class AC(SmartDevice):
    def turn_on(self):
        print("AC turned on")

    def turn_off(self):
        print("AC turned off")


class TV(SmartDevice):
    def turn_on(self):
        print("TV turned on")

    def turn_off(self):
        print("TV turned off")


devices = [Light(), Fan(), AC(), TV()]

for device in devices:
    device.turn_on()
    device.turn_off()



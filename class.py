# 1. Create a class Student with attributes such as roll_no, name, and marks. Create objects for multiple students and display their details and percentage.

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        percentage = sum(self.marks) / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage)


s1 = Student(1, "Pratiksha", [80, 85, 90, 75, 88])
s2 = Student(2, "Rahul", [70, 78, 82, 76, 80])

s1.display()
s2.display()


# 2. Create a class Employee with attributes emp_id, name, and basic_salary. Define methods to calculate HRA, DA, and gross salary.

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()


e = Employee(101, "Pratiksha", 30000)

print("Employee ID:", e.emp_id)
print("Name:", e.name)
print("HRA:", e.calculate_hra())
print("DA:", e.calculate_da())
print("Gross Salary:", e.gross_salary())


# 3. Create a class Rectangle with attributes length and breadth. Define methods to calculate area and perimeter.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r = Rectangle(10, 5)

print("Area:", r.area())
print("Perimeter:", r.perimeter())


# 4. Create a class Circle with an attribute radius. Define methods to calculate the area and circumference of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


c = Circle(7)

print("Area:", c.area())
print("Circumference:", c.circumference())


# 5. Create a class Book containing book_id, title, author, and price. Create objects for three books and display their information.

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


b1 = Book(101, "Python", "John", 500)
b2 = Book(102, "Java", "James", 600)
b3 = Book(103, "C++", "Bjarne", 550)

b1.display()
b2.display()
b3.display()


# 6. Create a class ElectricityBill containing consumer number, consumer name, and units consumed. Define a method to calculate the electricity bill according to different unit slabs.

class ElectricityBill:
    def __init__(self, consumer_number, consumer_name, units):
        self.consumer_number = consumer_number
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            return self.units * 1.5
        elif self.units <= 200:
            return 100 * 1.5 + (self.units - 100) * 2.5
        elif self.units <= 300:
            return 100 * 1.5 + 100 * 2.5 + (self.units - 200) * 4
        else:
            return 100 * 1.5 + 100 * 2.5 + 100 * 4 + (self.units - 300) * 5

    def display(self):
        print("Consumer Number:", self.consumer_number)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", self.calculate_bill())


bill = ElectricityBill(1001, "Pratiksha", 250)
bill.display()


# 7. Create a class MobilePhone with attributes brand, model, storage, and price. Define methods to display specifications and calculate the price after discount.

class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specifications(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def price_after_discount(self, discount):
        return self.price - (self.price * discount / 100)


phone = MobilePhone("Redmi", "Note 13", "128GB", 15000)

phone.display_specifications()
print("Price after discount:", phone.price_after_discount(10))


# 8. Create a class Patient containing patient ID, name, age, disease, and consultation fee. Define methods to display patient information and calculate the total bill.

class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)

    def total_bill(self, medicine_charge):
        return self.consultation_fee + medicine_charge


p = Patient(101, "Pratiksha", 20, "Fever", 500)

p.display()
print("Total Bill:", p.total_bill(1000))


# 9. Design an ATM class that allows a user to:
# a) Check balance
# b) Deposit money
# c) Withdraw money
# d) Display account details
# Create an object of the class and implement the operations through a menu-driven program.

class ATM:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def account_details(self):
        print("Account Number:", self.account_number)
        print("Name:", self.name)
        print("Balance:", self.balance)


atm = ATM(12345, "Pratiksha", 10000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == 4:
        atm.account_details()
    elif choice == 5:
        break
    else:
        print("Invalid choice.")


# 10. Create a class Vehicle containing vehicle number, model, rental rate, and availability. Implement methods to rent and return a vehicle and calculate rental charges based on the number of days.

class Vehicle:
    def __init__(self, vehicle_number, model, rental_rate, availability=True):
        self.vehicle_number = vehicle_number
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability

    def rent(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self):
        self.availability = True
        print("Vehicle returned successfully.")

    def rental_charges(self, days):
        return self.rental_rate * days


v = Vehicle("MH10AB1234", "Swift", 1500)

v.rent()
print("Rental Charges:", v.rental_charges(3))
v.return_vehicle()


# 11. Create a class ShoppingCart with customer name and cart ID. Initialize these values using a constructor. Implement methods to add products, remove products, and calculate the total bill. Use a destructor to display a message when the shopping cart object is destroyed.

class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = {}

    def add_product(self, name, price):
        self.products[name] = price

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]

    def total_bill(self):
        return sum(self.products.values())

    def __del__(self):
        print("Shopping cart object destroyed.")


cart = ShoppingCart("Pratiksha", 101)

cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 1000)

print("Total Bill:", cart.total_bill())

cart.remove_product("Mouse")

print("Total Bill:", cart.total_bill())

del cart


# 12. Create a class FoodOrder with order ID, customer name, food item, quantity, and price. Use a constructor to initialize the order. Define a method to calculate the total bill including tax. Implement a destructor to display an order completion message.

class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        amount = self.quantity * self.price
        tax = amount * 0.05
        return amount + tax

    def __del__(self):
        print("Order completed.")


order = FoodOrder(101, "Pratiksha", "Pizza", 2, 300)

print("Total Bill:", order.total_bill())

del order


# 13. Create a class StudentResult with student name and marks in five subjects. Use a constructor to initialize the details. Define methods to calculate total, percentage, and grade. Implement a destructor to display a suitable message.

class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def __del__(self):
        print("Student result object destroyed.")


student = StudentResult("Pratiksha", [85, 90, 80, 88, 92])

print("Name:", student.name)
print("Total:", student.total())
print("Percentage:", student.percentage())
print("Grade:", student.grade())

del student
# Abstraction

# 1. Create an abstract class Shape with an abstract method area(). Derive Circle, Rectangle, and Triangle classes and implement the area() method for each shape. Create objects of the derived classes and display their areas.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
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

print(Circle().area())
print(Rectangle().area())
print(Triangle().area())


# 2. Create an abstract class Vehicle with abstract methods start() and stop(). Derive Car, Bike, and Bus classes and implement these methods.
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")

class Bus(Vehicle):
    def start(self):
        print("Bus started")

    def stop(self):
        print("Bus stopped")

Car().start()
Car().stop()
Bike().start()
Bike().stop()
Bus().start()
Bus().stop()


# 3. Create an abstract class BankAccount with abstract methods deposit() and withdraw(). Derive SavingsAccount and CurrentAccount and implement the required operations
class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

class CurrentAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

account = SavingsAccount()
account.deposit(5000)
account.withdraw(1000)
print(account.balance)


# 4. Create an abstract class FoodOrder with abstract methods calculate_bill() and delivery_charge(). Derive RestaurantOrder and HomeDeliveryOrder and implement the methods appropriately.
class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass

class RestaurantOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 0

class HomeDeliveryOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 50


r = RestaurantOrder()
h = HomeDeliveryOrder()

print(r.calculate_bill() + r.delivery_charge())
print(h.calculate_bill() + h.delivery_charge())


# 5. Create an abstract class Patient with abstract methods calculate_bill() and treatment(). Derive InPatient, OutPatient, and EmergencyPatient classes and implement the methods according to the patient type.

class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        print("In-patient treatment")


class OutPatient(Patient):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        print("Out-patient treatment")


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        print("Emergency treatment")


patients = [InPatient(), OutPatient(), EmergencyPatient()]

for patient in patients:
    patient.treatment()
    print(patient.calculate_bill())


# 6. Create an abstract class Transport with an abstract method calculate_fare(distance). Implement subclasses:
# a) Bus
# b) Train
# c) Taxi
# d) Flight
# Calculate the fare according to the transportation type.

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 10


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 20


transports = [Bus(), Train(), Taxi(), Flight()]

for transport in transports:
    print(transport.calculate_fare(100))


# 7. Create an abstract class Question with an abstract method evaluate_answer(). Derive:
# a) MCQQuestion
# b) TrueFalseQuestion
# c) DescriptiveQuestion
# Implement answer evaluation for each question type.

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def evaluate_answer(self, answer):
        return answer == "B"


class TrueFalseQuestion(Question):
    def evaluate_answer(self, answer):
        return answer == "True"


class DescriptiveQuestion(Question):
    def evaluate_answer(self, answer):
        return len(answer) > 10


questions = [
    MCQQuestion(),
    TrueFalseQuestion(),
    DescriptiveQuestion()
]

print(questions[0].evaluate_answer("B"))
print(questions[1].evaluate_answer("True"))
print(questions[2].evaluate_answer("Python is easy"))


# 8. Create an abstract class Authentication with an abstract method authenticate(). Implement the method using:
# a) Password authentication
# b) OTP authentication
# c) Biometric authentication
# Demonstrate abstraction by interacting with objects through the abstract interface.

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Password authentication successful")


class OTPAuthentication(Authentication):
    def authenticate(self):
        print("OTP authentication successful")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Biometric authentication successful")


authentications = [
    PasswordAuthentication(),
    OTPAuthentication(),
    BiometricAuthentication()
]

for authentication in authentications:
    authentication.authenticate()


# 9. Create an abstract class CloudStorage with abstract methods:
# a) upload_file()
# b) download_file()
# c) delete_file()
# Create subclasses representing different storage services and implement the operations.

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to Google Drive")

    def download_file(self):
        print("File downloaded from Google Drive")

    def delete_file(self):
        print("File deleted from Google Drive")


class OneDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to OneDrive")

    def download_file(self):
        print("File downloaded from OneDrive")

    def delete_file(self):
        print("File deleted from OneDrive")


storage = [GoogleDrive(), OneDrive()]

for service in storage:
    service.upload_file()
    service.download_file()
    service.delete_file()


# Create an abstract class Appointment with abstract methods book_appointment() and calculate_fee(). Derive GeneralAppointment, SpecialistAppointment, and EmergencyAppointm

class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked")

    def calculate_fee(self):
        return 500


class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked")

    def calculate_fee(self):
        return 1000


class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment booked")

    def calculate_fee(self):
        return 2000


appointments = [
    GeneralAppointment(),
    SpecialistAppointment(),
    EmergencyAppointment()
]

for appointment in appointments:
    appointment.book_appointment()
    print(appointment.calculate_fee())
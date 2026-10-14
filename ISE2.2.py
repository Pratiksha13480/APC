class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, empId, salary):
        super().__init__(name, age)
        self.empId = empId
        self.salary = salary

    def Display(self):
        return super().Display()
        
 
        
    

e = Employee("piya", 22, 101, 700000)
print("name: ", e.name)
print("age: ", e.age)
print("employee id: ", e.empId)
print("salary: ", e.salary)

    

 
    
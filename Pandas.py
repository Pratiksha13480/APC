# 1. Create a dictionary containing Student ID, Student Name, Python Marks,
# DBMS Marks, and Mathematics Marks for 5 students. Convert it into a
# Pandas DataFrame, display the DataFrame, calculate total and average marks,
# and display students whose average marks are more than 75%.

import pandas as pd

students = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan"],
    "Python": [85, 78, 92, 70, 88],
    "DBMS": [80, 82, 90, 75, 85],
    "Mathematics": [90, 76, 88, 72, 91]
}

df = pd.DataFrame(students)

print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df["Total"] / 3

print("Total and Average Marks:")
print(df)

print("Students with average marks more than 75:")
print(df[df["Average"] > 75])


# 2. Create a dictionary containing Employee ID, Employee Name, Department,
# Salary, and Experience. Convert it into a Pandas DataFrame and display
# employees with salary greater than ₹50,000, average salary, highest salary,
# and employee with the highest experience.

employees = {
    "Employee_ID": [1, 2, 3, 4, 5],
    "Employee_Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan"],
    "Department": ["CSE", "HR", "IT", "Finance", "CSE"],
    "Salary": [55000, 48000, 65000, 52000, 75000],
    "Experience": [3, 5, 7, 4, 9]
}

df = pd.DataFrame(employees)

print(df)

print("Employees with salary greater than ₹50,000:")
print(df[df["Salary"] > 50000])

print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())

print("Employee with highest experience:")
print(df.loc[df["Experience"].idxmax()])


# 3. Create a dictionary containing Product ID, Product Name, Category,
# Price, and Quantity. Convert it into a DataFrame, calculate Total Amount
# using Price × Quantity, and find the product having the highest total sales.

products = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 800, 1500, 12000, 15000],
    "Quantity": [2, 10, 5, 3, 4]
}

df = pd.DataFrame(products)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print(df)

print("Product with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])


# 4. Create a dictionary containing Patient ID, Patient Name, Age, Disease,
# and Medical Charges. Convert it into a DataFrame, display patients above
# 60 years, find average and maximum medical charges, and display patients
# whose medical charges are greater than ₹50,000.

patients = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Ravi", "Anita", "Suresh", "Meena", "Raj"],
    "Age": [65, 45, 72, 55, 68],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Diabetes"],
    "Medical_Charges": [60000, 25000, 85000, 35000, 55000]
}

df = pd.DataFrame(patients)

print(df)

print("Patients above 60 years:")
print(df[df["Age"] > 60])

print("Average Medical Charge:", df["Medical_Charges"].mean())
print("Maximum Medical Charge:", df["Medical_Charges"].max())

print("Patients with charges greater than ₹50,000:")
print(df[df["Medical_Charges"] > 50000])


# 5. Create a dictionary containing Order_ID, Customer, Product, Quantity,
# Price, and Discount. Create a DataFrame, calculate Final Amount using
# Quantity × Price − Discount, and display all orders, orders above ₹5,000,
# highest-value order, and average order value.

orders = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Priya", "Rahul", "Sneha", "Karan"],
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor", "Printer"],
    "Quantity": [1, 2, 3, 2, 1],
    "Price": [60000, 30000, 20000, 15000, 25000],
    "Discount": [2000, 1000, 1500, 500, 1000]
}

df = pd.DataFrame(orders)

df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All Orders:")
print(df)

print("Orders above ₹5,000:")
print(df[df["Final_Amount"] > 5000])

print("Highest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("Average Order Value:", df["Final_Amount"].mean())


# 6. Create a dictionary containing Student_ID, Name, Department,
# Total_Classes, and Classes_Attended. Create a DataFrame, calculate
# Attendance Percentage, and display students whose attendance is below 75%.

attendance = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan"],
    "Department": ["CSE", "IT", "CSE", "ECE", "IT"],
    "Total_Classes": [100, 100, 120, 90, 110],
    "Classes_Attended": [85, 70, 90, 60, 100]
}

df = pd.DataFrame(attendance)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print(df)

print("Students below 75% attendance:")
print(df[df["Attendance_Percentage"] < 75])


# 7. A retail shop maintains sales information in a dictionary containing
# Product_ID, Product_Name, Category, Price, and Quantity. Convert it into
# a DataFrame, add Total_Sales using Price × Quantity, display products with
# sales greater than ₹10,000, find the product with maximum sales, and calculate average sales.

sales = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "TV", "Printer", "Tablet"],
    "Category": ["Electronics", "Electronics", "Electronics", "Office", "Electronics"],
    "Price": [50000, 25000, 40000, 12000, 20000],
    "Quantity": [2, 3, 1, 4, 2]
}

df = pd.DataFrame(sales)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print(df)

print("Products with sales greater than ₹10,000:")
print(df[df["Total_Sales"] > 10000])

print("Product with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("Average Sales:", df["Total_Sales"].mean())


# 8. Create a Pandas Series using a dictionary where student names are keys
# and marks are values. Display the Series, marks of a particular student,
# maximum and minimum marks, average marks, and students who scored more than 75.

student_marks = {
    "Amit": 85,
    "Priya": 72,
    "Rahul": 90,
    "Sneha": 68,
    "Karan": 78
}

s = pd.Series(student_marks)

print(s)

print("Marks of Rahul:", s["Rahul"])
print("Maximum Marks:", s.max())
print("Minimum Marks:", s.min())
print("Average Marks:", s.mean())

print("Students scoring more than 75:")
print(s[s > 75])


# 9. Create a Pandas Series using a dictionary containing employee names
# and salaries. Display the Series, highest salary, lowest salary, average
# salary, and employees earning more than ₹50,000.

employee_salary = {
    "Amit": 55000,
    "Priya": 48000,
    "Rahul": 65000,
    "Sneha": 45000,
    "Karan": 75000
}

s = pd.Series(employee_salary)

print(s)

print("Highest Salary:", s.max())
print("Lowest Salary:", s.min())
print("Average Salary:", s.mean())

print("Employees earning more than ₹50,000:")
print(s[s > 50000])


# 10. Create a Pandas Series using a dictionary containing product names
# and prices. Display all products and prices, increase every price by 10%,
# find the most expensive product, and display products costing more than ₹1,000.

product_prices = {
    "Laptop": 50000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Printer": 15000
}

s = pd.Series(product_prices)

print(s)

s = s * 1.10

print("Prices after 10% increase:")
print(s)

print("Most expensive product:")
print(s.idxmax(), s.max())

print("Products costing more than ₹1,000:")
print(s[s > 1000])


# 11. Create a Pandas Series using a dictionary where patient IDs are the
# index and patient ages are the values. Find average age, oldest patient,
# youngest patient, and patients above 60 years.

patient_age = {
    101: 65,
    102: 45,
    103: 72,
    104: 55,
    105: 68
}

s = pd.Series(patient_age)

print(s)

print("Average Age:", s.mean())

print("Oldest Patient:")
print(s.idxmax(), s.max())

print("Youngest Patient:")
print(s.idxmin(), s.min())

print("Patients above 60 years:")
print(s[s > 60])


# 12. Create a Pandas Series using a dictionary containing student names
# and attendance percentages. Find average attendance, students below 75%,
# students above 90%, and highest attendance.

student_attendance = {
    "Amit": 85,
    "Priya": 72,
    "Rahul": 95,
    "Sneha": 68,
    "Karan": 92
}

s = pd.Series(student_attendance)

print(s)

print("Average Attendance:", s.mean())

print("Students below 75%:")
print(s[s < 75])

print("Students above 90%:")
print(s[s > 90])

print("Highest Attendance:", s.max())


# 13. Read students.csv using Pandas, display the first and last 5 records,
# calculate total and average marks, display students with average marks greater
# than 75, find the student with the highest average, and find average marks for each subject.

df = pd.read_csv("students.csv")

print("First 5 records:")
print(df.head())

print("Last 5 records:")
print(df.tail())

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("Total and Average:")
print(df)

print("Students with average greater than 75:")
print(df[df["Average"] > 75])

print("Student with highest average:")
print(df.loc[df["Average"].idxmax()])

print("Average Python Marks:", df["Python"].mean())
print("Average DBMS Marks:", df["DBMS"].mean())
print("Average Maths Marks:", df["Maths"].mean())


# 14. Read employees.csv using Pandas, display employees from the CSE department,
# find average salary, highest and lowest salary, display employees with salary
# greater than ₹50,000, and calculate department-wise average salary.

df = pd.read_csv("employees.csv")

print("CSE Department Employees:")
print(df[df["Department"] == "CSE"])

print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())

print("Employees with salary greater than ₹50,000:")
print(df[df["Salary"] > 50000])

print("Department-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())


# 15. Read patients.csv using Pandas, display patients above 60 years,
# calculate average medical expense, find the patient with the highest
# medical expense, count patients for each disease, and display patients
# whose medical expense exceeds ₹50,000.

df = pd.read_csv("patients.csv")

print("Patients above 60 years:")
print(df[df["Age"] > 60])

print("Average Medical Expense:")
print(df["Medical_Expense"].mean())

print("Patient with highest medical expense:")
print(df.loc[df["Medical_Expense"].idxmax()])

print("Patient count for each disease:")
print(df["Disease"].value_counts())

print("Patients with medical expense above ₹50,000:")
print(df[df["Medical_Expense"] > 50000])


# 16. Read weather.csv using Pandas, find maximum temperature, minimum
# temperature, average temperature, display records where temperature is
# above 35°C, and calculate city-wise average temperature.

df = pd.read_csv("weather.csv")

print("Maximum Temperature:", df["Temperature"].max())
print("Minimum Temperature:", df["Temperature"].min())
print("Average Temperature:", df["Temperature"].mean())

print("Records where temperature is above 35°C:")
print(df[df["Temperature"] > 35])

print("City-wise Average Temperature:")
print(df.groupby("City")["Temperature"].mean())
# 1. Write a Python program using NumPy to create a one-dimensional array
# containing 10 integers and display the array, its size, data type,
# and number of dimensions.

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", arr)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Dimensions:", arr.ndim)


# 2. Create two NumPy arrays of 5 integers each and perform and display
# addition, subtraction, multiplication, division, and modulus.

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


# 3. Create a NumPy array containing 10 numbers and find and display
# the maximum, minimum, sum, and average of the elements.

arr = np.array([12, 25, 7, 45, 30, 18, 50, 9, 35, 20])

print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))


# 4. Create a NumPy array of integers from 1 to 20 and use Boolean
# indexing to separate and display the even and odd numbers.

arr = np.arange(1, 21)

print("Even numbers:", arr[arr % 2 == 0])
print("Odd numbers:", arr[arr % 2 != 0])


# 5. Create a one-dimensional array containing numbers from 1 to 12
# and reshape it into a 2 × 6 matrix, 3 × 4 matrix, and 4 × 3 matrix.

arr = np.arange(1, 13)

print("2 x 6 Matrix:")
print(arr.reshape(2, 6))

print("3 x 4 Matrix:")
print(arr.reshape(3, 4))

print("4 x 3 Matrix:")
print(arr.reshape(4, 3))


# 6. Create two 3 × 3 NumPy matrices and perform matrix addition.

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix Addition:")
print(a + b)


# 7. Create two compatible matrices using NumPy and perform matrix
# multiplication using an appropriate NumPy function.

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print("Matrix Multiplication:")
print(np.matmul(a, b))


# 8. Create a 3 × 4 matrix and display its transpose.

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print("Transpose:")
print(a.T)


# 9. Create a 4 × 4 NumPy array and display the first row, last column,
# diagonal elements, and elements from the second and third rows.

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print("First Row:", a[0])
print("Last Column:", a[:, -1])
print("Diagonal Elements:", np.diag(a))
print("Second and Third Rows:")
print(a[1:3])


# 10. Create a 4 × 4 matrix and calculate the sum of each row
# and each column separately.

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print("Row Sums:", np.sum(a, axis=1))
print("Column Sums:", np.sum(a, axis=0))


# 11. Create a NumPy array containing numbers from 1 to 20 and use
# slicing to display the first 5 elements, last 5 elements,
# alternate elements, and elements in reverse order.

arr = np.arange(1, 21)

print("First 5 Elements:", arr[:5])
print("Last 5 Elements:", arr[-5:])
print("Alternate Elements:", arr[::2])
print("Reverse Order:", arr[::-1])


# 12. Create an array of 10 integers and replace all elements greater
# than 50 with 0 using NumPy Boolean indexing.

arr = np.array([10, 25, 55, 70, 30, 90, 45, 60, 15, 80])

arr[arr > 50] = 0

print(arr)


# 13. Create an unsorted NumPy array and display it in ascending
# and descending order.

arr = np.array([45, 12, 89, 23, 7, 56, 34, 90, 18])

print("Ascending Order:", np.sort(arr))
print("Descending Order:", np.sort(arr)[::-1])


# 14. Create an array containing duplicate values and find and display
# only the unique elements.

arr = np.array([10, 20, 10, 30, 40, 20, 50, 30])

print("Unique Elements:", np.unique(arr))


# 15. Create two NumPy arrays and concatenate them horizontally
# and vertically.

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Horizontal Concatenation:")
print(np.hstack((a, b)))

print("Vertical Concatenation:")
print(np.vstack((a, b)))


# 16. Store marks of 10 students in a NumPy array and calculate
# the highest marks, lowest marks, average marks, median,
# and standard deviation.

marks = np.array([78, 85, 92, 67, 88, 76, 95, 81, 70, 89])

print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))


# 17. Take marks of 20 students, calculate the class average,
# and display the marks of students who scored above the average.

marks = np.array([65, 78, 90, 55, 82,
                  74, 88, 92, 60, 71,
                  85, 95, 68, 77, 80,
                  59, 87, 91, 73, 84])

average = np.mean(marks)

print("Class Average:", average)
print("Marks Above Average:", marks[marks > average])


# 18. Write a Python program using NumPy to create a 3D array of shape
# (2, 3, 4) containing numbers from 1 to 24 and display the array,
# number of dimensions, shape, and size.

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Array:")
print(arr)
print("Number of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)


# 19. Create a 3D array of shape (2, 3, 4) and access the first element,
# last element, element at index [0,1,2], and element at index [1,2,3].

arr = np.arange(1, 25).reshape(2, 3, 4)

print("First Element:", arr[0, 0, 0])
print("Last Element:", arr[-1, -1, -1])
print("Element at [0,1,2]:", arr[0, 1, 2])
print("Element at [1,2,3]:", arr[1, 2, 3])


# 20. Create a (2, 3, 4) array and calculate the sum of all elements,
# sum of each layer, sum along rows, and sum along columns.

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Sum of All Elements:", np.sum(arr))
print("Sum of Each Layer:", np.sum(arr, axis=(1, 2)))
print("Sum Along Rows:", np.sum(arr, axis=2))
print("Sum Along Columns:", np.sum(arr, axis=1))


# 21. Create a 3D array of random integers between 1 and 100
# and replace all values greater than 50 with 0.

arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original Array:")
print(arr)

arr[arr > 50] = 0

print("After Replacement:")
print(arr)


# 22. Generate a random 3D array of shape (3, 4, 5) and calculate
# its mean, median, standard deviation, variance, minimum, and maximum.

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))


# 23. Create a 3D NumPy array of shape (2, 3, 4) containing numbers
# from 1 to 24, flatten the array into a one-dimensional array,
# and display both the original and flattened arrays.

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Original Array:")
print(arr)

print("Flattened Array:")
print(arr.flatten())


# 24. Create a 3D array containing integers from 1 to 27, flatten
# the array, and calculate the sum, average, maximum, and minimum.

arr = np.arange(1, 28).reshape(3, 3, 3)

flat = arr.flatten()

print("Flattened Array:", flat)
print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))


# 25. Create a random 3D NumPy array of shape (3, 4, 5), flatten it,
# and display only the elements that are greater than 50, even numbers,
# and less than the average value.

arr = np.random.randint(1, 101, size=(3, 4, 5))

flat = arr.flatten()
average = np.mean(flat)

print("Elements Greater Than 50:")
print(flat[flat > 50])

print("Even Numbers:")
print(flat[flat % 2 == 0])

print("Average:", average)

print("Elements Less Than Average:")
print(flat[flat < average])
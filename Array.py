from array import array

arr = array('i', [10, 20, 30, 40, 50])
print("Original array:", arr)

# 1. append()
arr.append(60)
print("append(90):", arr)

# 2. buffer_info()
print("buffer_info():", arr.buffer_info())

# 3. byteswap()
arr.byteswap()
print("byteswap():", arr)
arr.byteswap()  

# 4. count()
print("count(20):", arr.count(20))

# 5. extend()
arr.extend([70, 80])
print("extend([70, 80]):", arr)

# 6. frombytes()
arr2 = array('i')
arr2.frombytes(array('i', [90, 100]).tobytes())
print("frombytes():", arr2)

# 7. fromfile()
with open("numbers.bin", "wb") as f:
    array('i', [110, 120]).tofile(f)

arr3 = array('i')
with open("numbers.bin", "rb") as f:
    arr3.fromfile(f, 2)

print("fromfile():", arr3)

# 8. fromlist()
arr4 = array('i')
arr4.fromlist([130, 140, 150])
print("fromlist():", arr4)

# 9. fromunicode()
unicode_arr = array('u')
unicode_arr.fromunicode("Python")
print("fromunicode():", unicode_arr)

# 10. index()
print("index(40):", arr.index(40))

# 11. insert()
arr.insert(2, 25)
print("insert(2, 25):", arr)

# 12. pop()
value = arr.pop()
print("pop():", value)
print("Array after pop():", arr)

# 13. remove()
arr.remove(25)
print("remove(25):", arr)

# 14. reverse()
arr.reverse()
print("reverse():", arr)

# 15. tobytes()
byte_data = arr.tobytes()
print("tobytes():", byte_data)

# 16. tofile()
with open("array_output.bin", "wb") as f:
    arr.tofile(f)
print("tofile(): Data written to array_output.bin")

# 17. tolist()
list_data = arr.tolist()
print("tolist():", list_data)

# 18. tounicode()
print("tounicode():", unicode_arr.tounicode())
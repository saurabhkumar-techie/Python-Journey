# 1. Creating a Tuple
fruits = ("Apple", "Banana", "Mango", "Orange")

print("Fruits:", fruits)

print("\nAccessing Elements:")# 2. Accessing Tuple Elements

print(fruits[0])
print(fruits[1])
print(fruits[-1])

print("\nTuple Slicing:")# 3. Tuple Slicing

print(fruits[0:2])
print(fruits[:3])
print(fruits[2:])

print("\nTuple Length:")# 4. Tuple Length

print(len(fruits))

print("\nDifferent Data Types:")# 5. Tuple with Different Data Types

student = ("Saurabh", 19, 8.5, True)

print(student)

print("\nSingle Element Tuple:")# 6. Single Element Tuple

number = (10,)

print(number)
print(type(number))



print("\nTuple Packing:")# 7. Tuple Packing

name = "Saurabh"
age = 19
course = "BCA"

student_info = name, age, course

print(student_info)


print("\nTuple Unpacking:")# 8. Tuple Unpacking

student_info = ("Saurabh", 19, "BCA")

name, age, course = student_info

print("Name:", name)
print("Age:", age)
print("Course:", course)

print("\nCount:")# 9. Count

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))


print("\nIndex:")# 10. Find Index

print(numbers.index(20))

print("\nMembership:")# 11. Membership

print(20 in numbers)
print(50 in numbers)

print("\nLoop:")# 12. Loop Through Tuple

for fruit in fruits:
    print(fruit)

print("\nNested Tuple:")# 13. Nested Tuple

students = (
    ("Saurabh", 19),
    ("Rahul", 20),
    ("Aman", 18)
)

print(students)

print(students[0])
print(students[0][0])
print(students[0][1])

print("\nList to Tuple:")# 14. Convert List to Tuple

my_list = [1, 2, 3, 4, 5]

my_tuple = tuple(my_list)

print(my_tuple)

# 15. Convert Tuple to List
print("\nTuple to List:")

my_tuple = (1, 2, 3, 4, 5)

my_list = list(my_tuple)

print(my_list)

print("\nTuple Concatenation:")# 16. Tuple Concatenation

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)


# 17. Tuple Repetition
print("\nTuple Repetition:")

numbers = (1, 2, 3)

print(numbers * 2)


# 18. Important Note
# Tuples are immutable.
# This means their elements cannot be changed.

colors = ("Red", "Green", "Blue")

print("\nOriginal Tuple:", colors)

# colors[0] = "Yellow"
# The above line will give an error because tuples cannot be changed.
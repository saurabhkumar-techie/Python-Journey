# Python Day 15: Dictionaries practice

student = { # Creating a Dictionary
    "name": "Saurabh",
    "age": 19,
    "course": "BCA",
    "college": "MM(DU)"
}

print("Student Details:")
print(student)

print("\nAccessing Values:") # Accessing Values

print(student["name"])
print(student["age"])
print(student["course"])


print("\nUsing get():") # Using get()

print(student.get("name"))
print(student.get("marks"))
print(student.get("marks", 0))

print("\nAdding Items:") # Adding New Items

student["city"] = "Ambala"
student["year"] = 2

print(student)

print("\nUpdating Values:") # Updating Values

student["age"] = 20
student["course"] = "BCA Data Science"

print(student)


print("\nUsing update():") # Using update()

student.update({"age": 19, "city": "Haryana"})

print(student)

print("\nUsing pop():") # Removing Items Using pop()

removed_course = student.pop("course")

print("Removed Course:", removed_course)
print(student)


print("\nUsing popitem():") # Removing the Last Inserted Item

student.popitem()

print(student)

print("\nChecking Keys:") # Checking Keys

print("name" in student)
print("marks" in student)

print("\nDictionary Length:") # Dictionary Length

print(len(student))

print("\nDictionary Keys:") # Getting All Keys

print(student.keys())

print("\nDictionary Values:") # Getting All Values

print(student.values())

print("\nDictionary Items:") # Getting Key-Value Pairs

print(student.items())

print("\nLoop Through Keys:") # Loop Through Keys

for key in student:
    print(key)

print("\nLoop Through Values:") # Loop Through Values

for value in student.values():
    print(value)

print("\nLoop Through Items:") # Loop Through Keys and Values

for key, value in student.items():
    print(key, ":", value)

print("\nNested Dictionary:") # Nested Dictionary

students = {
    "student1": {
        "name": "Rahul",
        "age": 20
    },
    "student2": {
        "name": "Aman",
        "age": 19
    }
}

print(students)

print(students["student1"]["name"])
print(students["student2"]["age"])

print("\nDifferent Data Types:") # Dictionary with Different Data Types

data = {
    "name": "Saurabh",
    "age": 19,
    "marks": 85.5,
    "passed": True,
    "subjects": ["Python", "DBMS", "HTML"]
}

print(data)

print("\nCopy Dictionary:") #Copy a Dictionary

original = {"a": 1, "b": 2, "c": 3}

copied = original.copy()

print("Original:", original)
print("Copied:", copied)

print("\nUsing fromkeys():") # Create Dictionary Using fromkeys()

keys = ["name", "age", "course"]

new_student = dict.fromkeys(keys, "Not Set")

print(new_student)

print("\nUsing setdefault():") # Set Default Value

student_data = {"name": "Saurabh"}

student_data.setdefault("course", "BCA")
student_data.setdefault("name", "Rahul")

print(student_data)

print("\nUsing clear():") #Clear Dictionary

temporary = {"x": 10, "y": 20}

temporary.clear()

print(temporary)

print("\nCounting Subjects:") #Count Items in a Dictionary

subjects = {
    "subject1": "Python",
    "subject2": "DBMS",
    "subject3": "HTML",
    "subject4": "CSS"
}

print("Total Subjects:", len(subjects))

print("\nStudent Marks:") #Student Marks Example

marks = {
    "Python": 85,
    "DBMS": 78,
    "HTML": 90,
    "CSS": 82
}

for subject, score in marks.items():
    print(subject, ":", score)

total_marks = sum(marks.values())
average_marks = total_marks / len(marks)

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

print("\nCreate Your Profile:") # User Input Dictionary

name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")

profile = {
    "name": name,
    "age": age,
    "course": course
}

print("\nYour Profile:")

for key, value in profile.items():
    print(key.capitalize(), ":", value)
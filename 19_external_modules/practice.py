# Python Day 19: External Modules

# 1. Importing the math Module
import math

print("1. Math Module")

print("Square Root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Factorial:", math.factorial(5))
print("Ceiling:", math.ceil(4.2))
print("Floor:", math.floor(4.8))
print("Pi:", math.pi)


# 2. Using the random Module
import random

print("\n2. Random Module")

print("Random Number:", random.randint(1, 100))
print("Random Choice:", random.choice(["Python", "Java", "C++"]))

numbers = [10, 20, 30, 40, 50]

random.shuffle(numbers)
print("Shuffled List:", numbers)


# 3. Using the datetime Module
import datetime

print("\n3. Date and Time")

current_date = datetime.date.today()
current_time = datetime.datetime.now()

print("Today's Date:", current_date)
print("Current Date and Time:", current_time)


# 4. Using the calendar Module
import calendar

print("\n4. Calendar Module")

year = 2026
month = 10

print(calendar.month(year, month))
print("Leap Year:", calendar.isleap(year))


# 5. Using the os Module
import os

print("\n5. OS Module")

print("Current Directory:", os.getcwd())
print("Operating System:", os.name)

print("Files in Current Directory:")
print(os.listdir("."))


# 6. Using the sys Module
import sys

print("\n6. SYS Module")

print("Python Version:", sys.version)
print("Platform:", sys.platform)


# 7. Using the statistics Module
import statistics

print("\n7. Statistics Module")

marks = [70, 80, 90, 85, 75]

print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))
print("Maximum:", max(marks))
print("Minimum:", min(marks))


# 8. Using the collections Module
from collections import Counter

print("\n8. Collections Module")

fruits = ["Apple", "Banana", "Apple", "Mango", "Banana", "Apple"]

count = Counter(fruits)

print("Fruit Count:", count)
print("Apple Count:", count["Apple"])


# 9. Using the itertools Module
import itertools

print("\n9. Itertools Module")

numbers = [1, 2, 3]

result = list(itertools.permutations(numbers, 2))

print("Permutations:", result)


# 10. Using the time Module
import time

print("\n10. Time Module")

print("Starting...")
time.sleep(1)
print("One second completed!")


# 11. Creating Your Own Module
# Create another file named mymodule.py
# Put this function inside that file:
#
# def greet(name):
#     return f"Hello, {name}!"
#
# Then import it using:
# from mymodule import greet
# print(greet("Saurabh"))


# 12. Installing an External Library
# Example: requests
#
# Install it in the VS Code terminal:
# python -m pip install requests
#
# Then use it:
#
# import requests
#
# response = requests.get("https://example.com", timeout=10)
# print("Status Code:", response.status_code)
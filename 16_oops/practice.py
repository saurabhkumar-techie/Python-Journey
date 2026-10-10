# Python Day 16: Object-Oriented Programming (OOP)

class Student:  # Creating a Class and Object
    name = "Saurabh"
    course = "BCA"

    def show_details(self):
        print("Name:", self.name)
        print("Course:", self.course)

student1 = Student()

print("1. Class and Object:")
student1.show_details()

class Person: # Using Constructor (__init__)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("My age is", self.age)


person1 = Person("Saurabh", 19)
person2 = Person("Rahul", 20)

print("\n2. Constructor:")
person1.introduce()
person2.introduce()

class Mobile: #Instance Variables
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


mobile1 = Mobile("Samsung", 20000)
mobile2 = Mobile("Apple", 70000)

print("\n3. Instance Variables:")
print(mobile1.brand, mobile1.price)
print(mobile2.brand, mobile2.price)

class Calculator: #Instance Method
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()

print("\n4. Instance Methods:")
print("Addition:", calc.add(10, 5))
print("Multiplication:", calc.multiply(10, 5))

class Employee: #Class Variable
    company = "ABC Technologies"

    def __init__(self, name):
        self.name = name


emp1 = Employee("Aman")
emp2 = Employee("Rahul")

print("\n5. Class Variable:")
print(emp1.name, emp1.company)
print(emp2.name, emp2.company)

class Animal: #Inheritance
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog1 = Dog()

print("\n6. Inheritance:")
dog1.eat()
dog1.bark()

class Grandparent: #Multilevel Inheritance
    def house(self):
        print("Grandparent's house")


class Parent(Grandparent):
    def car(self):
        print("Parent's car")


class Child(Parent):
    def bike(self):
        print("Child's bike")


child1 = Child()

print("\n7. Multilevel Inheritance:")
child1.house()
child1.car()
child1.bike()

class Vehicle: #Method Overriding
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def start(self):
        print("Car is starting")


car1 = Car()

print("\n8. Method Overriding:")
car1.start()

class Cat: #Polymorphism
    def sound(self):
        print("Cat says Meow")


class Cow:
    def sound(self):
        print("Cow says Moo")


animals = [Cat(), Cow()]

print("\n9. Polymorphism:")

for animal in animals:
    animal.sound()

class BankAccount: #Encapsulation
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)
        else:
            print("Enter a valid amount")

    def get_balance(self):
        return self.__balance


account = BankAccount("Saurabh", 1000)

print("\n10. Encapsulation:")
print("Owner:", account.owner)
print("Balance:", account.get_balance())

account.deposit(500)

print("Updated Balance:", account.get_balance())

from abc import ABC, abstractmethod #Abstraction


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)

print("\n11. Abstraction:")
print("Rectangle Area:", rectangle.area())

class ParentClass: #Using super()
    def __init__(self, name):
        self.name = name


class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


child = ChildClass("Saurabh", 19)

print("\n12. Using super():")
child.display()

class School: #Class Method
    school_name = "ABC School"

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name


print("\n13. Class Method:")
print("Before:", School.school_name)

School.change_school("XYZ School")

print("After:", School.school_name)

class MathOperations: #Static Method
    @staticmethod
    def square(number):
        return number * number


print("\n14. Static Method:")
print("Square:", MathOperations.square(5))


# 15. Mini Project: Student Management
class StudentRecord:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


student = StudentRecord("Saurabh", 101, 85)

print("\n15. Student Management:")
student.display()
student.result()
# Classes-and-Objects
# Python OOP Basics: Simple Class & 4 Key Principles

This repository contains a straightforward introduction to Object-Oriented Programming (OOP) in Python. 
It includes:

- A simple class example with a full explanation
- The **4 Pillars of OOP** with clear definitions and Python code samples

---

## 🧱 Part 1: Simple Python Class with Full Explanation

--- 
python
class Car:
    # Class variable (shared across all objects)
    wheels = 4

    def __init__(self, brand, color):
        # Instance variables (unique to each object)
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")
| Component                  | Type               | Description                                 |
| -------------------------- | ------------------ | ------------------------------------------- |
| `class Car:`               | Class definition   | Creates a new class called `Car`            |
| `wheels`                   | Class variable     | Shared by all cars (every car has 4 wheels) |
| `__init__`                 | Constructor        | Initializes object with brand and color     |
| `self.brand`, `self.color` | Instance variables | Data stored **per object**                  |
| `self`                     | Reference          | Refers to the current object                |
| `drive()`                  | Method             | Function defined inside the class           |

my_car = Car("Toyota", "blue")
my_car.drive()   # Output: The blue Toyota is driving.

## 🧠 Part 2: The 4 Pillars of Object-Oriented Programming (OOP)
The 4 core concepts are:

Encapsulation

Inheritance

Polymorphism

Abstraction

Let’s look at each one with a short explanation and example.

🔐 1. Encapsulation
Definition: Wrapping data and code together, hiding internal details.

Done using private variables (_ or __)

Prevents outside access to sensitive data directly

Code Example:
python
Copy
Edit
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
Usage:
python
Copy
Edit
acc = BankAccount("John", 1000)
acc.deposit(500)
print(acc.get_balance())     # 1500
# print(acc.__balance)      ❌ Error: can't access private variable

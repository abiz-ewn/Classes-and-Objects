# Classes-and-Objects
# Python OOP Basics: Simple Class & 4 Key Principles

This repository contains a straightforward introduction to Object-Oriented Programming (OOP) in Python. It includes:

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


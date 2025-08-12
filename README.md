# Classes-and-Objects

This repository provides an introduction to **Object-Oriented Programming (OOP)** in Python. It includes a simple class example with a full explanation and dives into the **4 Pillars of OOP** with clear definitions and code samples.

---

## 🧱 Part 1: Simple Python Class Explained

```python
class Car:
    # Class variable (shared across all objects)
    wheels = 4

    def __init__(self, brand, color):
        # Instance variables (unique to each object)
        self.brand = brand
        self.color = color

    def drive(self):
        # Method to simulate driving
        print(f"The {self.color} {self.brand} is driving.")

# Creating an object (instance) of the Car class
my_car = Car("Toyota", "blue")
# Calling the drive method on the object
my_car.drive()                  # Output: The blue Toyota is driving.
```

| Component                  | Type               | Description                                 |
| -------------------------- | ------------------ | ------------------------------------------- |
| `class Car:`               | Class definition   | Creates a new class called `Car`.           |
| `wheels`                   | Class variable     | Shared by all `Car` objects.                |
| `__init__`                 | Constructor Method | Initializes a new object's state (attributes). |
| `self.brand`, `self.color` | Instance variables | Data unique to each specific object.        |
| `self`                     | Reference          | Refers to the current instance of the class. |
| `drive()`                  | Method             | A function defined inside the class.        |

## 🧠 Part 2: The 4 Pillars of Object-Oriented Programming (OOP)

The four core concepts of OOP are:

- **Encapsulation**
- **Inheritance**
- **Polymorphism**
- **Abstraction**

Let’s look at each one with a short explanation and a code example.

---

### 🔐 1. Encapsulation

**Definition:** Bundling data (attributes) and methods that operate on the data into a single unit (a class). It restricts direct access to some of an object's components, which is a way to prevent accidental modification of data.

- Achieved using private variables (e.g., `__balance`).
- Prevents outside code from directly accessing sensitive data.

**Code Example:**
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable prefixed with __

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount("John", 1000)
acc.deposit(500)

print(acc.get_balance())  # ✅ Correct way: 1500
# print(acc.__balance)    # ❌ Error: AttributeError, cannot access private variable directly
```

### 🧬 2. Inheritance
**Definition:** A mechanism where a new class (child/subclass) derives attributes and methods from an existing class (parent/superclass).

- Promotes code reusability.
- The child class can extend or override the functionality of the parent class.

**Code Example:**
```python
class Animal:
    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # This method overrides the parent's speak method
        print("Bark")

a = Animal()
a.speak()  # Output: Some generic animal sound

d = Dog()
d.speak()  # Output: Bark
```

### 🎭 3. Polymorphism
**Definition:** The ability of an object to take on many forms. In practice, it means that different classes can be treated through the same interface, and each class implements the interface in its own way.

- Allows a single method name to work differently for different classes.
- Often achieved via method overriding (as seen in Inheritance).

**Code Example:**
```python
class Bird:
    def fly(self):
        print("Bird flies high in the sky")

class Airplane:
    def fly(self):
        print("Airplane flies faster and higher")

def flying_test(thing_that_can_fly):
    thing_that_can_fly.fly()

b = Bird()
a = Airplane()

flying_test(b)  # Output: Bird flies high in the sky
flying_test(a)  # Output: Airplane flies faster and higher
```

### 🧩 4. Abstraction
**Definition:** Hiding complex implementation details and showing only the essential features of the object. It focuses on what an object does instead of how it does it.

- Often implemented in Python using abstract base classes (`ABC`).
- Forces subclasses to implement specific methods defined in the abstract class.

**Code Example:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract base class
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self): # Must implement the abstract 'area' method
        return self.side * self.side

sq = Square(5)
print(sq.area())  # Output: 25

# s = Shape()     # ❌ Error: Can't instantiate abstract class Shape

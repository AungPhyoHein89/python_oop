# 🐍 Python Object-Oriented Programming (OOP) Journey

Welcome to my Python OOP repository! This repository serves as a practical codebase for mastering **Object-Oriented Programming (OOP)** principles in Python, inspired by Harvard's CS50W curriculum.

Inside, you will find the evolution of data structures—moving from simple tuples and dictionaries to creating robust, custom data types using Classes and Objects.

---

## 🚀 What I Learned Today (Day-13 Reset)

### 1. The Evolution of Data Handling
Before diving into OOP, I explored how Python handles multi-value data and identified their limitations:
* **Tuples:** Great for returning multiple values, but **Immutable** (leads to `TypeError` when trying to assign values like `student[1] = "Ravenclaw"`).
* **Lists:** Mutable, but index-based access (`student[0]`) makes the code unreadable and prone to errors.
* **Dictionaries:** Key-value pairing is better, but spelling typos in string keys (e.g., `student["hose"]`) can silently break the system without compile-time errors.

### 2. Custom Data Types with `Class`
To solve the limitations above, I built a custom blueprint using Python Classes. 

```python
class Student:
    def __init__(self, name, house):
        self.name = name        # Instance Variable / Attribute
        self.house = house      # Instance Variable / Attribute

The Blueprint: The Class acts as a structural layout that does not consume object memory until instantiation.

The Magic of self: It acts as a dedicated variable group placeholder for the specific object that is about to be created.

Attributes vs. Instance Variables: * Instance Variables: The actual data fields inside the unique object (e.g., student_1.name).

Attributes: The general term for any variable/property bound to an object, accessed cleanly using the dot (.) notation.

🛠️ Code Architecture Evolution
Here is the finalized robust structure implementing the special __init__ constructor method:

Python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    if student.name == "Padma":
        student.house = "Ravenclaw"
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
📈 Next Up
[x] Class Initialization & Attributes (__init__, self)

[ ] Object Methods (Adding behavior to objects)

[ ] Data Validation (raise ValueError)

[ ] Advanced OOP Principles (Inheritance & Decorators)

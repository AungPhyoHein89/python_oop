"""
### Insecure Encapsulation OOP
class Student:
  def __init__(self, name, house):
    if not name:
      raise ValueError("Missing Name.")
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalide House.")
    self.name = name
    self.house = house

  def __str__(self):
    return f"{self.name} from {self.house}"

def main():
  student = get_student()
  student.house = "Number Four ..."
  print(student)

def get_student():
  name = input(f"Name: ")
  house = input(f"House: ")
  return Student(name, house)

if __name__ == "__main__":
  main()
"""
"""
class Student:
  def __init__(self, name, house):
    if not name:
      raise ValueError("Missing Name.")
    self.name = name
    self.house = house
  
  @property
  def house(self):
    return self._house
  
  @house.setter
  def house(self, house):
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalid House.")
    self._house = house

  def __str__(self):
    return f"{self.name} from {self.house}"
  

def main():
  try:
    student = get_student()
    print("\n--- Initial Student ---")
    print(student)

    print("\nTrying to change house to 'Number four...' ...")
    student.house = "Number four ..."

  except ValueError as e:
    print(f"❌ Caught an error: {e}")

def get_student():
  name = input(f"Name: ")
  house = input(f"House: ")
  return Student(name, house)

if __name__ == "__main__":
  main()
"""

class Student:
  def __init__(self, name, house):
    self.name = name
    self.house = house

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if not name:
      raise ValueError("Missing Name")
    self._name = name

  @property
  def house(self):
    return self._house
  
  @house.setter
  def house(self, house):
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invaild House.")
    self._house = house

  def __str__(self):
    return f"{self.name} from {self.house}"

def main():
  while True:
    try:  
      student = get_student()
      #student.house = "Number Four ..."
      print(student)
      break
    except ValueError as e:
      print(f"Error: {e}.Try Again\n")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  return Student(name, house)

if __name__ == "__main__":
  main()
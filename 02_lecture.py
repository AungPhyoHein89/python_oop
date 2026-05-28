"""import sys

class Student:
  def __init__(self, name, house):
    if not name :
      sys.exit("Missing Name")
    self.name = name
    self.house = house

def main():
  student = get_student()
  print(f"{student.name} from {student.house}")

def get_student():
  name = input(f"Name: ")
  house = input(f"House: ")
  return Student(name, house)

if __name__ == "__main__":
  main()
"""

class Student:
  def __init__(self, name, house):
    if not name:
      raise ValueError("Missing Name")
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalid House")
    self.name = name
    self.house = house

def main():
  student = get_student()
  print(f"{student.name} from {student.house}")

def get_student():
  while True:
    try:
      name = input(f"Name: ")
      house = input(f"House: ")
      return Student(name, house)
    except ValueError as e:
      print(f"❌ Error : {e}. Try Again!\n")
      continue
    
if __name__ == "__main__":
  main()

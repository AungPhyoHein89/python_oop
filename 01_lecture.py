#First 

# name = input(f"Name: ")
# house = input(f"House: ")

# print(f"{name} form {house}")

#Using Function

# def main():
#   name = get_name()
#   house = get_house()
#   print(f"{name} from {house}")

# def get_name():
#   return input(f"Name: ")
  

# def get_house():
#   return input(f"House: ")
  

# if __name__ == "__main__":
#   main()


# 3 return two (multi-value) values

# def main():
#   name, house = get_student()
#   print(f"{name} from {house}")

# def get_student():
#   name = input(f"Name: ")
#   house = input(f"House: ")
#   return name, house

# if __name__ == "__main__":
#   main()

# 4 return as tuple
# item assignment error in this example

# def main():
#   student = get_student()
#   if student[0] == "Padma": student[1] = "Ravenclaw"
#   print(f"{student[0]} from {student[1]}")

# def get_student():
#   name = input(f"Name: ")
#   house = input(f"House: ")
#   return (name, house)

# if __name__ == "__main__":
#   main()

# return list

# def main():
#   student = get_student()
#   if student[0] == "Padma":
#     student[1] = "Ravenclaw"
#   print(f"{student[0]} from {student[1]}")

# def get_student():
#   name = input(f"Name: ")
#   house = input(f"House: ")
#   return [name, house]

# if __name__ == "__main__":
#   main()

# return disctionary

# def main():
#   student = get_student()
#   if student["name"] == "Padma":
#     student["house"] = "Ravenclaw"
#   print(f"{student['name']} from {student['house']}")

# def get_student():
#   name = input(f"Name: ")
#   house = input(f"House: ")
#   return {"name": name, "house": house}

# if __name__ == "__main__":
#   main()

# return dictionary 2

# def main():
#   student = get_student()
#   if student["name"] == "Padma":
#     student["house"] = "Ravenclaw"
#   print(f"{student['name']} from {student['house']}")

# def get_student():
#   student = {}
#   student["name"] = input(f"Name: ")
#   student["house"] = input(f"House: ")
#   return student

# if __name__ == "__main__":
#   main()

### Return as Custom Data Type

# class Student:
#   ...

# def main():
#   student = get_student()
#   if student.name == "Padma":
#     student.house = "Ravenclaw"
#   print(f"{student.name} from {student.house}")

# def get_student():
#   student = Student()
#   student.name = input(f"Name: ")
#   student.house = input(f"House: ")
#   return student

# if __name__ == "__main__":
#   main()

### Create Student object by special __ method

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
  name = input(f"Name: ")
  house = input(f"House: ")
  return Student(name, house)

if __name__ == "__main__":
  main()
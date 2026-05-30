class Dashboard:
  def __init__(self, speed):
    self.speed = speed
  
  @property
  def speed(self):
    return self._speed
  
  @speed.setter
  def speed(self, speed):
    #if speed <= 0 or speed >= 180:
    if not (0 < speed <= 180):
      raise ValueError("Invalid Limit!")
    self._speed = speed
  
  def __str__(self):
    return f"Your car is running in {self.speed} km/hr"

def main():
  try:
    car = get_speed()
    print(car)
    
    print("\nTrying to change speed into Invalid Limit form another Programmer")
    car.speed = 900
    
  except ValueError as e:
    print(f"Speed Error: {e}")

def get_speed():
  speed = int(input("Speed: "))
  return Dashboard(speed)

if __name__ == "__main__":
  main()
class Phone:
  def __init__(self, battery_percent):
    self.battery_percent = battery_percent

  
  @property
  def battery_percent(self):
    return self._battery_percent
  
  @battery_percent.setter
  def battery_percent(self, battery_percent):
    if battery_percent < 0 or battery_percent > 100:
      raise ValueError("Invalid Battery Percent")  
    self._battery_percent = battery_percent
  
  def __str__(self):
    return f"Current Battery Percent: {self.battery_percent}%"

def main():
  try:
    iphone = get_battery_percent()
    #iphone.battery_percent = -20
    print("--- Phone Info ---")
    print(iphone)
  except ValueError as e:
    print(f"Error -> {e}")

def get_battery_percent():
  battery_percent = int(input("Battery Percent: "))
  return Phone(battery_percent)

if __name__ == "__main__":
  main()
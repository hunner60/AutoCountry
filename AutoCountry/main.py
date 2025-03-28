def display_menu():
  print("\n********************************")
  print(" AutoCountry Vehicle Finder v0.1 ")
  print("********************************")
  print("Please Enter the following number below from the following menu:\n")
  print("1. PRINT all Authorized Vehicles")
  print("2. Exit")

def main():
  while True:
      display_menu()
      choice = input("\nEnter your choice: ")

      if choice == "1":
          print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
          allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
          for vehicle in allowed_vehicles:
              print(vehicle)
      elif choice == "2":
          print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
          break
      else:
          print("\nInvalid choice, please enter 1 or 2.")

if __name__ == "__main__":
  main()

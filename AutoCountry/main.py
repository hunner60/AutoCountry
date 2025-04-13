# CarFinder v0.3 - AutoCountry Vehicle Finder

authorized_vehicles = [
    'Ford F-150',
    'Chevrolet Silverado',
    'Tesla CyberTruck',
    'Toyota Tundra',
    'Nissan Titan'
]

def display_menu():
    print("\n********************************")
    print(" AutoCountry Vehicle Finder v0.3 ")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nPlease enter your selection: ")

        if choice == "1":
            print("\nAuthorized Vehicles:")
            for vehicle in authorized_vehicles:
                print(vehicle)

        elif choice == "2":
            vehicle_name = input("Please Enter the full Vehicle name: ")
            if vehicle_name in authorized_vehicles:
                print(f"{vehicle_name} is an authorized vehicle")
            else:
                print(f"{vehicle_name} is not an authorized vehicle. If you received this in error, please check the spelling and try again.")

        elif choice == "3":
            new_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
            if new_vehicle not in authorized_vehicles:
                authorized_vehicles.append(new_vehicle)
                print(f'You have added "{new_vehicle}" as an authorized vehicle')
            else:
                print(f'"{new_vehicle}" is already an authorized vehicle.')

        elif choice == "4":
            print("Exiting AutoCountry Vehicle Finder. Goodbye!")
            break

        else:
            print("Invalid choice, please enter a valid option (1-4).")

if __name__ == "__main__":
    main()


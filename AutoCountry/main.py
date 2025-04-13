# CarFinder v0.3 - AutoCountry Vehicle Finder

authorizedVehiclesList = [ 
    'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500'
]

def display_menu():
    print("\n********************************")
    print(" AutoCountry Vehicle Finder v0.3 ")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nPlease enter your selection: ")

        if choice == "1":
            print("\nAuthorized Vehicles:")
            for vehicle in authorizedVehiclesList:
                print(vehicle)

        elif choice == "2":
            vehicle_name = input("Please Enter the full Vehicle name: ")
            if vehicle_name in authorizedVehiclesList:
                print(f"{vehicle_name} is an authorized vehicle")
            else:
                print(f"{vehicle_name} is not an authorized vehicle. If you received this in error, please check the spelling and try again.")

        elif choice == "3":
            new_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
            if new_vehicle not in authorizedVehiclesList:
                authorizedVehiclesList.append(new_vehicle)
                print(f'You have added "{new_vehicle}" as an authorized vehicle')
            else:
                print(f'"{new_vehicle}" is already an authorized vehicle.')

        elif choice == "4":
            vehicle_to_remove = input("Please enter the full Vehicle name you would like to REMOVE: ")
            if vehicle_to_remove in authorizedVehiclesList:
                confirmation = input(f"Are you sure you want to remove \"{vehicle_to_remove}\" from the Authorized Vehicles List? (yes/no): ").strip().lower()
                if confirmation == "yes":
                    authorizedVehiclesList.remove(vehicle_to_remove)
                    print(f'"{vehicle_to_remove}" has been removed from the authorized vehicles list.')
                else:
                    print(f'No changes made. "{vehicle_to_remove}" remains in the list.')
            else:
                print(f'"{vehicle_to_remove}" is not an authorized vehicle.')

        elif choice == "5":
            print("Exiting AutoCountry Vehicle Finder. Goodbye!")
            break

        else:
            print("Invalid choice, please enter a valid option (1-5).")

if __name__ == "__main__":
    main()

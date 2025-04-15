# CarFinder v0.4 - AutoCountry Vehicle Finder (Enhanced for File I/O)

import os

FILENAME = "authorized_vehicles.txt"

def load_vehicles():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w') as f:
            default_vehicles = [
                'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck',
                'Toyota Tundra', 'Rivian R1T', 'Ram 1500'
            ]
            f.write('\n'.join(default_vehicles))
    with open(FILENAME, 'r') as f:
        return [line.strip() for line in f.readlines()]

def save_vehicles(vehicle_list):
    with open(FILENAME, 'w') as f:
        f.write('\n'.join(vehicle_list))

def display_menu():
    print("\n********************************")
    print(" AutoCountry Vehicle Finder v0.4 ")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")

def main():
    while True:
        vehicle_list = load_vehicles()
        display_menu()
        choice = input("\nPlease enter your selection: ")

        if choice == "1":
            print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
            for vehicle in vehicle_list:
                print(vehicle)

        elif choice == "2":
            vehicle_name = input("Please Enter the full Vehicle name: ").strip()
            if vehicle_name in vehicle_list:
                print(f"{vehicle_name} is an authorized vehicle.")
            else:
                print(f"{vehicle_name} is not an authorized vehicle. If you received this in error, please check the spelling and try again.")

        elif choice == "3":
            new_vehicle = input("Please Enter the full Vehicle name you would like to add: ").strip()
            if new_vehicle not in vehicle_list:
                vehicle_list.append(new_vehicle)
                save_vehicles(vehicle_list)
                print(f'You have added "{new_vehicle}" as an authorized vehicle')
            else:
                print(f'"{new_vehicle}" is already an authorized vehicle.')

        elif choice == "4":
            vehicle_to_remove = input("Please enter the full Vehicle name you would like to REMOVE: ").strip()
            if vehicle_to_remove in vehicle_list:
                confirmation = input(f"Are you sure you want to remove \"{vehicle_to_remove}\" from the Authorized Vehicles List? (yes/no): ").strip().lower()
                if confirmation == "yes":
                    vehicle_list.remove(vehicle_to_remove)
                    save_vehicles(vehicle_list)
                    print(f'"{vehicle_to_remove}" has been removed from the authorized vehicles list.')
                else:
                    print(f'No changes made. "{vehicle_to_remove}" remains in the list.')
            else:
                print(f'"{vehicle_to_remove}" is not an authorized vehicle.')

        elif choice == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break

        else:
            print("Invalid choice, please enter a valid option (1-5).")

if __name__ == "__main__":
    main()

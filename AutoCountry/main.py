#Car Finder v0.5
import os

FILENAME = "authorized_vehicles.txt"
DEFAULT_VEHICLES = ["Toyota Camry", "Honda Accord", "Ford F-150"]

def load_vehicles():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w') as file:
            for vehicle in DEFAULT_VEHICLES:
                file.write(vehicle + '\n')
    with open(FILENAME, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_vehicles(vehicle_list):
    with open(FILENAME, 'w') as file:
        for vehicle in vehicle_list:
            file.write(vehicle + '\n')

def display_menu():
    print("\n=== Welcome to AutoCountry CarFinder ===")
    print("1. PRINT all vehicles")
    print("2. SEARCH for a vehicle")
    print("3. ADD a vehicle")
    print("4. DELETE a vehicle")
    print("5. Exit")

def print_vehicles(vehicle_list):
    print("\n--- Authorized Vehicles ---")
    for vehicle in vehicle_list:
        print(vehicle)

def search_vehicle(vehicle_list):
    name = input("Enter the vehicle name to search: ").strip()
    if name in vehicle_list:
        print(f"{name} is an authorized vehicle.")
    else:
        print(f"{name} is NOT an authorized vehicle.")

def add_vehicle(vehicle_list):
    name = input("Enter the vehicle name to add: ").strip()
    if name not in vehicle_list:
        vehicle_list.append(name)
        save_vehicles(vehicle_list)
        print(f"{name} has been added.")
    else:
        print(f"{name} already exists.")

def delete_vehicle(vehicle_list):
    name = input("Enter the vehicle name to delete: ").strip()
    if name in vehicle_list:
        confirm = input(f"Are you sure you want to delete {name}? (y/n): ").strip().lower()
        if confirm == 'y':
            vehicle_list.remove(name)
            save_vehicles(vehicle_list)
            print(f"{name} has been removed.")
        else:
            print("No changes made.")
    else:
        print(f"{name} not found in the list.")

def main():
    while True:
        vehicle_list = load_vehicles()
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            print_vehicles(vehicle_list)
        elif choice == "2":
            search_vehicle(vehicle_list)
        elif choice == "3":
            add_vehicle(vehicle_list)
        elif choice == "4":
            delete_vehicle(vehicle_list)
        elif choice == "5":
            print("Exiting CarFinder. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

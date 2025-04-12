def km_to_m(km):
    return km * 1000

def min_to_sec(minutes):
    return minutes * 60

def hr_to_min(hours):
    return hours * 60

def gram_to_kg(grams):
    return grams / 1000

def show_menu():
    print("\n--- Unit Conversion Calculator ---")
    print("1. Kilometer to Meter")
    print("2. Minute to Second")
    print("3. Hour to Minute")
    print("4. Gram to Kilogram")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            value = float(input("Enter kilometers: "))
            print(f"{value} km = {km_to_m(value)} meters")
        elif choice == '2':
            value = float(input("Enter minutes: "))
            print(f"{value} minutes = {min_to_sec(value)} seconds")
        elif choice == '3':
            value = float(input("Enter hours: "))
            print(f"{value} hours = {hr_to_min(value)} minutes")
        elif choice == '4':
            value = float(input("Enter grams: "))
            print(f"{value} grams = {gram_to_kg(value)} kilograms")
        elif choice == '5':
            print("Thanks for using the converter. Bye!")
            break
        else:
            print("Invalid option. Try again.")

main()

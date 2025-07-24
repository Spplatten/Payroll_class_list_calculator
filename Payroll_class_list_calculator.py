
class Employee:
    def __init__(self, name, hours_worked, hourly_rate, tax_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.tax_rate = tax_rate

    def calculate_pay(self):
        regular_hours = min(self.hours_worked, 40)
        overtime_hours = max(0, self.hours_worked - 40)
        regular_pay = regular_hours * self.hourly_rate
        overtime_pay = overtime_hours * self.hourly_rate * 1.5
        return regular_pay + overtime_pay

payroll = []

# Main loop
while True:
    print("\n Virtual Payroll")
    print("1. Add an employee")
    print("2. View payroll")
    print("3. Do Nothing")
    print("4. Remove an employee")
    print("5. Vertical Listing")
    print("6. Exit")
    
    choice = input("Choose an option (1-6): ")

    if choice == "1": 
        while True:
            name = input("Enter employee name (or type 'end' to finish): ")
            if name.lower() == 'end':
                break
            try:
                hours_worked = float(input(f"Enter hours worked for {name}: "))
                hourly_rate = float(input(f"Enter hourly rate for {name}: "))
                tax_rate = float(input(f"Enter tax rate for {name} (as a decimal): "))
                employee = Employee(name, hours_worked, hourly_rate, tax_rate)
                payroll.append(employee)
            except ValueError:
                print("Invalid input. Please enter numeric values for hours and rates.")
                continue
    elif choice == "2": # View Cars
        if payroll:
            print("Payroll Summary:")
            for emp in payroll:
                pay = emp.calculate_pay()
                print(f"{emp.name}: ${pay:.2f}")
        else:
            print(" Your payroll is empty.")
    elif choice == "3": # Start All Engines
            print("\nDoing nothing for now. Please choose another option.")
    elif choice == "4": # Remove Car
        if payroll:
            print("\nWhich employee would you like to remove?")
            for i, emp in enumerate(payroll, 1):
                print(f"{i}. {emp.name}")
            try:
                index = int(input("Enter the number of the employee to remove: "))
                if 1 <= index <= len(payroll):
                    removed_car = payroll.pop(index - 1)  # Remove or pop() the object from the list.
                    print(f"{removed_car.name} {removed_car.hours_worked} {removed_car.hourly_rate} has been removed from your garage.")
                else:
                    print("Invalid employee number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print(" Your garage is empty.")
    elif choice == "5": # Print vertical listing of garage
        for index, obj in enumerate(payroll):
            print(f"\nIndex {index}")
            for attr, value in obj.__dict__.items():  # Treat as a dictionary with attribute-value pairs.
                print(f"  {attr}: {value}")
    elif choice == "6": # Exit
        print("Sending checks out to employees. See you next week! ")
        break
    else:
        print("Invalid choice. Try again.")
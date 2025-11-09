# O'Tria Fee
# CIS261 
# Course Project Phase 1: Create and Call Functions with Parameters

# Functions to get the employee's name. End exits the loop.

def get_employee_name():
    return input("Enter employee name (or 'End' to finish):")

# Function to get totaled hours worked. Float to use decimals.

def get_hours_worked():
    return float(input("Enter hours worked:"))

# Function to get hourly pay rate

def get_hourly_rate():
    return float(input("Enter hourly rate:"))

# Function to get income tax rate
 
def get_tax_rate():
    return float(input("Enter income tax rate as a decimal (.08 = 8%):"))

# Function to calculate gross pay, income tax, and net pay

def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay*tax_rate
    net_pay = gross_pay- income_tax
    return gross_pay, income_tax, net_pay

# Function to display individual employee payroll info

def display_employee_info(name, hours, rate, gross, tax_rate, tax, net):
    print(f"\nEmployee: {name}")
    print(f"Hours Worked: {hours}")
    print(f"Hourly rate: ${rate:.2f}")   
    print(f"Gross Pay:${gross:.2f}")    
    print(f"Tax Rate: {tax_rate:.2%}")
    print(f"Income Tax: ${tax:.2f}")
    print(f"Net Pay: ${net:.2f}\n")

# Function to display totals after all employees are entered

def display_totals(count, total_hours, total_gross, total_tax, total_net):
    print(f"\nPayroll Summary")
    print(f"Total Employees: {count}")

    print(f"Total Hours Worked: {total_hours}")
    print(f"Total Gross Pay: ${total_gross:.2f}")
    print(f"Total income Tax: ${total_tax:.2f}")
    print(f"Total Net Pay: ${total_net:.2f}")

# Beginning totals

employee_count = 0
total_hours = 0
total_gross = 0
total_tax= 0
total_net = 0

# Main loop to process multiple employees

while True:
    name = get_employee_name()
    if name.lower() == "end":    #Loop stops if user types "end"
        break

    hours = get_hours_worked()
    rate = get_hourly_rate()
    tax_rate = get_tax_rate()

    gross, tax, net = calculate_pay(hours, rate, tax_rate)
    display_employee_info(name, hours, rate, gross, tax_rate, tax, net)

# Update totals

    employee_count += 1
    total_hours += hours
    total_gross += gross
    total_tax += tax
    total_net += net

# Display final totals

display_totals(employee_count, total_hours, total_gross, total_tax, total_net)
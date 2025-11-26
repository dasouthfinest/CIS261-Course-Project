# O'Tria Fee
# CIS261
# Course Project Phase 2: Using Lists and Dictionaries to Store and Retrieve Data

# Get employee name
def get_employee_name():
    return input("Enter employee name (or 'End' to finish): ")

# Get hours worked
def get_hours_worked():
    return float(input("Enter hours worked: "))

# Get hourly rate
def get_hourly_rate():
    return float(input("Enter hourly rate: "))

# Get tax rate
def get_tax_rate():
    return float(input("Enter income tax rate as a decimal (.08 = 8%): "))

# NEW: Get from/to dates
def get_dates():
    from_date = input("Enter FROM date (mm/dd/yyyy): ")
    to_date = input("Enter TO date (mm/dd/yyyy): ")
    return from_date, to_date

# Calculate gross, tax, net
def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

# Display employee info (now includes dates)
def display_employee_info(name, from_date, to_date, hours, rate, gross, tax_rate, tax, net):
    print(f"\nEmployee: {name}")
    print(f"From Date: {from_date}")
    print(f"To Date: {to_date}")
    print(f"Hours Worked: {hours}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross:.2f}")
    print(f"Tax Rate: {tax_rate:.2%}")
    print(f"Income Tax: ${tax:.2f}")
    print(f"Net Pay: ${net:.2f}\n")

# Process all employees after loop ends
def process_employees(employee_list):
    totals = {
        "employees": 0,
        "hours": 0,
        "gross": 0,
        "tax": 0,
        "net": 0
    }

    for emp in employee_list:
        name, from_date, to_date, hours, rate, tax_rate = emp

        gross, tax, net = calculate_pay(hours, rate, tax_rate)

        display_employee_info(name, from_date, to_date, hours, rate, gross, tax_rate, tax, net)

        totals["employees"] += 1
        totals["hours"] += hours
        totals["gross"] += gross
        totals["tax"] += tax
        totals["net"] += net

    return totals

# Display totals from dictionary
def display_totals(totals):
    print("\nPayroll Summary")
    print(f"Total Employees: {totals['employees']}")
    print(f"Total Hours Worked: {totals['hours']}")
    print(f"Total Gross Pay: ${totals['gross']:.2f}")
    print(f"Total Income Tax: ${totals['tax']:.2f}")
    print(f"Total Net Pay: ${totals['net']:.2f}")

# Main program
def main():
    employee_data = []

    while True:
        name = get_employee_name()
        if name.lower() == "end":
            break

        from_date, to_date = get_dates()
        hours = get_hours_worked()
        rate = get_hourly_rate()
        tax_rate = get_tax_rate()
        print()

        employee_data.append([name, from_date, to_date, hours, rate, tax_rate])

    totals = process_employees(employee_data)
    display_totals(totals)

if __name__ == "__main__":
    main()
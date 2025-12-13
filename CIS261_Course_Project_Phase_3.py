# ********************************************************
# Name: O'Tria Fee
# Class: CIS 261
# Lab: Course Project Phase 3 
# ********************************************************

import datetime

def get_input(prompt, min_val=0, max_val=float('inf')):
    """Get and validate numeric input from user"""
    while True:
        try:
            value = float(input(prompt))
            if value < min_val or value > max_val:
                print("Value out of range.")
                continue
            return value
        except ValueError:
            print("Invalid number. Try again.")

def get_dates():
    """Get and return from date and to date for hours worked"""
    from_date = input("Enter FROM date (mm/dd/yyyy): ")
    to_date = input("Enter TO date (mm/dd/yyyy): ")
    return from_date, to_date

def calculate_pay(hours, rate, tax_rate):
    """Calculate gross pay, tax amount, and net pay"""
    gross_pay = hours * rate
    tax = gross_pay * tax_rate
    net_pay = gross_pay - tax
    return gross_pay, tax, net_pay

def display_employee(name, from_date, to_date, hours, rate, gross, tax_rate, tax, net):
    """Display information for a single employee"""
    print("\nEmployee Payroll Record")
    print("Name:", name)
    print("From Date:", from_date)
    print("To Date:", to_date)
    print("Hours Worked:", hours)
    print("Hourly Rate:", f"${rate:.2f}")
    print("Gross Pay:", f"${gross:.2f}")
    print("Income Tax Rate:", tax_rate)
    print("Income Tax:", f"${tax:.2f}")
    print("Net Pay:", f"${net:.2f}")

def write_employee_to_file(file_handle, from_date, to_date, name, hours, rate, tax_rate):
    """Write employee data to file in pipe-delimited format"""
    record = f"{from_date}|{to_date}|{name}|{hours}|{rate}|{tax_rate}\n"
    file_handle.write(record)

def generate_payroll_report():
    """Read file and generate payroll report with date filtering"""
    filter_date = input("Enter FROM date to filter (mm/dd/yyyy) or 'All': ")

    if filter_date != "All":
        try:
            datetime.datetime.strptime(filter_date, "%m/%d/%Y")
        except ValueError:
            print("Invalid date format.")
            return

    totals = {
        "employees": 0,
        "hours": 0,
        "tax": 0,
        "net": 0
    }

    try:
        with open("employees.txt", "r") as file:
            for line in file:
                from_date, to_date, name, hours, rate, tax_rate = line.strip().split("|")

                if filter_date == "All" or filter_date == from_date:
                    hours = float(hours)
                    rate = float(rate)
                    tax_rate = float(tax_rate)

                    gross, tax, net = calculate_pay(hours, rate, tax_rate)
                    display_employee(name, from_date, to_date, hours, rate, gross, tax_rate, tax, net)

                    totals["employees"] += 1
                    totals["hours"] += hours
                    totals["tax"] += tax
                    totals["net"] += net

        display_totals(totals)

    except FileNotFoundError:
        print("Employee file not found. Enter data first.")

def display_totals(totals_dict):
    """Display summary totals"""
    print("\nPayroll Summary")
    print("Total Employees:", totals_dict["employees"])
    print("Total Hours:", totals_dict["hours"])
    print("Total Taxes:", f"${totals_dict['tax']:.2f}")
    print("Total Net Pay:", f"${totals_dict['net']:.2f}")

def main():
    print("Employee Payroll System")
    print("Enter 'End' for employee name to finish")

    file = open("employees.txt", "a")

    while True:
        name = input("\nEnter employee name: ")
        if name.lower() == "end":
            break

        from_date, to_date = get_dates()
        hours = get_input("Enter hours worked: ", 0)
        rate = get_input("Enter hourly rate: ", 0)
        tax_rate = get_input("Enter tax rate (0.0 - 1.0): ", 0, 1)

        write_employee_to_file(file, from_date, to_date, name, hours, rate, tax_rate)

    file.close()

    generate_payroll_report()

if __name__ == "__main__":
    main()
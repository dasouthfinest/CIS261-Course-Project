# ********************************************************
# Name: O'Tria Fee
# Class: CIS 261
# Lab: Course Project Phase 4
# ********************************************************

import datetime

# -------------------------------
# LOGIN CLASS AND USER FUNCTIONS
# -------------------------------

class Login:
    """Class to store login information (UserID, Password, Authorization)"""
    def __init__(self, userid, password, authorization):
        self.UserID = userid
        self.Password = password
        self.Authorization = authorization

def CreateUsers(filename="Users.txt"):
    """
    Create users, passwords, and roles.
    - Opens Users.txt in append mode so new users are added.
    - Loops until user types 'End'.
    - Validates role as Admin/User.
    - Writes pipe-delimited records to file.
    """
    print("##### Create users, passwords, and roles #####")
    with open(filename, "a+") as UserFile:
        while True:
            username = GetUserName()
            if username.upper() == "END":
                break
            userpwd = GetUserPassword()
            userrole = GetUserRole()
            UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
            UserFile.write(UserDetail)
    PrintUserInfo(filename)

def GetUserName():
    """Prompt for username"""
    username = input("Enter user name or 'End' to quit: ")
    return username

def GetUserPassword():
    """Prompt for password"""
    userpwd = input("Enter password: ")
    return userpwd

def GetUserRole():
    """
    Prompt for role and validate Admin/User.
    - Keeps looping until a valid role is entered.
    - Prints a blank line after success for readability.
    """
    userrole = input("Enter role (Admin or User): ")
    while True:
        if userrole.upper() == "ADMIN" or userrole.upper() == "USER":
            print()  # blank line for readability
            return userrole
        else:
            userrole = input("Enter role (Admin or User): ")

def PrintUserInfo(filename="Users.txt"):
    """
    Display all users from file.
    - Reads Users.txt line by line.
    - Splits each record by pipe delimiter.
    - Prints UserID, Password, and Role.
    """
    with open(filename, "r") as UserFile:
        for line in UserFile:
            UserDetail = line.strip()
            UserList = UserDetail.split("|")
            if len(UserList) < 3:   # skip blank or malformed lines
                continue
            username = UserList[0]
            userpwd = UserList[1]
            userrole = UserList[2]
            print("User Name:", username, "Password:", userpwd, "Role:", userrole)

def LoginProcess(filename="Users.txt"):
    """
    Login process:
    - Prompts for UserID and Password.
    - Reads Users.txt and checks for match.
    - If valid, returns role and username.
    - If invalid, prints message and returns None.
    """
    UserName = input("Enter User Name: ")
    UserPassword = input("Enter Password: ")
    with open(filename, "r") as UserFile:
        for line in UserFile:
            UserDetail = line.strip()
            UserList = UserDetail.split("|")
            if len(UserList) < 3:   # skip blank or malformed lines
                continue
            if UserName == UserList[0] and UserPassword == UserList[1]:
                UserRole = UserList[2]
                print("Login successful")
                return UserRole, UserName
    # If no match found
    print("Invalid login. Exiting.")
    return None, None

# -------------------------------
# PAYROLL FUNCTIONS (FROM PHASE 3)
# -------------------------------

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

def generate_payroll_report():
    """
    Read file and generate payroll report with date filtering.
    - Prompts for filter date or 'All'.
    - Reads employees.txt and calculates gross, tax, net.
    - Displays each employee record and totals.
    """
    filter_date = input("Enter FROM date to filter (mm/dd/yyyy) or 'All': ")

    if filter_date.upper() != "ALL":
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

# -------------------------------
# MAIN PROGRAM FLOW
# -------------------------------

def main():
    # Step 1: Create users
    CreateUsers()

    # Step 2: Show Data Entry header before login
    print("##### Data Entry #####")

    # Step 3: Login
    role, userid = LoginProcess()
    if role is None:
        return  # stop program cleanly if login fails

    # Step 4: Authorization branching
    if role.upper() == "ADMIN":
        # Admin can enter employees
        with open("employees.txt", "a") as file:
            while True:
                name = input("\nEnter employee name (or End to finish): ")
                if name.lower() == "end":
                    break
                from_date, to_date = get_dates()
                hours = get_input("Enter hours worked: ", 0)
                rate = get_input("Enter hourly rate: ", 0)
                tax_rate = get_input("Enter tax rate (0.0 - 1.0): ", 0, 1)
                file.write(f"{from_date}|{to_date}|{name}|{hours}|{rate}|{tax_rate}\n")
        generate_payroll_report()

    elif role.upper() == "USER":
        # User only reporting
        generate_payroll_report()

if __name__ == "__main__":
    main()
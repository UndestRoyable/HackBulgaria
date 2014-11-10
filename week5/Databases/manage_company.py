import sqlite3


def menu_print():
    print("Hello! I'm your company manager!")
    print("You have the following commands:")
    print("list_employees, monthly_spending, yearly_spending, add_employee, delete_employee, update_employee")
    print("If you want to see how they work, type -commands ")


def commands_description():
    print("""list_employees - Prints out all employees,
            in the following format name - position""")

    print(""" monthly_spending - Prints out the total sum for monthly
            spending that the company is doing for salaries""")
    print(" yearly_spending - Prints out the total sum for one year of operation (Again, salaries)")
    print("add_employee, the program starts to promt for data, to create a new employee.")
    print("""delete_employee <employee_id>,
            the program should delete the given employee from thje database""")
    print("""update_employee <employee_id>,
             the program should prompt the user to change each of the fields for the given employee""")

db = sqlite3.connect("company")
db.row_factory = sqlite3.Row
cursor = db.cursor()
result = cursor.execute("SELECT * FROM employees")

menu_print()

command = input("Enter command:")

if command == "-commands":
    commands_description()

elif command == "list_employees":
    for row in result:
        print("{} - {}".format(row["name"], row["position"]))

elif command == "monthly_spending":
    monthly_spending = cursor.execute("SELECT SUM(monthly_salary) as spending FROM employees;")
    for row in monthly_spending:
        print(row["spending"])

elif command == "yearly_spending":
    yearly_salaries = cursor.execute("SELECT SUM(monthly_salary*12) as salaries FROM employees;")
    for row in yearly_salaries:
        salaries = row["salaries"]

    yearly_bonuses = cursor.execute("SELECT SUM(yearly_bonus) as bonuses FROM employees;")
    for row in yearly_bonuses:
        bonuses = row["bonuses"]
    yearly_spending = salaries + bonuses
    print(yearly_spending)

elif command == "add_employee":
    name = input("Enter name: ")
    monthly_salary = input("Enter monthly salary: ")
    yearly_bonus = input("Enter yearly bonus: ")
    position = input("Enter position: ")

    cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
                  VALUES(?, ?, ?, ?)''', (name, monthly_salary, yearly_bonus, position))
    print('New user created!')
    db.commit()

elif command == "delete_employee":
    employee_id = input("Enter the employee_id: ")
    cursor.execute("DELETE FROM employees WHERE id = ? ", (employee_id,))
    db.commit()
    print("The employee with ID {} was succesfully deleted!".format(employee_id))

elif command == "update_employee":
    employee_id = input("Enter the employee_id: ")
    name = input("Enter name: ")
    monthly_salary = input("Enter monthly salary: ")
    yearly_bonus = input("Enter yearly bonus: ")
    position = input("Enter position: ")

    cursor.execute('''UPDATE employees SET name = ?, monthly_salary = ?,
                     yearly_bonus = ?, position = ?
                     WHERE id = ?''', (name, monthly_salary, yearly_bonus, position, employee_id))
    db.commit()
    print("The employee with ID {} was succesfully updated!".format(employee_id))

db.close()

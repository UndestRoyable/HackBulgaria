class Employee:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class HourlyEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary_per_hour = salary

    def weekSalary(self, hours):
        if hours <= 40:
            return hours * self.salary_per_hour
        else:
            over_worked = hours - 40
            return 40 * self.salary_per_hour + over_worked * self.salary_per_hour * 1.5


class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.week_salary = salary

    def weeklyPay(self, hours):
        return self.week_salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name)
        self.salary = salary
        self.bonus = bonus

    def weeklyPay(self, hours):
        return self.salary + self.bonus


def main():
    staff = []
    staff.append(HourlyEmployee("Morgan, Harry", 30.0))
    staff.append(SalariedEmployee("Lin, Sally", 52000.0))
    staff.append(Manager("Smith, Mary", 104000.0, 50.0))
    for employee in staff :
        hours = int(input("Hours worked by " + employee.getName() + ": "))
        pay = employee.weekSalary(hours)
        print("Salary: %.2f" % pay)


if __name__ == '__main__':
    main()
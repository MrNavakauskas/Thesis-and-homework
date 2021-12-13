# Create an application that:
# • Should have a Class Employee
# • The employee should have the following characteristics: name, hourly rate, working_from
# • Have a private method that calculates how many days the employee worked from the day you entered (from_work) to
# today (given that the employee works 7 days a week)
# • Should have a method of calculating_remuneration that uses the method described above to calculate the total
# salary (given that the employee works 8 hours a day)
# • Should have a Class Normal Employee that would change the Employee’s class so that it calculates the salary
# while working employee 5 days a week
# • Create the desired Employee object
# • Create the desired Normal Employee object
# • Run the Calculate_Remuneration function with both objects

import datetime


class Employee:
    def __init__(self, name, hourly_rate, working_from):
        self.name = name
        self.hourly_rate = hourly_rate
        self.working_from = working_from

    def working_hours(self):
        working_from = datetime.datetime.strptime(self.working_from, "%Y, %m, %d, %H, %M, %S")
        now = datetime.datetime.today()
        diff = now - working_from
        return diff.days * 8

    def salary_calc(self):
        salary = self.hourly_rate * self.working_hours()
        print(self.name + " earned " + str(salary))


class NormalEmployee(Employee):
    def working_hours(self):
        working_from = datetime.datetime.strptime(self.working_from, "%Y, %m, %d, %H, %M, %S")
        now = datetime.datetime.today()
        diff = now - working_from
        return (diff.days * 8) / 7 * 5


gediminas = Employee("Gediminas", 18, "2019, 03, 12, 12, 00, 00")
gediminas_normal = NormalEmployee("Gediminas", 18, "2019, 03, 12, 12, 00, 00")
gediminas.salary_calc()
gediminas_normal.salary_calc()

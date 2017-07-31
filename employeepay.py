"""
Author: Mattyb
Description: This class determines an employees pay given the hourly wage and the number of hours he works based on a 40 hour work
week and a 1.5 times overtime pay scale.
Notes: I see the need to use self as a nested requirement in the total pay for some reason
Notes: I also need to ensure i clean up my area of print jobs.

"""


class EmployeePay():

    def __init__(self):
        self.hourly_wage = 0
        self.hours = 0

    def overtime(self):
        return (self.hours - 40) * (self.hourly_wage + (self.hourly_wage / 2))

    def regular_pay(self):
        if self.hours >= 40:
            return self.hourly_wage * 40
        elif self.hours <= 0:
            return "No pay due!"
        else:
            return self.hours * self.hourly_wage

    def total_weekly_pay(self):
        print("Total Weekly Pay = ")
        if self.hours <= 0:
            return "No pay due!"
        else:
            return self.regular_pay(self) + self.overtime(self)

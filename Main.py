
class Employee:
    def __init__(self, lastname, name, age, experience, customers_served=0):
        self.Name = name
        self.LastName = lastname
        self.Age = age
        self.Experience = experience
        self.CustomersServed = customers_served
        self.Rate = 300
        self.Salary = self.CustomersServed * self.Rate + 8000

    def print_employee_card(self):
        print("Прізвище:", self.LastName)
        print("Ім'я:", self.Name)
        print("Вік:", self.Age)
        print("Досвід:", self.Experience)
        print("Обслугованих Клієнтів:", self.CustomersServed)

    def salary_paycheck(self):
        print("Ваша ЗП:", self.Salary)


class Cashier(Employee):
    def __init__(self, lastname, name, age, experience, cash_collected):
        super().__init__(lastname, name, age, experience)
        self.Rate = 200
        self.CashCollected = cash_collected
        self.Salary = cash_collected / self.Rate + 8000

    def print_employee_card(self):
        super().print_employee_card()
        print("Грошей Зібрано:", self.CashCollected)

    def salary_paycheck(self):
        print("Ваша ЗП (Cashier):", self.Salary)


class Guard(Employee):
    def __init__(self, lastname, name, age, experience, guard_licence):
        super().__init__(lastname, name, age, experience)
        self.Rate = 1100
        self.GuardLicence = guard_licence
        self.Salary = experience * self.Rate + 8000

    def print_employee_card(self):
        super().print_employee_card()
        print("Ліцензія Охоронця:", self.GuardLicence)

    def salary_paycheck(self):
        print("Ваша ЗП (Guard):", self.Salary)


# Створення працівників
employee1 = Employee("Samchuk", "Maxim", 24, 3, 25)
employee2 = Cashier("Horodski", "Mykhailo", 23, 1, 5200)
employee3 = Guard("Kovalenko", "Ivan", 25, 5, "L-12345")

employees = [employee1, employee2, employee3]

for employee in employees:
    print("\nІнформація про працівника:")
    employee.print_employee_card()
    employee.salary_paycheck()



try:
    employee3 = Sigmector("Olegiv", "Mychailo", "54", 1, "BO4184821CI")
    employee3.print_employee_info()
    employee3.show_licence()
    employee3.to_receive_a_salary()
except TypeError as error:
    logging.exception("Сталася помилка: %s", error)
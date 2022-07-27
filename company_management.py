from random import randint

class Employee(object):
    """
    Class describing an employee of certain department.
    
    Attributes:
        first_name   (string): first name of the employee.
        last_name    (string): last name of the employee.
        age          (int):    age of the employee.
        job          (string): name of the employee's job.
        salary       (float):  salary of the employee.
        bonus        (float):  bonus, that is predicted for the employee.
        total_salary (float):  total salary, which is salary + bonus, if bonus was applied (else bonus=0).
    """
    def __init__(self, first_name, last_name, age, job, salary, bonus):
        """
        Constructor of the Employyer class
        
        Parameters:
            first_name   (string): first name of the employee.
            last_name    (string): last name of the employee.
            age          (int):    age of the employee.
            job          (string): name of the employee's job.
            salary       (float):  salary of the employee.
            bonus        (float):  bonus, that is predicted for the employee.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.salary = salary
        self.bonus = bonus
        self.total_salary = salary

    def modify_bonus(self, bonus):
        """
        Function, that modifies actual bonus.
        
        Parameters:
            bonus (float):  bonus, that is predicted for the employee.
        """
        self.bonus = bonus
    def apply_bonus(self):
        """
        Function, that applies actual bonus.
        """
        self.total_salary = self.salary + self.bonus
        
    def __repr__(self):
        """
        String representation of the employee.
        """
        return "{}, {}, {}, {}, {}, {}, {}".format(self.first_name, self.last_name, self.age, self.job, self.salary, self.bonus, self.total_salary)
        
    def __str__(self):
        """
        String representation of the employee.
        """
        return self.__repr__()
    
    def get_first_name(self):
        """
        Function returning the first name of the employee
        
        Returns:
            first_name (string)
        """
        return self.first_name
    
    def get_last_name(self):
        """
        Function returning the last name of the employee
        
        Returns:
            last_name (string)
        """
        return self.last_name
    
class Department(object):
    """
    Class describing certain Department.
    
    Attributes:
        name             (string): department name
        users            (list):   list of instances of the Employee's class
        index_first_name (list):   index of the first names of the users
        index_last_name  (list):   index of the last names of the users
        amount           (int):    amount of users
    """
    
    def __init__(self, name):
        """
        Constructor of the Employyer class.
        
        Parameters:
            name             (string): department name
    """
        self.name = name
        self.users = []
        self.index_first_name = []
        self.index_last_name = []
        self.amount = 0
        
#         self.__class__.departments.append(name)
    
    def display_employees(self):
        """
        Function displaying informations about users in this department.
        """
        for user in self.users:
            print(user)
            
#     def display_departments(self):
#         for department in self.__class__.departments:
#             print(department)
            
    def create_user(self, first_name, last_name, age, job, salary, bonus):
        """
        Function creating new user based on given values.
        
        Parameters:
            first_name   (string): first name of the employee.
            last_name    (string): last name of the employee.
            age          (int):    age of the employee.
            job          (string): name of the employee's job.
            salary       (float):  salary of the employee.
            bonus        (float):  bonus, that is predicted for the employee.
        
        """
        user = Employee(first_name, last_name, age, job, salary, bonus)
        self.users.append(user)
        self.index_first_name.append(first_name)
        self.index_last_name.append(last_name)
        self.amount += 1
        
    def remove_employee(self, first_name, last_name):
        """
        Function deleting certain user based on given values.
        
        Parameters:
            first_name (string): first name of the employee.
            last_name  (string): last name of the employee.
        Returns:
            True if operation done correctly
            False otherwise
        """
        for i in range(self.amount):
            if self.index_first_name[i] == first_name and self.index_last_name[i] == last_name:
                self.users.pop(i)
                self.index_first_name.pop(i)
                self.index_last_name.pop(i)
                self.amount -= 1
                return True
        return False
                
    def apply_bonus(self, first_name=None, last_name=None):
        """
        Function applying bonus to the certain user based on given values. If both parameters are None, bonus is applied for all users.
        
        Parameters:
            first_name (string): first name of the employee.
            last_name  (string): last name of the employee.
        Returns:
            True if operation done correctly.
            False if user not found
        """
        if first_name is None and last_name is None:
            for i in range(self.amount):
                self.users[i].apply_bonus()
            return True
        for i in range(self.amount):
            if self.index_first_name[i] == first_name and self.index_last_name[i] == last_name:
                self.users[i].apply_bonus()
                return True
        return False
    
    def modify_bonus(self, first_name, last_name, bonus):
        """
        Function modyfying bonus to the certain user based on given values.
        
        Parameters:
            first_name (string): first name of the employee.
            last_name  (string): last name of the employee.
            bonus      (int):    new bonus for the employee.
        
        Returns:
            True if operation done correctly.
            False if user not found
        """
        for i in range(self.amount):
            if self.index_first_name[i] == first_name and self.index_last_name[i] == last_name:
                self.users[i].bonus = bonus
                return True
        return False
    
    def __repr__(self):
        """
        String representation of the department.
        """
        ret = ""
        for user in self.users:
            ret += "{}, {}\n".format(self.name, str(user))
        return ret
    
    def __str__(self):
        """
        String representation of the department.
        """
        return self.__repr__()

class Company(object):
    """
    Class describing the whole company.
    
    Attributes:
        departments (dict): dictionary with the following content scheme - (key:value) = ((string): (Department))
    """
    def __init__(self):
        """
        Constructor for the company class.

        Parameters:
            departments (dict): dictionary with the following content scheme - (key:value) = ((string): (Department))
        """
        self.departments = {}
    
    def display_departments(self):
        """
        Function, that displays only department names.
        """
        for department in self.departments:
            print(department)
            
    def display_all(self):
        """
        Function, that displays informations on all users of all the departments.
        """
        for department in self.departments:
            print(self.departments[department])
    
    def add_employee(self, department, first_name, last_name, age, job, salary, bonus):
        """
        Function, that adds employee to a certain department.
        
        Parameters:
            department   (string): department name.
            first_name   (string): first name of the employee.
            last_name    (string): last name of the employee.
            age          (int):    age of the employee.
            job          (string): name of the employee's job.
            salary       (float):  salary of the employee.
            bonus        (float):  bonus, that is predicted for the employee.
        """
        if department not in self.departments:
            self.departments[department] = Department(department)
        self.departments[department].create_user(first_name, last_name, age, job, salary, bonus)
    
    def remove_employee(self, department, first_name, last_name):
        """
        Function deleting certain user based on given values.
        
        Parameters:
            department (string): department's name
            first_name (string): first name of the employee.
            last_name  (string): last name of the employee.
        Returns:
            True if operation done correctly
            False otherwise
        """
        if department in self.departments:
            return self.departments[department].remove_employee(first_name, last_name)
        return False
        
        
    def apply_bonus(self, department=None, first_name=None, last_name=None):
        """
        Function applying bonus to the certain user based on given values.
        If department is None, bonus is applied to all workers.
        If department is not None, but both names are, bonus is applied to all workers in this department.
        
        Parameters:
            department (string): department name.
            first_name (string): first name of the employee.
            last_name  (string): last name of the employee.
        
        Returns:
            True if operation done correctly.
            False if user not found
        """
        if department is None:
            for name in self.departments:
                self.departments[name].apply_bonus(None, None)
            return True
        if department in self.departments:
            D = self.departments[department]
            if first_name is None and last_name is None:
                return D.apply_bonus(None, None)
            return D.apply_bonus(first_name, last_name)
        return False
            
    def modify_bonus(self, department, first_name, last_name, bonus):
        """
        Function modyfying bonus to the certain user based on given values.
        
        Parameters:
            department (string): department name.
            first_name (string): first name of the employee.
            last_name  (string): last name of the employee.
            bonus      (int):    new bonus for the employee.
        
        Returns:
            True if operation done correctly.
            False if user not found.
        """
        if department in self.departments:
            D = self.departments[department]
            return D.modify_bonus(first_name, last_name, bonus)
        
    def add_department(self, department):
        """
        Function adding new department.
        
        Parameters:
            department (string): department name.
        
        Returns:
            True if department added.
            False if already in company.
        """
        if department not in self.departments:
            D = Department(department)
            self.departments[department] = D
            
    def remove_department(self, name):
        """
        Function deleting certain department.
        
        Parameters:
            name (string): department name.
        
        Returns:
            True if department deleted.
            False if department doesn't exist
        """
        if name in self.departments:
            del self.departments[name]
            return True
        return False
    
    def export_data(self, filename):
        """
        Function, that exports all the user intel to external file.
        Parameters:
            filename (string) - name of external file.
        """
        with open(filename, 'w') as file:
            for name in self.departments:
                file.write("{}".format(self.departments[name]))
                    
        
        
if __name__ == '__main__':

    while True:
        choice = int(input("0 - random filled database \n1 - empty database\n"))
        if choice == 1 or choice == 0:
            break
    company = Company()
    if choice == 0:
        amount = int(input("Amount of data : "))
        # print(amount)
        departments = ["R&D", "Administration", "Customization", "HR"]
        first_names = ["Adam", "Anna", "Bartosz", "Michal", "Klaudia", "Julia", "Paulina", "Karolina"]
        last_names = ["Michalak", "Jerzykiewicz", "Jarosz", "Wilk", "Lis", "Kot"]
        ages = list(range(22, 65, 1))
        jobs = ["Junior Python Developer", "Mid Python Developer", "Senior Python Developer", "Database Administrator", "HR Specialist", "C# Developer", "Java Developer", "Dev-Ops Engineer"]
        salaries = list(range(4500, 10000, 500))
        bonuses = list(range(0, 1000, 100))

        
        for i in range(amount):
            d_id = randint(0, len(departments)-1)
            f_id = randint(0, len(first_names)-1)
            l_id = randint(0, len(last_names)-1)
            a_id = randint(0, len(ages)-1)
            j_id = randint(0, len(jobs)-1)
            s_id = randint(0, len(salaries)-1)
            b_id = randint(0, len(bonuses)-1)
            company.add_employee(departments[d_id], first_names[f_id], last_names[l_id], ages[a_id],
                                jobs[j_id], salaries[s_id], bonuses[b_id])

    while True:
        print("0 - add employee")
        print("1 - remove employee")
        print("2 - add department")
        print("3 - remove department")
        print("4 - show all departments")
        print("5 - show all")
        print("6 - modify bonus")
        print("7 - apply bonus")
        print("8 - export data")
        print("Other - end")
        choice = int(input("select: "))
        while choice not in [0,1,2,3,4,5,6,7,8]:
            choice = int(input("Bad choice, select: "))

        if choice == 0:
            department = input("Department name: ")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            age = int(input("Age: "))
            job = input("Job Title: ")
            salary = float(input("Salary: "))
            bonus =  float(input("Bonus: "))
            company.add_employee(department, first_name, last_name, age, job, salary, bonus)
            print("user added\n")

        elif choice == 1:
            department = input("Department name: ")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            if company.remove_employee(department, first_name, last_name):
                print("Employee removed\n")
            else:
                print("No employee with such values\n")
        
        elif choice == 2:
            department = input("Department name: ")
            if company.add_department(department):
                print("Department added\n")
            else:
                print("Department already exists")

        elif choice == 3:
            department = input("Department name: ")
            if company.remove_department(department):
                print("Department removed\n")
            else:
                print("Department doesn't exist\n")
        elif choice == 4:
            print("\n")
            company.display_departments()
            print("\n")
        elif choice == 5:
            print("\n")
            company.display_all()
            print("\n")
        elif choice == 6:
            department = input("Department name: ")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            bonus = float(input("Bonus: "))
            if company.modify_bonus(department, first_name, last_name, bonus):
                print("Done!\n")
            else:
                print("There were some issues...\n")
        elif choice == 7:
            department = input("Department name, if 'all' typed, everyone gets bonus: ")
            test = False
            if department == 'all':
                test = company.apply_bonus(None, None, None)
            else:
                first_name = input("First Name, if 'all' typed, everyone in this department gets bonus: ")
                if first_name == 'all':
                    test = company.apply_bonus(department, None, None)
                else:
                    last_name = input("Last Name: ")
                    test = company.apply_bonus(department, first_name, last_name)
            if test:
                print("Succesfully applied bonus!\n")
            else:
                print("There were some issues...\n")
        elif choice == 8:
            f = input("file name to export data: ")
            company.export_data(f)
            print("Done!")
        else:
            quit()
        
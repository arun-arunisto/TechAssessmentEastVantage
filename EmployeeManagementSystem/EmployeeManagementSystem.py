#Employee Management System

#1. Employee Class
class Employee:
    def __init__(self, emp_id, emp_name, emp_title, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_title = emp_title
        self.emp_department = emp_department
        
    #to display employee details
    def emp_details(self):
        data = f"Employee Id : {self.emp_id} \nEmployee Name : {self.emp_name} \nEmployee Title : {self.emp_title} \nEmployee Department : {self.emp_department}"
        print(data)

    #implementing string representation using dunder method __str__
    def __str__(self):
        return f"Employee Id: {self.emp_id} | Employee Name: {self.emp_name}"

#2. Department Class
class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.emp_list = [] #to store the employees data
    #add an employee
    def add_employee(self, employee):
        self.emp_list.append(employee)
        print("Employee Added Successfully!!")

    #remove an employee
    def remove_employee(self, emp_id):
        for emp in self.emp_list:
            if emp.emp_id == emp_id:
                self.emp_list.remove(emp)
                print(f"Employee {emp_id} removed from {self.dept_name} Department")
                return
        else:
            print(f"No data available for Employee ID {emp_id}")
    
    #listing all employee
    def all_employee(self):
        print(f"Employees in {self.dept_name} Department")
        if len(self.emp_list) != 0:
            for emp in self.emp_list:
                print(emp)
        else:
            print("No records found!!")

#Company Class with department dictionary
class Company:
    def __init__(self):
        self.dept_dict = {}
    #adding a department
    def add_department(self, dept_name):
        if dept_name not in self.dept_dict:
            self.dept_dict[dept_name] = Department(dept_name)
            print(f"{dept_name} Department Added Successfully!!")
        else:
            print(f"{dept_name} Department Already Exists")

    #remove department
    def remove_department(self, dept_name):
        if dept_name in self.dept_dict:
            del self.dept_dict[dept_name]
            print(f"{dept_name} Department Removed Successfully!!")
        else:
            print(f"{dept_name} Department Not exists!!")

    #displaying department
    def display_departments(self):
        print("Departments:")
        if len(self.dept_dict) != 0:
            for dept in self.dept_dict:
                print(dept)
        else:
            print("No records added")
        

def main():
    company = Company()
    while True:
        option = input("[1] Company Dashboard [2] Exit \nSelect the option: ")
        if option == "1":
            while True:
                opt = input("[1] Department [2] Employee [3] Back \nSelect the option: ")
                if opt == "1":
                    while True:
                        dept = input("[1] Departments [2] Add Department [3] Remove Department [4] Back \nSelect the option: ")
                        if dept == "1":
                            company.display_departments()
                        elif dept == "2":
                            dept_name = input("Department name: ")
                            company.add_department(dept_name)
                        elif dept == "3":
                            dept_name = input("Department name: ")
                            company.remove_department(dept_name)
                        elif dept == "4":
                            break
                        else:
                            print("Invalid Option!!")
                elif opt == "2":
                    while True:
                        emp = input("[1] Employees [2] Add Employee [3] Remove Employee [4] Back \nSelect the option: ")
                        if emp == "1":
                            dept = input("Enter the department name: ")
                            if dept in company.dept_dict:
                                company.dept_dict[dept].all_employee()
                            else:
                                print(f"{dept} Department not added")
                        elif emp == "2":
                            dept = input("Enter the department name: ")
                            if dept in company.dept_dict:
                                print("Enter the employee details")
                                emp_id = input("Enter ID: ")
                                emp_name = input("Enter name: ")
                                emp_title = input("Enter title: ")
                                employee = Employee(emp_id, emp_name, emp_title, dept)
                                company.dept_dict[dept].add_employee(employee)
                            else:
                                print(f"{dept} Department not added")
                        elif emp == "3":
                            dept = input("Enter the department name: ")
                            if dept in company.dept_dict:
                                emp_id = input("Enter the employee ID: ")
                                company.dept_dict[dept].remove_employee(emp_id)
                            else:
                                print(f"{dept} Department not added")
                        elif emp == "4":
                            break
                        else:
                            print("Invalid Option!!")
                elif opt == "3":
                    break
                else:
                    print("Invalid Option!!")
        elif option == "2":
            print("Thank You!!")
            break
        else:
            print("Invalid Option!!")
                        
                                    

if __name__ == "__main__":
    main()
        

    


    

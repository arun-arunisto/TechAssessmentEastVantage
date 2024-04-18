# TechAssessmentEastVantage
## 1. Employee Management System
Employee management system is a pure python oriented project and 3 main classes in this project
- Employee
- Department
- Company

### 1. Employee Class
In Employee class 4 arguments and one method to display employee details and i use dunder method __str__ for representation
```Python
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
```
### 2. Department Class
In Department class there's we have options to add, remove, display all employees. To save the employee data we are using list here.
```python
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
```

### 3. Company Class
In company class we are able to add department remove department and we can list all departments
```python
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
```
### main() method
Inside the main method i write all other programming workflow that able to access by the client/user


## Workflow
Program worflow, first you need to clone this repo using `git clone` command, like below
```Command
git clone https://github.com/arun-arunisto/TechAssessmentEastVantage
```

After cloning the repo change your directory to `EmployeeManagementSystem` using below command
```Command
cd EmployeeManagementSystem
```

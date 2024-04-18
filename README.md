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
### 2. 

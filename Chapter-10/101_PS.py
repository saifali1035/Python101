class Employee_Details:
    def submit_details(self, name, age, dep):
        with open('/workspaces/Python101/Chapter-10/Employee.txt','a') as f:
            f.write(f"\nName of new employee is {name}, his age is {age} and his dep is {dep}")


name, age, dep=input("Hi ! What is your name, age and dep with space in between : ").split()
New_Record=Employee_Details()
New_Record.submit_details(name, age, dep)

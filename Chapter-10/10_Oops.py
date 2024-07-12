#creating a class
class School:
    Name="VWPS International School"
    Fees=80000
    #init construct
    def __init__(self):
        print("Student data created !")

    def getTeacherStrength(self, signature):
        print(f"The Numbers of Teacher are {self.TeacherStrength}\n{signature}")
    #static method
    @staticmethod
    def greetUser():
        print("Good Morning sir")

#class instantiaton
Saif_New_School = School()

#getting attribute
print("Saif's New School is", Saif_New_School.Name)

#changing attribute
print("Earlier Fees was", Saif_New_School.Fees)
#this is intstance attribute and take precidence over class attributes
Saif_New_School.Fees=90000
print("New Fees is", Saif_New_School.Fees)

#printing fuction with self paranmeter
Saif_New_School.TeacherStrength=90
Saif_New_School.getTeacherStrength("Thanks !!")

Saif_New_School.greetUser()
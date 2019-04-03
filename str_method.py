class employee:
    def __init__(self):
        self.name="Kaustubh"
        self.salary=100000
    def __str__(self):
        return "Name=" +self.name+ " Salary="+str(self.salary)

e1=employee()
print(e1)
    

class employee:
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary

class sales(employee):
    def __init__(self,nm,sal,inc):
        super().__init__(nm,sal)
        self.inct=inc
    def getSalary(self):
        return self.salary+self.inct


e1=employee("Kaustubh",78998)
print("Total salary of {} is {}".format(e1.getName(),e1.getSalary()))

s1=sales("Kaustubh",78998,8)
print("Total salary of {} is {}".format(s1.getName(),s1.getSalary()))

        

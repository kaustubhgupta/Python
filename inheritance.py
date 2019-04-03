class quad:
    def __init__(self,a,b,c,d):
        self.side1=a
        self.side2=b
        self.side3=c
        self.side4=d
    def perimeter(self):
        return self.side1+self.side2+self.side3+self.side4

class rect(quad):
    def __init__(self,a,b,c=None,d=None):
        super().__init__(a,b,c,d)
        self.side3=self.side1
        self.side4=self.side2
    

        

class person:
    counter=0
    def __init__(self,a='ravi',b='male'):
         self.name=a
         self.gender=b
         person.counter=person.counter+1
    def showinfo(self):
        print('Name:',self.name)
        print('Gender:',self.gender)
    @classmethod
    def count(cls):
        print('No of objects created:',cls.counter)
        
        

class employee:
    def __new__(cls):
        print("__new__ method ")
        inst=object.__new__(cls)
        return inst
    def __init__(self):
        print("__init__ method")
        self.name="Hello"

e1=employee()
print(e1.name)

        

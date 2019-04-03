age=7
def a():
    print("Global variable 'age':",globals()['age'])

    #Modifying Global variable inside the function
    globals()['age']=23
    print("Global variable 'age' inside the function:",globals()['age'])

    #A local variable
    age=11
    print("Local Variable 'age':",age)
    return
a()
print("Checking global varibale outside the function:",age)

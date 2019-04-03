age=7
def a():
    global age
    age=12
    print("Age is : ",age)
    return
a()
print("Age Outside function is: ",age)

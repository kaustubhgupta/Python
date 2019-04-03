class car:
    def __init__(self,a=40):
        self.__speed=a
    def get_speed(self):
        return self.__speed
    def set_speed(self,a):
        self.__speed=a
        return
    

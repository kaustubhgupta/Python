def food(f):
    tip=0.1*f
    total=f+tip
    per_person=total/num
    return per_person
def movie(m):
    return m/num
num=int(input("Enter the no of persons:"))
total_food=int(input("Enter amonut spend on food:"))
total_movie=int(input("Entet the amount spend on movie:"))
x=food(total_food)
y=movie(total_movie)
print("Per person contibution:{}".format(x+y))

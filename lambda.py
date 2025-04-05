#Add 10 to argument and return the result
x = lambda a: a + 10
print(x(5))

#summarize argument a, b, c and return the result
x = lambda a,b,c: a + b + c
print(x(5,6,2))

#classes & objects
#create a class
class MyClass:
    x = 5
    print(MyClass) #this line of code wass meant to be a mistake 

#create an object
p1 = MyClass()
print(p1.x)


#concatenation of strings
a = "Hello World!"
b = "Welcome New User"
c = a + b 
d = a + " " + b
print(c)
print(d)

#Boolean 
print(10==9)
print(10==20)
print(10<20)

a = 16
b = 20
if a < b:
    print("You are not qualified")
else:
    print("You are qualified")

#Operators
#Assignment operators  

#membership operators
car=["BMW", "Ford", "Benz"]
print("Ford" in car)
print("Volvo" not in car)
print("Benz" not in car) 

#identity operators
x = 10
y = 10
z = x
print(x is y)
print(z is x)
print(y is x)
print("I just like the timeless elegance of marble and the warmth of wood in interior designs")
print("I would like my dream home to be built with the perfect mix of style and practicality")

cars = ["lambo", "benz", "ferrari"]
print(type(cars))
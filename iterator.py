mytuple =("Red", "Blue", "Yellow")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "Red"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "Yellow"
for x in mystr:
    print(x)


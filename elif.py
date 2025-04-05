x = 5
y = 10
if y < x:
    print("y is less than x")
elif x < y:
    print("x is less than y")

#shorthand if
    x = 5
    y = 10
    if x < y: print("x is less than y")

#shorthand if else
    x = 5 
    y = 10
    print("x is less than y") if x < y else print("y is not less than x")

#if statements with logical operators
#AND
x = 10
y = 15
z = 35
if x < z and y > x:
    print("The expression is true")

#OR
x = 10
y = 15
z = 35
if x < z or y < x:
    print("One of the expression is true")

#NOT
x = 10
y = 15
z = 35
if not x > z:
    print("One of the expression is true")

#nested if statements
x = 41
if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is greater than 20")
    else:
        print("x is not greater than 20")
#while loop
i = 1
while i < 6:
    print(i)
    i +=1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break 
    i += 1

#for loop
Animals = ["Goat", "pig", "kangaroo"]
for x in Animals:
    print(x)

#to loop through a string:
for x in "Happy Moments":
    print(x)

cars = ['Ford', 'Benz', 'Lexus', 'Urus', 'CAT', 'Volvo', 'Volkswagen', 'Suzuki']
for x in cars:
    print(x)
    if x == 'Volvo':
        break 
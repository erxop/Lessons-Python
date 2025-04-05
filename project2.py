def get_last_digit (number):
    return number % 10
number = int(input("Please enter a number: "))
last_digit = get_last_digit(number)
print(last_digit)
num=int(input("Enter any number: "))
lastdigit = num%10
if lastdigit%3==0:
    print("This number is divisible by 3.")
else: 
    print("This number is not divisible by 3.")


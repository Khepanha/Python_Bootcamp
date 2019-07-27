import random
number = input("Enter a number: \n>> ")
try:
    number = int(number)
    for i in range(number):
        print(random.randint(0,100))
except:
    print(random.randint(0,100))

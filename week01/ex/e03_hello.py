number = input("Enter number: \n>> ")
if number == "":
    print("Nothing to display.")
else:
    number = int(number)
    for i in range(number):
        print("Hello World!")

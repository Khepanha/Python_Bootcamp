while True:
        number = input("Enter a number: \n>> ")
        try:
                number = int(number)
                if number%2 == 0:
                    print(f"{number} is EVEN")
                else:
                    print(f"{number} is ODD")
        except:
                if number.isdigit == False or number != "EXIT":
                        print (f"{number} is not a valid number.")
                if number == "EXIT":
                        break
        


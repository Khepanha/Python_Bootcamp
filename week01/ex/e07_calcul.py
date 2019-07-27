total = 0
while True:
    number = input("Enter a number: \n>> ")
    if number == "exit":
        break
    else:
        try:
            number = int(number)
            total += number
            print("TOTAL: ",total)
        except:
            print("TOTAL: ",total)

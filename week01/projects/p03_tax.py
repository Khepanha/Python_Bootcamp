while True:
    Input = input("Please enter your amount: \n>>")
    if Input.isdigit() == True:
        amount = int (Input)
        while True:
            Input = input("Please enter tax rate: \n>>")
            if Input.isdigit() == False:
                print ("Rate is incorrect, try again.")
                continue
            rate = int (Input)
            if rate < 99 and rate > 1:
                print ("===== ===== ===== ===== =====")
                print ("AMOUNT: " + repr(amount))
                print ("RATE: " + repr(rate) + "%")
                print ("===== ===== ===== ===== =====")
                TAX = (amount * rate)/100
                NET = amount - TAX
                print ("TAX: " + repr(TAX) + "$")
                print ("NET: " + repr(NET) + "$")
                print ("===== ===== ===== ===== =====")
                break
            if rate > 99 or rate < 1:
                print ("Rate is incorrect, try again.")
                continue
        break
    if Input.isdigit() == False:
        print ("Number is incorrect, try again.")
        continue
       
  
        






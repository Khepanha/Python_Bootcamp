import random
i = 1
sum = 0
print ("Welcome to the dice game!")
while True:
    num = input ("Enter the number of dice you want to roll: ")
    if num.isdigit() == False:
        print ("USAGE: The number must be between 1 and 8")
        continue
    num1 = int(num)
    if num1 > 8 or num1 < 1:
        print ("USAGE: The number must be between 1 and 8")
        continue
    while i <= num1:
        RAN = random.randint(1,6)
        print ("Dice " + repr(i) + " : " + repr(RAN))
        sum += RAN
        i += 1
    print ("========== \n" + "RESULT: " + repr(sum) + "\n==========")
    break
    

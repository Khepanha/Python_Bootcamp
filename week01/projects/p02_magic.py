import random
while True:
    ran = random.randint(1,88)
    A = ran
    name = input ("Hello, what is your name? \n")
    print ("Well " + name + ", try to guess the number I have in mind:")
    num = input()
    num1 = int(num)
    if num1 == A:
        print ("You won in 1 turn only, that's amazing!")
        num = input ("Do you want to play again? [Y/N] \n")
        if num != "Y" and num != "N":
            print ("Sorry, I did not understand. Let me repeat:")
            num = input("Do you want to play again? [Y/N] \n")
        if num == "N":
            print ("Ok, bye " + name + "! See you later!")
            break
        if num == "Y":
            continue
    for i in range(1,3):
        if num1 > 88 or num1 < 0:
            num2 = input ("Invalid number, USAGE: 1-88, try again! \n")
            num1 = int(num2)
        if num1 > A: 
            num2 = input ("Too high, try again! \n")
            num1 = int(num2)
        if num1 < A:
            num2 = input ("Too low, try again! \n")
            num1 = int(num2)
        if num1 == A:
            print ("It took you " + repr(i+1) + " turn to guess my number which was " + repr(A) + "!")
    print ("It took you " + repr(i+1) + " turn to guess my number which was " + repr(A) + "!")
    num = input ("Do you want to play again? [Y/N] \n")
    if num != "N" and num != "Y":
        print ("Sorry, I did not understand. Let me repeat:")
        num = input("Do you want to play again? [Y/N] \n")
    if num == "N":
        print ("Ok, bye " + name + "! See you later!")
        break
    if num == "Y":
        continue

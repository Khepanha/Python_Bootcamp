code = input ("Enter your encrypted message: \n>> ")
arr = list(code)
newstr = ""
if code != "":
    for i in range(len(arr)):
        A = ord(arr[i])
        if A >= 65 and A <= 90:
            D = A - 13
            if D < 65:
                B = 65 - D
                C = 90 - B
                newstr += chr(C)
            else:
                newstr += chr(D)
        if A >= 97 and A <= 122:
            D = A - 13
            if D < 97:
                B = 97 - D
                C = 122 - B
                newstr += chr(C)
            else:
                newstr += chr(D)
        if A < 65:
            newstr += chr(32)
    print (newstr)
else:
    print ("Nothing to decode.")


    

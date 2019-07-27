code = input ("Enter your secret message: \n>> ")
arr = list(code)
newstr = ""
if code != "":
    for i in range(len(arr)):
        A = ord(arr[i])
        if A >= 65 and A <= 90:
            B = A + 13
            if B > 90:
                B -= 90
                B += 64
            newstr += chr(B)
        if A >= 97 and A <= 122:
            B = A + 13
            if B > 122:
                B -= 122
                B += 96
            newstr += chr(B)
        if A < 65:
            newstr += chr(32)
    print (newstr)
else:
    print ("Nothing to encode.")
        


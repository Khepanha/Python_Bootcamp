string = input ("Enter a string: \n>> ")
arr = list(string)
newstr = ""
if string != "":
    for i in range(len(arr)):
        if ord(arr[i]) >= 97 and ord(arr[i]) <= 122:
            newstr += arr[i].upper()
        if ord(arr[i]) >= 65 and ord(arr[i]) <= 90:
            newstr += arr[i].lower()
    print (newstr)
else:
    print ("Empty")


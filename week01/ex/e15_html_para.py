arr = ""
while True:
        string = input("Enter a string: \n>> ")
        arr += "\n" + "<h1>"+string+"</h1>"
        s = arr.replace("<h1>GEN</h1>"," ")
        if string == "GEN":
                print(s)
                break




from datetime import datetime
def time_list(num):
    a = []
    i=1
    n=0
    count=0
    h=datetime.now().hour
    m=datetime.now().minute
    s=datetime.now().second
    if type(num) == type(1) or num.isdigit():
        num = int(num)
        while n<num:
            if s+n<60:
                a.append(str(h)+":"+str(m)+":"+str(s+n))
            elif s+n==60*i:
                count+=1
                i+=1
                a.append(str(h)+":"+str(m)+":"+str(0))
            else:
                a.append(str(h)+":"+str(m+count)+":"+str((s+n)-60*count))
            n+=1
        return a
    if (num == ""):
        return (">> []")
    elif num.isdigit() == False :
        return (">> []")
    else:
        return (">> []")
print(time_list(""))


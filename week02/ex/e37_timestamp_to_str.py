import time
from time import gmtime
def timestamp_to_str (T):
    if type (T) == type (1) or T.isdigit() == True:
        T = int (T)
        DT = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(int(T)))
        return DT
    else:
        return (">> Your timestamp is not valid.")
print (timestamp_to_str (1623646780))

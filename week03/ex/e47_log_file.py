import os
from datetime import datetime
from time import strftime
def log_file (F):
    while (True):
        I = input ("$: ")
        if (I == "EXIT"):
            break
        else:
            f = open (F, 'a')
            DT = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            f.write("[" + DT + "] " + I + "\n")
            f.close()
log_file()

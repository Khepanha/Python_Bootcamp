def read_file(F):
    try:
        f = open(F, 'r')
        return (f.read())
        f.close()
    except:
        return "Invalid Filename"
print (read_file())

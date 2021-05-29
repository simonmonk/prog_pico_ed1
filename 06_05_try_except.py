file_name = "testXX.txt"
try:
    f = open(file_name, "r")
    print(f.read())
    f.close()
except:
    print("File {} doesn't exist".format(file_name))
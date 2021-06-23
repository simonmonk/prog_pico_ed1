config_file = "config.txt"
count = 0

def read_config():
    global count
    try:
        f = open(config_file, "r")
        count = int(f.read())
        f.close()
    except:
        pass
    
def write_config():
    f = open(config_file, "w")
    f.write(str(count))
    f.close()
    
read_config()
print(count)
count += 1
write_config()

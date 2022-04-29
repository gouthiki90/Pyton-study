f = open("/usr/Desktop/hello.txt", "r")

for line in f.readlines():
    print(line)
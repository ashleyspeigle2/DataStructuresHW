counter = 0

f = open("HelloWorld.txt","r")
for line in f.readlines():
    print(counter, line)
    counter = counter + 1

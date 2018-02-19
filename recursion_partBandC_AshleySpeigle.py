import time

#recursive Part B and C
k = []
v = []
def dynamicFib(n):
    if n in k:
        i = k.index(n)
        return v[i]

    else:
        if n <= 1:
            k.append(n)
            i = k.index(n)
            v.append(1)
            return v[i]

        else:
            v.append(dynamicFib(n - 1)+dynamicFib(n - 2))
            k.append(n)
            i = k.index(n)
            return v[i]
#recursion
def fib(n):
    if (n < 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
#nonrecursion
def fib2(n):
    x = 1
    y = 1
    z = 0
    for i in range (n):
        z = x + y
        x = y
        y = z

    return(x)
       
#calculate run time
def timing():
    for p in range(30,101,10):
        startTime2 = time.time()
        fib2(p)
        endTime2 = time.time()
        print ("Linear time is: ", endTime2 - startTime2)

        startTime3 = time.time()
        dynamicFib(p)
        endTime3 = time.time()
        print ("Dynamic is: ", endTime3 - startTime3)
        
        startTime = time.time()
        fib(p)
        endTime = time.time()
        print ("Recursive is: ", endTime - startTime)


        if (endTime - startTime) > (endTime2 - startTime2):
            print("Recursion is slower")

        elif(endTime - startTime) == (endTime2 - startTime2):
            print("Recursion and nonrecursion is the same")

        elif(endTime3 - startTime3) > (endTime2 - startTime2):
            print("Nonrecursion is faster than dynamic")

        elif(endTime2 - startTime2) > (endTime3 - startTime3):
            print("Dynamic is faster than nonrecursion")
            
        elif(endTime3 - startTime3) == (endTime2 - startTime2):
            print("Nonrecursion and dynamic are the same")

        else:
            print("Recursion is faster")

timing()

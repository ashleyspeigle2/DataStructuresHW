#bubblesort

listOfN = [7,5,4,1,9,0,3,-2,21,-6,13]

sortedList = sorted(listOfN)

print(listOfN)

def bubbleSort(list):
    count = 0
    for i in range(len(list)):
        for  i in range(len(list) - 1):
            first = list[i]
            second = list[i + 1]
            if (first > second):
                swap = first
                list[i] = second
                list[i + 1] = swap
                count += 1

    return list

bubbleSort(listOfN)
print(listOfN)
print(sortedList)
print(listOfN == sortedList)





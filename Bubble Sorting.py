sizeOfList = eval(input("Enter The Total Number To Be Inserted.:\t"))
listValues = []

for index in range(sizeOfList):
    element = (input(f"Enter The {index+1} Element Of The List:\t"))
    listValues.append(element)
print("All The Inserted Element In The List is:", listValues, "\tAnd The Size Of List is:", len(listValues))

length =len(listValues)
totalPasses = 0
totalComparision = 0
totalSwapping = 0
flag = False
for index1 in range(length-1):
        totalPasses +=1
        for index2 in range(0,length - index1 - 1):
            totalComparision +=1
            if listValues[index2] > listValues[index2+1]:
                listValues[index2], listValues[index2+1] = listValues[index2+1], listValues[index2]
                totalSwapping +=1
                # temp = listValues[index2]
                # listValues[index2] = listValues[index2+1]                             #Second  Method Of Swapping
                # listValues[index2+1] = temp
                
                # print("\nBefore Swapping", listValues[index2], listValues[index2+1])
                # listValues[index2] = listValues[index2] - listValues[index2+1]
                # listValues[index2+1] = listValues[index2+1] + listValues[index2]      # Third  Method Of Swapping
                # listValues[index2] = listValues[index2+1] - listValues[index2]
                # print("Final Swapping", listValues[index2], listValues[index2+1])
                flag = True
        if flag == False:
                break
print(f"\nAll The Inserted Element In The List After Bubble Sorting is: {listValues}. The Size Of List is: {len(listValues)}")
print(f"Total Number of  Passes, Comparision & Swapping Used To Be Sort Is {totalPasses}, {totalComparision} & {totalSwapping} respectively.")
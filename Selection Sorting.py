sizeOfList = eval(input("Enter The Total Number To Be Inserted.:\t"))
listValues = []

for index in range(sizeOfList):
    element = (input(f"Enter The {index+1} Element Of The List:\t"))
    listValues.append(element)
print("All The Inserted Element In The List is:", listValues, "\tAnd The Size Of List is:", len(listValues))

length =len(listValues)
totalPasses = 0
totalSwapping = 0
totalComparision = 0
for index1 in range(length - 1):
    totalPasses +=1
    minimum = index1
    for index2 in range(index1 + 1, length):
        if listValues[minimum] > listValues[index2]:
            minimum = index2
            totalComparision +=1
    listValues[index1], listValues[minimum] = listValues[minimum], listValues[index1]
    totalSwapping +=1
print(f"\nAll The Inserted Element In The List After Selection Sorting is: {listValues}. The Size Of List is: {len(listValues)}. \nTotal Number of Passes, Comparision & Swapping Used To Be Sort Is {totalPasses}, {totalComparision} & {totalSwapping} respectively.")

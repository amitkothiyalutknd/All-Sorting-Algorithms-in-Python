sizeOfList = eval(input("Enter The Total Number To Be Inserted.:\t"))
listValues = []

for index in range(sizeOfList):
    element = (input(f"Enter The {index+1} Element Of The List:\t"))
    listValues.append(element)
print("All The Inserted Element In The List is:", listValues, "\tAnd The Size Of List is:", len(listValues))

length =len(listValues)
totalPasses = 0
totalSwapping = 0
for index1 in range(1,length):
    totalPasses +=1
    Key = listValues[index1]
    index2 = index1 - 1
    while listValues[index2] > Key and index2 >= 0:
        listValues[index2+1] = listValues[index2]
        totalSwapping +=1
        index2 -=1
    listValues[index2+1] = Key

print(f"\nAll The Inserted Element In The List After Insertion Sorting is: {listValues}. The Size Of List is: {len(listValues)}. \nTotal Number of Passes(Comparision) & Swapping Used To Be Sort Is {totalPasses} & {totalSwapping} respectively.")

listValues = list(map(int, input("Enter Multiple Elements To Be Insert In List One. Seperate Inputs Single Space.:\t").split(' ')))
print(f"All The Inserted Elements Of The First List is: {listValues}. And The Size Of List is: {len(listValues)}.")

def mergeSort(listValues):
    if len(listValues) < 2:
        return listValues
    sorted = []
    mid = int (len(listValues)/2)
    merge1 = mergeSort(listValues[:mid])
    merge2 = mergeSort(listValues[mid:])
    index1 = index2 = 0
    while index1 < len(merge1) and index2 < len(merge2):
        if merge1[index1] > merge2[index2]:
            sorted.append(merge2[index2])
            index2 +=1
        else:
            sorted.append(merge1[index1])
            index1 +=1
    sorted += merge1[index1:]
    sorted += merge2[index2:] 
    return sorted

print("\nAll The Inserted Element In The List After Quick Sorting is:\t", mergeSort(listValues) ,f"\tThe Size Of List is: {len(listValues)}.")
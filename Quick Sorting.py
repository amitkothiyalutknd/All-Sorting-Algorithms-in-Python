listValues = list(map(int, input("Enter Multiple Elements To Be Insert In List One. Seperate Inputs From Single Space.:\t").split(' ')))
print(f"All The Inserted Elements Of The First List is: {listValues}. And The Size Of List is: {len(listValues)}.")

def quickSort(listvalues, low, high):
    if (low < high):
        pivot, lowIndex, highIndex = low, low, high
        while (lowIndex < highIndex):
            while listvalues[lowIndex] <= listvalues[pivot] and lowIndex < high:
                lowIndex += 1
            while listvalues[highIndex] > listvalues[pivot]:
                highIndex -= 1
            if (lowIndex < highIndex):
                listvalues[lowIndex], listvalues[highIndex] = listvalues[highIndex], listvalues[lowIndex]
        listvalues[pivot], listvalues[highIndex] = listvalues[highIndex], listvalues[pivot]
        quickSort(listvalues, low, highIndex - 1)
        quickSort(listvalues, highIndex + 1, high)
        return listvalues
    else:
      return listvalues

print("\nAll The Inserted Element In The List After Quick Sorting is: ", quickSort(listValues, 0, len(listValues) - 1), f"\tThe Size Of List is: {len(listValues)}.")
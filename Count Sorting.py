def foundMax(listValues):
    maxNumber = listValues[0]
    for index in range(1, len(listValues)):
        if maxNumber < listValues[index]:
            maxNumber = listValues[index]
    return maxNumber

def countSortNumber(listValues):
    maxNo = foundMax(listValues)
    countArray = [0] * (maxNo + 1)
    for index1 in range(len(listValues)):
        index2 = listValues[index1]
        countArray[index2] +=1
    index2, index3 = 0, 0
    while index2 <= maxNo:
        if countArray[index2] > 0:
            listValues[index3] = index2
            countArray[index2] -=1
            index3 +=1
        else:
            index2 +=1
    return listValues

def countSortLetter(listValues):
    tempArray = [ord(alphabet) for index in listValues for alphabet in index]
    maxNo = foundMax(tempArray)
    countArray = [0 for i in range(256)]
    for index1 in range(len(tempArray)):
        index2 = tempArray[index1]
        countArray[index2] +=1
    index2, index3 = 0, 0
    while index2 <= maxNo:
        if countArray[index2] > 0:
            tempArray[index3] = index2
            countArray[index2] -=1
            index3 +=1
        else:
            index2 +=1
    for index in range(len(tempArray)):
            listValues[index] = chr(tempArray[index])
    return listValues
    
while True:
    chce = int(input('''
                1 Insert Number To Be Sort
                2 Insert Alphabet To Be Sort
                3 Exit Oeration
                '''))
    if chce == 1:
        listValues = list(map(eval, input(f"Enter Multiple Numbers To Be Insert In List. Seperate Inputs From Comma.:\t").split(',')))
        print(f"\nAll The Inserted Numbers In The List is: {listValues}. \tAnd The Size Of List is: {len(listValues)}.")
        print("All The Inserted Numbers In The List After Count Sorting is:\t", countSortNumber(listValues),f"\tThe Size Of List is: {len(listValues)}.")
    elif chce == 2:
        listValues = list(map(str, input(f"Enter Multiple Alphabets To Be Insert In List. Seperate Inputs From Comma.:\t").split(',')))
        print(f"\nAll The Inserted Alphabets In The List is: {listValues}. \tAnd The Size Of List is: {len(listValues)}.")
        print("All The Inserted Alphabets In The List After Count Sorting is:\t", countSortLetter(listValues),f"\tThe Size Of List is: {len(listValues)}.")
    elif chce == 3:
            break
    else:
            print("Invalid Choice")

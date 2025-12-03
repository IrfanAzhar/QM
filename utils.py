def summingMethod (intNumber):
    sumList = []
    resultantSum = 0
    resultantSum = sum_to_one_digit(intNumber)
    sumList.append(resultantSum)
    while resultantSum > 9:
        resultantSum = sum_to_one_digit(resultantSum)
        sumList.append(resultantSum)
    return sumList


def sum_to_one_digit (intNumber):
    #print("the input to sum_to_one_digit() is = ", intNumber)
    strNumber = str(intNumber)
    len_intNumber = len(strNumber)
    #print(strNumber[len_intNumber - 1], type(strNumber))
    sumOfDigits = 0

    for x in range(len_intNumber):
        sumOfDigits += int(strNumber[x])
        #print("value of iteratoir x = ", x, " and temp sum =  ", sumOfDigits)
    return sumOfDigits

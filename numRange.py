import copy

def numRange(A,B,C):
    res=[]
    for i in range(len(A)):
        currentSum = 0
        currentArr = []
        j = i
        while j < len(A) and currentSum+A[j] <=C:
            currentSum+=A[j]
            currentArr.append(A[j])
            if currentSum >=B:
                newArr = copy.deepcopy(currentArr)
                res.append(newArr)
            j+=1
    return len(res)


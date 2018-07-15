import copy

def prettyPrint(A):
    
    row = [A]*(2*A-1)
    square =[]
    for i in range(2*A-1):
        rowy = copy.deepcopy(row)
        square.append(rowy)

    index = 1
    while index <= A:
        for j in range(index,2*A-1-index):
            print(index,j)
            square[index][j] = A-index
            square[j][index] = A-index
            square[2*A-2-index][j] = A-index
            square[j][2*A-2-index] = A-index
        index+=1

    for i in range(len(square)):
        print(square[i])
    return square


print(prettyPrint(4))

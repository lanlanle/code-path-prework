def nextGreater(A):
        res = []
        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                if A[j]>A[i]:
                    res.append(A[j])
                    break
            else:
                res.append(-1)
        res.append(-1)
        return res
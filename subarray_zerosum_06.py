def zero_sum(arr):
    res = []
    for i in range(0, len(arr)):
        for j in range(len(arr)-1,i,-1):
            if(sum(arr[i:j])==0):
                res.append((i,j-1))
        if(arr[i]==0):
            res.append((i,i))
    return res
arr = [4,-1,-3,1,2,-1]
print(zero_sum(arr))
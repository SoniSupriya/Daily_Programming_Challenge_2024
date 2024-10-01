def sliding_window_max(arr,k):
    res = []
    n,i = len(arr),0
    while (i+k<=n):
        m = max(arr[i:i+k])
        #print(arr[i:i+k])
        res.append(m)
        i += 1
    return res

arr =  [7,7,7,7]
k = 1
print(sliding_window_max(arr,k))
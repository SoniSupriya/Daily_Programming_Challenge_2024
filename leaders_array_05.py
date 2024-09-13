def leadersArray(arr):
    res_list=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]<arr[j]):
                break
        else:
            if (arr[i] not in res_list): res_list.append(arr[i]) 
    return res_list
arr = [7, 10, 4, 10, 6, 5, 2]
print(leadersArray(arr))
def first_element_repeat_k(arr,k):
    arr_count={}
    for i in range(len(arr)):
        if(arr[i]in arr_count):
            arr_count[arr[i]]+=1
        else:
            arr_count[arr[i]]=1

    print(arr_count)
    for i in range(len(arr)):
        if(arr_count[arr[i]]==k):
            return arr[i]
    return -1
arr=[6,6,6,6,7,7,8,8,8]
k = 3
print(first_element_repeat_k(arr,k))
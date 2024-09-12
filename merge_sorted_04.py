def merge_Sorted(arr1,arr2):
    arr = sorted((arr1+arr2))
    count = 0
    for i in range(0,len(arr1)):
        arr1[i]=arr[count]
        count+=1
    for i in range(0,len(arr2)):
        arr2[i]=arr[count]
        count+=1
    return arr1,arr2
arr1 = [2,3,8]
arr2 = [4,6,10]
print(merge_Sorted(arr1,arr2))


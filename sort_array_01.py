def sortColors(nums):
    c0,c1,c2 = 0,0,0
    for i in nums:
        if(i==0):
            c0+=1    
        elif(i==1):
            c1+=1
        elif(i==2):
            c2+=1
        
    for i in range(0,len(nums)):
        if(i<c0):
            nums[i]=0
        elif((i>=c0) and (i<c0+c1)):
            nums[i]=1
        else:
            nums[i]=2
nums = [0,1,2,1,0,2,1,0]
sortColors(nums)
print(nums)
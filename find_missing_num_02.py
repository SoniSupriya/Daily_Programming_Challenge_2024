def missingNumber(nums):
    n = 1
    for i in range(1,len(nums)):
        if(n in nums):
            n =n+1
        elif((n not in nums)and(1<=n<len(nums))):
            return n
            break
    else:
        return len(nums)
nums = [1,2,3,4]
print(missingNumber(nums))

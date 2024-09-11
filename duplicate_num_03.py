def findDuplicate(nums):
        freq={}
        n_max=max(nums)
        for i in range(n_max+1):
            if nums[i] in freq:
                return nums[i]
            else:
                freq[nums[i]]=1
nums = [1,3,4,2,2]
print(findDuplicate(nums))
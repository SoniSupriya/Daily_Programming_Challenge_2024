def longest_substring(strs):
    strs.sort()
    res = ""
    first = strs[0]
    last = strs[-1]
    min_len = min(len(first),len(last))
    i = 0
    while(i<min_len and first[i]==last[i]):
        i = i+1
    if(i == 0):
        return res
    
    return first[:i]

strs = ["alone"]
print(longest_substring(strs))
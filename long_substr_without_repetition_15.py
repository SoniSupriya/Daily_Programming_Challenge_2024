def substring_without_repetition(s):
    max_len = 0
    left = 0
    res_set = set()
    for i in range(len(s)):
        while(s[i] in res_set):
            res_set.remove(s[left])
            left = left+1
        res_set.add(s[i])
        max_len = max(max_len,i-left+1)
    return max_len
S = "i"
print(substring_without_repetition(S))    
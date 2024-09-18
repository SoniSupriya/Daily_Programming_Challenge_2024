def group_anagrams(strs):
       dictionary = {}
       for word in strs:
           sortedWord = ''.join(sorted(word))
           if sortedWord not in dictionary:
               dictionary[sortedWord] = [word]
           else:
               dictionary[sortedWord] += [word]
       return [dictionary[i] for i in dictionary]

strs = ["abc", "def", "ghi"]
print(group_anagrams(strs))

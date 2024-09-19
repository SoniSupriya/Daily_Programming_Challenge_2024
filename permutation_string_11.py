from itertools import permutations

def permute_string(s: str):
    unique_permutations = set(permutations(s))
    return [''.join(p) for p in unique_permutations]

print(permute_string("abcd"))
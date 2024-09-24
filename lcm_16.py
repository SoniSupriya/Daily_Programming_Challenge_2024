import math
def lcm(a,b):
    pro = a*b
    div = math.gcd(a,b)
    return pro/div
m = 123456
n = 789012
print(lcm(m,n))
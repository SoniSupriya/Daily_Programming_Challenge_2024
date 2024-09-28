def sortedInsert(s, element):
    if len(s) == 0 or element > s[-1]:
        s.append(element)
        return
    else:
        temp = s.pop()
        sortedInsert(s, element)
        s.append(temp)
def sortStack(s):
    if len(s) != 0:
        temp = s.pop()
        sortStack(s)
        sortedInsert(s, temp) 
def printStack(s):
    for i in s[::1]:
        print(i, end=" ")
    print()

s = [4,4,45,4,6,7]
sortStack(s)
(printStack(s))
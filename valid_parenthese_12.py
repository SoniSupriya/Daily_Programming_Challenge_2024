def valid_parenthese(s):
    l = []
    if(len(s)==0 ):
        return True
    elif (len(s)%2!=0):
        return False
    else:
        for i in range(len(s)):
            if(s[i] in "([{"):
                l.append(s[i])
            else:
                if(s[i]==")" and l[-1]!="("):
                    return False
                if(s[i]=="]" and l[-1]!="["):
                    return False
                if(s[i]=="}" and l[-1]!="{"):
                    return False
                if((s[i]==")" and l[-1]=="(")or (s[i]=="]" and l[-1]=="[")or (s[i]=="}" and l[-1]=="{")):
                    l.pop()
        return True
s = "([{}])"
print(valid_parenthese(s))

txt = "word"
str1=""
txt1 = txt.strip()
x = txt1.rsplit(" ")
#print(x)
for i in range(len(x)-1,-1,-1):
    if(x[i]==''):
        pass
    elif((i==0)):
        str1=str1+x[i]
    else:
        str1= str1+(x[i])+" "
print(str1)
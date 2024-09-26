def count_divisors(n):
    count=0
    for i in range(1,int(n**0.5)+1):
        if(n%i==0):
            if(n/i==i):
                count +=1
            else:
                count +=2
    return count
number = int(input("Enter the number : "))
print(count_divisors(number))
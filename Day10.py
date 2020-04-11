n=int(input())
current=0
max=0
while n>0:

    rem=n%2

    if rem==1:
        current+=1
        if current>max:
            max=current
    else:
        current=0
    n = n // 2
print(max)

n=int(input())
for k in range(0,n):
    s=input()
    even=""
    odd=""

    for i in range(0,len(s)):
        if i%2==0:
            even+=s[i]
        else:
            odd+=s[i]
    print(even,odd)   

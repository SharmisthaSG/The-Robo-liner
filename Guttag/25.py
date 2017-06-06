s = "1.23,2.4,3.123" #sequence of decimals as a string
x,y,sum=0,0,0
for i in range(len(s)):
    if s[i] == ",":
        y=i
        t=s[x:y]
        x=y+1
        t=float(t)
        sum+=t
    if i==len(s)-1:
        y=i
        t=s[x:y+1]
        x=y+1
        t=float(t)
        sum+=t
print sum

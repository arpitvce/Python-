tup=tuple(input().split(','))
s=set()
for i in tup:
    s.add(i)
l=[]
for i in s:
    count=0
    for j in tup:
        if j==i:
            count+=1
    l.append((i,count))
tupp=tuple(l)
print(tupp)
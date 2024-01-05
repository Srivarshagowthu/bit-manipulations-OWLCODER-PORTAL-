'''a=[1,2,3,3,4,4,5]
b0=[]
b1=[]
res=0
res1=0
for i in range(len(a)):
    p="0"+bin(a[i])[2::]
    if p[-2]=="1":
        b1.append(a[i])
    if p[-2]=="0":
        b0.append(a[i])
for j in b1:
    res^=j
print(resu)
for k in b0:
    resu1^=k
print(resu1)'''
#32 range bit
'''n=11
st=" "
for i in range(31):
    if i>=0:
        mask=1<<i
        if (n&mask)>0:
            st+="1"
        else:
            st+="0"
    i-=1
print(st[::-1])'''
#msb

'''n=11
st=" "
for i in range(31):
    if i>=0:
        mask=1<<i
        if (n&mask)>0:
            print(i)
            break'''
#long subsequence
'''a=[0,1,0,3,2,3]
q=[-1]
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        p=[]
        p=a[i:i+2]
        for j in p:
            if j not in q and q[-1]<j:
                q.append(j)
print(*q)'''
##for the above ques
'''seq=[]
for i in nums:
    index=bisect.bisect_left(seq,i)
    if index>=len(seq):
        seq.append(i)
    else:
        seq[index]=i'''
#array range of bitwise operation
'''a=[1,2,3,4,5,6]
m=2
n=5
res=[]
for i in range(m,n+1):
    p=a[i]
    for j in range(m+1,n):
        p&=a[j]
    res.append(p)
print(res)'''



        

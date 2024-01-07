#32 bit generation
n=int(input())
st=""
for i in range(32):
    if(i>=0):
        mask=1<<i
    if(n&mask)>0:
        st+="1"
    else:
        st+="0"
print(int(st,2))
=================================
#and over a range
n=int(input())
a=list(map(int,input().split()))
k=int(input())
for i in range(k):
    l,r=map(int,input().split())
    p=a[l]
    for j in range(l,r+1):
        p&=a[j]
    print(p)
===============================
#####all twice except two
class Solution:
	def singleNumber(self, a):
		# Code 
		ans=[]
		p=a[0]
		for i in range(len(a)):#total xor value
		    p^=a[i]
		c=0
		while(p):
		    if(p&1):
		        break
		    c+=1
		    p>>=1
		x1=0
		x2=0
		for j in range(len(a)):
		    if a[j]&(1<<c):
		        x1^=a[j]
		    else:
		        x2^=a[j]
		ans.append(x1)
		ans.append(x2)
		return ans
		        


'''a=[2,3,5]
p=[]
for i in range(len(a)-1):
    if a[i]%a[i+1]==0 or a[i+1]%a[i]==0:
        print(a[i])
        print(a[i+1])'''
'''import itertools
p=[1,3,2]
q=list(itertools.permutations(p))
print(sorted(set(q)))'''
a=[2,7,9,3,1]
for j in range(len(a)-2):
    for i in range(j+1,len(a)):
        if i-j!=1:
            print(a[j]+a[i])
            print()

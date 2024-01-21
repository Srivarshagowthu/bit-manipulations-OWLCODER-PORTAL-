##from collections import Counter,OrderedDict
##from operator import itemgetter
##a=[5,2,1,3,2]
##d={}
##for i in a:
##    if i in d:
##        d[i]+=1
##    else:
##        d[i]=1
##p=sorted(d.items(),key=itemgetter(1))
##print(OrderedDict(sorted(d.items())))
##
##    
##
'''d = {'a': 2, 'b': 3, 'f': 1,  'h':1, 'l': 5}
sorted_d = {key for key, value in sorted(d.items(), key=lambda item: item[1])}
print(list(sorted_d))'''
from collections import Counter

class Solution:
    def kTop(self, a, N, K):
        # Use Counter to count occurrences
        counter = Counter(a)

        # Get the top K elements based on frequency
        top_k = [key for key, _ in counter.most_common(K)]

        # Print the top K elements
        print(top_k)

# Example usage
solution_instance = Solution()
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
N = len(a)
K = 2
solution_instance.kTop(a, N, K)


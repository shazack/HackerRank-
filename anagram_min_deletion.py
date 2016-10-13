#get the minimum number of deletions to make two strings anagrams of each other

from collections import Counter

def number_needed(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    count_a.subtract(count_b)
    final_sum = sum(abs(i) for i in count_a.values())
    return final_sum


   
    
   


a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

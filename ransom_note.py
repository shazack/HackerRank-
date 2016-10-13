#check if a ransom note can be made from a magazine if it contains all the words - no concatenation or substrings are allowed

from collections import Counter
def ransom_note(magazine, rasom):
    count_mag = Counter(magazine)
  
    #print count_mag
    count_rasom = Counter(rasom)
    count_rasom.subtract(count_mag)
    for i in count_rasom.values():
        if i>0:
            return False
    return True
   
    
m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    

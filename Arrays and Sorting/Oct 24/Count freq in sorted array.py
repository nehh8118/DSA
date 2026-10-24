class Solution:
    def countFreq(self, arr, target):
        # code here
        count={} #hash for counting freq
        for num in arr:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
                
        if target in count: #checking if target in array, else returning 0
            return count[target]
        else:
            return 0


'''
req: to return the freq of given target in array
approach: hashmap to count freq and return the target's freq
'''
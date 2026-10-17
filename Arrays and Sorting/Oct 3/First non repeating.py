class Solution:
    def firstNonRepeating(self, arr): 
        # code here
        count={}
        for i, num in enumerate(arr):
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for num in arr:
            if count[num]==1:
                return num
        return 0

    #req: return the first non-repeating element in an array, if all elements are repeating return 0
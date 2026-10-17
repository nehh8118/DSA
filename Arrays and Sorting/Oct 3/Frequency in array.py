class Solution:
    def countFreq(self, arr):
        #code here
        res=[]
        count={}
        for i, num in enumerate(arr): #creating a dictionary to store the frequency of each number in the array
            if num in count:
                count[num]+=1 #if already present in the dictionary, increment the count
            else:
                count[num]=1 #else add to dictionary
        return res
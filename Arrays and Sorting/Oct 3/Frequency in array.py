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

n = int(input("Enter the number of elements in the list: "))
arr = list(map(int, input("Enter the elements of the list separated by space: ").split()))

obj = Solution()
result = obj.countFreq(arr)
print(result)

#req: count the frequency of each number in the array and return its frequency.
#approach: The solution uses a dictionary to count the occurrences of each number in the array and returns the dictinary

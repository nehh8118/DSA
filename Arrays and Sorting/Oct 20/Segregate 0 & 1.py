class Solution:
    def segregate0and1(self, arr):
        # code here
        maxVal=max(arr)
        count=[0]*(maxVal+1)

        for num in arr:
            count[num]=count[num]+1
        arr[:]=[]

        for num, freq in enumerate(count):
            arr.extend([num]*freq)

        return arr

arr=list(map(int, input("Enter the elements of the list separated by space: ").split()))
obj = Solution()    
print(obj.segregate0and1(arr))


'''
req: Sort an array of integers containing only 0s, 1s.
approach: The solution uses a counting sort algorithm to do this
'''

            
class Solution:
    def reverseArray(self, arr):
        # code here
        l=0
        r=len(arr)-1
        while l<r:
            temp=arr[l]
            arr[l]=arr[r]
            arr[r]=temp
            l+=1
            r-=1

n = int(input("Enter the number of elements in the list: "))
arr = list(map(int, input("Enter the elements of the list separated by space: ").split()))   

obj = Solution()
obj.reverseArray(arr)       
print(arr)    
        
#req: return the reversed array
#approach: The solution uses two pointers, one starting at the beginning of the array and the other at the end.
# It swaps the elements at these pointers and moves them towards the center until they meet or cross    

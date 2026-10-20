class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        l=0
        r=len(nums)-1
        while l<r:
            if nums[l]%2==0: #if left element is even, moving to next
                l+=1
            elif (nums[r]%2)!=0: #if right element is odd, moving to next
                r-=1
            else: #if left element is odd and right element is even, swap
                nums[l], nums[r]= nums[r], nums[l]
                l+=1
                r-=1
        return nums

    solution = Solution()
    n = int(input("Enter the number of elements in the list: "))
    arr = list(map(int, input("Enter the elements of the list separated by space: ").split()))
    print("The sorted array is:", solution.sortArrayByParity(arr))
                
    '''
        #uses more space
        n=len(nums)
        even=[]
        odd=[]
        for i in range(n):
            if nums[i]%2==0:
                even= even+[nums[i]]
            else:
                odd= odd + [nums[i]]
        nums=even+odd
        return nums
        '''



        
        
        
        
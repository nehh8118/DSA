class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        left=nums1[:m]
        right=nums2

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                nums1[k]=left[i]
                i+=1
            else:
                nums1[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            nums1[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            nums1[k]=right[j]
            j+=1
            k+=1

solution = Solution()
m = int(input("Enter the number of elements in the first sorted array: "))
nums1 = list(map(int, input("Enter the elements of the first sorted array separated by space: ").split()))
n = int(input("Enter the number of elements in the second sorted array: "))
nums2 = list(map(int, input("Enter the elements of the second sorted array separated by space: ").split()))
solution.merge(nums1, m, nums2, n)
print("The merged sorted array is:", nums1)


'''
req: Merge two sorted arrays into one sorted array.
approach: The solution uses a two-pointer technique to merge the two sorted arrays into one sorted array
the later part of the merging sorted arrays of merge sort alg
'''


        
        
class Solution:
    def getSecondLargest(self, arr):
        # code here
        largest=SecondLargest=0
        for num in arr:
            if num>largest: #largest number is found, update largest and second largest
                SecondLargest=largest
                largest=num
            if num>SecondLargest and num<largest: #if the current number is greater than second largest and less than largest, update second largest
                SecondLargest=num
        if SecondLargest==0: #if there is no second largest number in the array, return -1
            return -1
        else:
            return SecondLargest

                
                
                
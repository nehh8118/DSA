def countingSort(arr):
    highest = max(arr)
    count=[0]*highest

    for num in arr:
        count[num]+=1

    sortedArr=[]

    for num, freq in enumerate(count):
        sortedArr.extend([num]*freq)

    return sortedArr

arr=list(map(int, input("Enter the elements of the list separated by space: ").split()))
result = countingSort(arr)
print(result)

'''
req: Sort an array of integers using counting sort.
approach: The solution uses a counting array to store the frequency of each integer in the input array. 
It then reconstructs the sorted array by iterating through the counting array. here, index is the num and element is the frequency of that num.
'''
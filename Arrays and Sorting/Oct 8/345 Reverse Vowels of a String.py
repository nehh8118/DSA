def reverseVowels(self, s: str) -> str:
    l = 0
    r = len(s) - 1
    listS = list(s)
    vowel = 'aeiouAEIOU'
    while l < r:
        if listS[l] not in vowel:
            l += 1
        elif listS[r] not in vowel:
            r -= 1
        else:
            listS[l], listS[r] = listS[r], listS[l]
            l += 1
            r -= 1
    return "".join(listS)

print(reverseVowels("hello"))

'''req: Reverse the vowels in a string
approach: Used two pointers, one starting from the beginning and the other from the end of the string 
to swap the vowels at these pointers and move them towards each other until they meet in the middle.
ADDITIONAL condition to check if they are vowels or else iterate to next'''

        
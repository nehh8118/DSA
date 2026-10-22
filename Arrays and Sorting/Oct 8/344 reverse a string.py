def reverseString(s: list[str]) -> None:
    l=0
    r=len(s)-1
    while l<r:
        s[l], s[r] = s[r], s[l]
        l+=1
        r-=1
    return s

print(reverseString(["h", "e", "l", "l", "o"]))

'''req: Reverse a string
approach: Used two pointers, one starting from the beginning and the other from the end of the string
to swap the elements at these pointers and move them towards each other until they meet in the middle.
'''



        
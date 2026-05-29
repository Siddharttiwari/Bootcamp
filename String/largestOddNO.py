"""
Input:
 s = "5347"
Output:
 "5347"
"""

def largestoddNumber(nums):
    for i in range(len(nums)-1,-1,-1):
        if int(nums[i])%2==1:
            return nums[:i+1]
    return " "

nums=input()
print(largestoddNumber(nums))
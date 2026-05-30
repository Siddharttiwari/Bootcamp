"""
THIS WILLL ONLY SHOW LENGTH OF THE SUBSEQUENCE
def longest_common_subsequence(str1,str2,m,n):
    if n==0 or m==0:
        return 0
    
    if str1[m-1]==str2[n-1]:
        return 1+longest_common_subsequence(str1,str2,m-1,n-1)
    else:
        return max(longest_common_subsequence(str1,str2,m,n-1),longest_common_subsequence(str1,str2,m-1,n))

str1=input()
str2=input()
m=len(str1)
n=len(str2)
print(longest_common_subsequence(str1,str2,m,n))
"""
"""
THIS WILL PRINT THE SUBSEQUECE
def longest_common_subsequence(str1,str2,m,n):
    if n==0 or m==0:
        return ""
    
    if str1[m-1]==str2[n-1]:
        return longest_common_subsequence(str1,str2,m-1,n-1) + str1[m-1]
    else:
        lcs1=longest_common_subsequence(str1,str2,m,n-1)
        lcs2=longest_common_subsequence(str1,str2,m-1,n)

        if lcs1>lcs2:
            return lcs1
        else:
            return lcs2
    

str1=input()
str2=input()
m=len(str1)
n=len(str2)
print(longest_common_subsequence(str1,str2,m,n))
"""
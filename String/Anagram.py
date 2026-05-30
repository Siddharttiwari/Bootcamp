"""
Given two strings, the task is to check whether they contain the same characters in the same frequency, even if the order is different. This condition is known as being anagrams. For example:

Input: "listen", "silent"
Output: Yes
"""

def anagram(string1,string2):
    freq=[0]*26
    if len(string1)!=len(string2):
        return False
    
    for char in string1:
        freq[ord(char)-ord('A')]+=1

    for char in string2:
        freq[ord(char)-ord('A')]-=1
    
    for count in freq:
        if count!=0:
            return False
    return True

string1=input().upper()
string2=input().upper()
print(anagram(string1,string2))

    
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

    
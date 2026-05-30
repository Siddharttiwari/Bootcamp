def nonrepeating(string):
    freq=[0]*256
    for char in string:
        freq[ord(char)]+=1
        
    for char in string:
        if freq[ord(char)]==1:
            return char

    return "Not found"
    
string=input()
print(nonrepeating(string))
        
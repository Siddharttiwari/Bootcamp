"""
strings = ["flower", "flow", "flight"]
output=fl
"""

def prefix(string):
    if len(string)==0:
        return ""
    base=string[0]
    for i in range(len(base)):
        for words in string[1:]:
            if (i==len(words)) or base[i]!=words[i]:
                return base[0:i]
    return base
    
string=input("Space separted value").split()
print(prefix(string))
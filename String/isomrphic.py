"""
Input:
 s = "foo", t = "bar"
Output:
 false
"""
def isomorphic(st1,st2):
    n1,n2=[0]*256,[0]*256
    n=len(st1)
    for i in range(n):
        if n1[ord(st1[i])]!=n2[ord(st2[i])]:
            return False
        
        n1[ord(st1[i])]=i+1
        n2[ord(st2[i])]=i+1
    return True
        
st1=input()
st2=input()
print(isomorphic(st1,st2))
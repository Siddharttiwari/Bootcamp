def vote(arr):
    n=len(arr)
    freq={}
    for el in arr:
        if el in freq:
            freq[el]+=1
        else:
            freq[el]=1
    
    for el in freq:
        if freq[el]>=n/4:
            return el
        else:
            return 0
        
arr=list(map(int,input().split()))
print(vote(arr))


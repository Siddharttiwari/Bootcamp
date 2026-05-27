x_diff=0
    freq={}
    for i in range(n):
        if arr[i] not in freq:
            freq[arr[i]]=i
        else:
            max_diff=max(max_diff,i-freq[arr[i]])
    return max_diff

arr=list(map(int,input().split()))
print(diff(arr))
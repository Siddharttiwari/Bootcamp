def deletesmallest(arr):
    n=len(arr)
    smallest=arr[0]
    for i in range(n):
        if arr[i]<smallest:
            smallest=arr[i]
    arr.remove(smallest)
    return arr

if __name__=="__main__":
    arr=list(map(int,input().split()))
    print(deletesmallest(arr))
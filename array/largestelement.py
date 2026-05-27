def largest(arr):
    n=len(arr)
    largest=arr[0]
    for i in range(n):
        if arr[i]>largest:
            largest=arr[i]
    return largest


if __name__=="__main__":
    arr=list(map(int,input().split()))
    print(largest(arr))




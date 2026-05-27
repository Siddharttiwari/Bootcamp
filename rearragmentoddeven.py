def rearrangment(arr):
    first_odd_index=0
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i],arr[first_odd_index]=arr[first_odd_index],arr[i]
            first_odd_index+=1
    return 

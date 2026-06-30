def traint(arr, dep):
    arr.sort()
    dep.sort()

    i = 1
    j = 0
    platforms = 1
    ans = 1

    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:
            platforms += 1
            ans = max(ans, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1

    return ans


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print(traint(arr, dep))
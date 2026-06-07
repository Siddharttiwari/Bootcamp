def maxWater(self, arr):
        n=len(arr)
        left,right=0,n-1
        maxleft=0
        maxright=0
        totalwater=0
        while left<=right:
            if arr[left]<=arr[right]:
                if arr[left]>=maxleft:
                    maxleft=arr[left]
                else:
                    totalwater+=maxleft-arr[left]
                left+=1
            else:
                if arr[right]>=maxright:
                    maxright=arr[right]
                else:
                    totalwater+=maxright-arr[right]
                right-=1
        return totalwater
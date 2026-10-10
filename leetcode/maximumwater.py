"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
"""



def maximumwater(nums):
    n = len(nums)
    maxwater = 0
    i = 0
    j = n - 1

    while i < j:
        water = min(nums[i], nums[j]) * (j - i)
        maxwater = max(maxwater, water)

        if nums[i] < nums[j]:
            i += 1
        else:
            j -= 1

    return maxwater
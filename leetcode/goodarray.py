"""
Input: nums = [1, 3, 3, 2]
Output: true
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. It can be seen that nums is a permutation of base[3] = [1, 2, 3, 3] (by swapping the second and fourth elements in nums, we reach base[3]). Therefore, the answer is true.
"""

def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        base = max(nums)

        if base != n - 1:
            return False

        for i in range(1, base):
            if nums.count(i) != 1:
                return False

        if nums.count(base) != 2:
            return False

        return True
        
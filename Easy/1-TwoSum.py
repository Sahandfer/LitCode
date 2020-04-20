"""
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
"""
class Solution(object):
    def twoSum(self, nums, target):
        rtype = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[j] + nums[i] == target):
                    rtype = [i,j]
                    break
            if (len(rtype)):
                break
        return rtype

if __name__ == "__main__":
    # Test Cases
    print(Solution().twoSum([2,7,11,15], 9))
    print(Solution().twoSum([3,2,4], 6))
    print(Solution().twoSum([-1,-2,-3,-4,-5], -8))

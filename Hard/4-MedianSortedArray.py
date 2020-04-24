class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        med1 = nums1[(len(nums1)-1)//2] if len(nums1)%2!= 0 else ((nums1[len(nums1)//2]+ nums1[(len(nums1)//2)-1])/2)
        med2 = nums2[(len(nums2)-1)//2] if len(nums2)%2!= 0 else ((nums2[len(nums2)//2]+ nums2[(len(nums2)//2)-1])/2)
        return (med1+med2)/2

if __name__ == "__main__":
    # Test Cases
    print(Solution().findMedianSortedArrays([1, 3], [2]))
    print(Solution().findMedianSortedArrays([1, 2], [3,4]))
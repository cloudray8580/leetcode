class Solution(object):

    # O(nlogn)
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = nums1 + nums2
        total.sort()
        length = len(total)
        index = length // 2
        if length % 2 == 0:
            median = (total[index-1] + total[index]) / 2.0
        else:
            median = total[index]
        return median

    # O(n)
    def findMedianSortedArrays2(self, nums1, nums2):
        total = []
        index1 = 0
        index2 = 0
        length1 = len(nums1)
        length2 = len(nums2)
        length = length1 + length2
        for i in range(length):
            # pay attentation to the position of condition
            # using the early stop verification
            # to avoid index out of range exception
            if index1 < length1 and (index2 == length2 or nums1[index1] <= nums2[index2]):
                # total[i] = nums1[index1]
                total.append(nums1[index1])
                index1 += 1
            elif index2 < length2 and (index1 == length1 or nums1[index1] > nums2[index2]):
                # total[i] = nums2[index2]
                total.append(nums2[index2])
                index2 += 1
        index = length // 2
        if length % 2 == 0:
            median = (total[index - 1] + total[index]) / 2.0
        else:
            median = total[index]
        return median

    # O(logn)
    def findMedianSortedArrays3(self, nums1, nums2):
        median = 0
        return median

instance = Solution()
nums1 = [1,3]
nums2 = [2]
print(instance.findMedianSortedArrays(nums1,nums2))
print(instance.findMedianSortedArrays2(nums1,nums2))
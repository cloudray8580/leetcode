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
        length1 = len(nums1)
        length2 = len(nums2)
        if length1 >= length2:
            maxi = length1
            tempnums1 = nums1
            tempnums2 = nums2
            lengthi = length1
            lengthj = length2
        else:
            maxi = length2
            tempnums1 = nums2
            tempnums2 = nums1
            lengthi = length2
            lengthj = length1
        mini = 0

        while maxi > mini:
            i = (maxi + mini) // 2
            j = (length1+length2)//2 - i # require length1 > length2

            if i-1 > 0 and i < lengthi and j-1 > 0 and j < lengthj:
                if tempnums1[i-1] <= tempnums2[j] and tempnums2[j-1] <= tempnums1[i]:
                    return max(tempnums1[i-1],tempnums2[j-1])
            elif i-1 > 0 and j < lengthi:
                if tempnums1[i - 1] <= tempnums2[j]:
                    return tempnums1[i-1]
            elif i < lengthi and j-1 > 0:
                if tempnums2[j-1] <= tempnums1[i]:
                    return tempnums2[j-1]

        median = 0
        return median

instance = Solution()
nums1 = [1,3]
nums2 = [2]
print(instance.findMedianSortedArrays(nums1,nums2))
print(instance.findMedianSortedArrays2(nums1,nums2))
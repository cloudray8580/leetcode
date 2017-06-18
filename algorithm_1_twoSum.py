class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1 in range(len(nums)):
            for index2 in range(index1+1,len(nums)):
                if nums[index1] + nums[index2] == target:
                    list = []
                    list.append(index1)
                    list.append(index2)
                    print(list)
                    return list


    def twoSumBetter(self, nums, target):
        if len(nums) <= 1:
            return False
        buffer_dict = {}
        for i in range(len(nums)):
            if nums[i] in buffer_dict:
                return [buffer_dict[nums[i]],i]
            else:
                buffer_dict[target-nums[i]] = i

instance = Solution()
# instance.twoSum([3,4,5,1],6)
print(instance.twoSumBetter([3,4,5,1],6))
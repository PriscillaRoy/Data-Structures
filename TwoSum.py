class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comp = list()
        for i in range(0,len(nums)):
            if (nums[i]) in comp :
                return (comp.index(nums[i]) , i)
            comp.append(target - nums[i])
        return False
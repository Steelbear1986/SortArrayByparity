class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        q = []
        q1 = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                q.append(nums[i])
            else:
                q1.append(nums[i])
        return q + q1

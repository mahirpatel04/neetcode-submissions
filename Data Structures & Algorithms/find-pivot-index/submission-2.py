class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums[1::])
        for i, l in enumerate(nums):
            print(leftSum, rightSum)
            if leftSum == rightSum:
                return i
            else:
                if i + 1 < len(nums):
                    rightSum -= nums[i+1]
                else:
                    rightSum = 0
                leftSum += l

        return -1
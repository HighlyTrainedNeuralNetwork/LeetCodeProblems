def minPairSum(nums):
    left, right = 0, len(nums) - 1
    nums = sorted(nums)
    max_pair = 0
    while left < right:
        max_pair = max(max_pair, nums[left] + nums[right])
        left += 1
        right -= 1
    return max_pair

minPairSum([3,5,4,2,4,6])
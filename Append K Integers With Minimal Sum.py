# Search for first element should be binary instead of simple iteration

def minimalKSum(nums, k):
    # sum of n terms in arithmetic progression with gap of 1 is (n)(n+1)/2
    nums = sorted(list(set(nums)))
    if nums[-1] <= k + len(nums):
        return (k + len(nums)) * (k + len(nums) + 1) // 2 - sum(nums)
    for i in range(len(nums)):
        if nums[i] - i > k:
            return (k + i) * (k + i + 1) // 2 - sum(nums[:i])

nums = [1,4,25,10,25]
k = 2
# nums = [5,6]
# k = 6
print(minimalKSum(nums, k))
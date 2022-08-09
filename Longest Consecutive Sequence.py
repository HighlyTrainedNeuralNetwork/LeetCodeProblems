def longestConsecutive(nums):
    len = 0
    nums = set(nums)
    for num in nums:
        if num - 1 not in nums:
            streak = 1
            while num + 1 in nums:
                num += 1
                streak += 1
            len = max(len, streak)
    return len

nums = [100, 4, 200, 1 , 3, 2]
print(longestConsecutive(nums))
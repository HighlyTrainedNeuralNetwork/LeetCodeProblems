def minimizeMax(nums, p):
    if not p:
        return 0
    nums.sort()

    def possible(mid):
        pairs = 0
        i = 1
        while i < len(nums):
            if nums[i] - nums[i - 1] <= mid:
                pairs += 1
                if pairs == p:
                    return True
                # this double increment is what confused me. I did not determine a way to enforce each element is
                # used once
                i += 1
            i += 1
        return False

    left = 0
    right = nums[-1] - nums[0]
    while left < right:
        mid = (left + right) // 2
        if possible(mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == "__main__":
    nums = [3,4,2,3,2,1,2]
    p = 3
    output = minimizeMax(nums, p)
    print(output)

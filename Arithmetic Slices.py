def numberOfArithmeticSlices(nums):
    deltas = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    slices = 0
    for i in range(len(deltas) - 1):
        window_size = 2
        window = deltas[i:i + window_size]
        expansion_room = len(deltas) - i - window_size
        while expansion_room >= 0 and len(set(window)) == 1:
            slices += 1
            window_size += 1
            expansion_room -= 1
            window = deltas[i:i + window_size]
    return slices




# nums = [1,2,3,4]
nums = [1,2,3,4,8,9,10]
print(numberOfArithmeticSlices(nums))
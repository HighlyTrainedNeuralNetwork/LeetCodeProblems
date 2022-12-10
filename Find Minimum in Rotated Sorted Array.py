# The interesting part of this is how you handle which of the endpoints need to shift
def findMin(nums):
    l, r = 0, len(nums) - 1
    if nums[l] < nums[r] or r == 0:
        return nums[l]
    while l <= r:
        c = (l + r) // 2
        if nums[c] < nums[c - 1]:
            return nums[c]
        elif nums[c] > nums[c + 1]:
            return nums[c + 1]
        else:
            if nums[c] > nums[0]:
                l = c + 1
            else:
                r = c - 1

if __name__ == "__main__":
    nums = [5,1,2,3,4]
    output = findMin(nums)
    print(output)
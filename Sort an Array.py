# Naive solution of swapping current and smallest element in a shrinking window was o(n^2).
# Intended solution appears to be merge or quick sort.


def sortArray(nums):
    def merge(left, right):
        output = []
        while left and right:
            if left[0] < right[0]:
                output.append(left.pop(0))
            else:
                output.append(right.pop(0))
        output.extend(left)
        output.extend(right)
        return output

    if len(nums) == 1:
        return nums
    left = nums[:len(nums) // 2]
    right = nums[len(nums) // 2:]
    left = sortArray(left)
    right = sortArray(right)
    return merge(left, right)

if __name__ == "__main__":
    nums = [5, 2, 3, 1]
    output = sortArray(nums)
    print(output)
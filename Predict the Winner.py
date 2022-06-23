# Initial naive recursion solution was too slow. I looked at solutions. Some consensus on memoization being
# the intended approach.

def predictTheWinner(nums):
    def looper(nums):
        if len(nums) == 1:
            return nums[0]
        score_1 = sum(nums) - looper(nums[1:])
        score_2 = sum(nums) - looper(nums[:-1])
        return max(score_1, score_2)
    if sum(nums) - looper(nums) <= looper(nums):
        return True
    return False

def predictTheWinner(nums):
    memo = {}
    def looper(nums, left, right):
        if (left, right) in memo.keys():
            return memo[(left, right)]
        if len(nums) == 1:
            memo[(left, right)] = nums[0]
            return nums[0]
        score_1 = sum(nums) - looper(nums[1:], left + 1, right)
        score_2 = sum(nums) - looper(nums[:-1], left, right - 1)
        memo[(left, right)] = max(score_1, score_2)
        return max(score_1, score_2)
    score_1 = looper(nums, 0, len(nums) - 1)
    if sum(nums) - score_1 <= score_1:
        return True
    return False

nums = [1, 5, 2]
print(predictTheWinner(nums))
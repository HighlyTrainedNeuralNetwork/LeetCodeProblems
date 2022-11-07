from itertools import accumulate
import operator
def productExceptSelf(nums):
    pre = list(accumulate(nums, operator.mul))[:-1]
    post = list(accumulate(nums[::-1], operator.mul))[:-1][::-1]
    pre.insert(0, 1)
    post.append(1)
    output = [pre[i] * post[i] for i in range(len(nums))]
    return output

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    output = productExceptSelf(nums)
    print(output)
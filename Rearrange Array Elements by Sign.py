def rearrangeArray(nums):
    def isPositive(num):
        if num >= 0:
            return True
        return False
    positive = []
    negative = []
    for num in nums:
        if isPositive(num):
            positive.append(num)
        else:
            negative.append(num)
    return [item for pair in zip(positive, negative) for item in pair]


if __name__ == "__main__":
    nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
    output = rearrangeArray(nums)
    print(output)
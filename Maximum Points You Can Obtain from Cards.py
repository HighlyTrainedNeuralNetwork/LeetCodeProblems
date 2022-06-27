# Initial solution based on repurposing Predict the Winner problem solution
# was too slow. I looked at answers. Intended solution is a sliding window
# that relies on tracking of previous sums in some capacity.
def maxScore(cardPoints, k):
    memo = {}
    def looper(points, left, right, selections):
        if (left, right, selections) in memo.keys():
            return memo[(left, right, selections)]
        if selections == 0:
            return 0
        score_1 = points[0] + looper(points[1:], left + 1, right, selections - 1)
        score_2 = points[-1] + looper(points[:-1], left, right - 1, selections - 1)
        memo[(left, right, selections)] = max(score_1, score_2)
        return max(score_1, score_2)
    return looper(cardPoints, 0, len(cardPoints) - 1, k)

def maxScore(cardPoints, k):
    out = sum(cardPoints)
    window_len = len(cardPoints) - k
    window_sum = sum(cardPoints[:window_len])
    for i in range(k + 1):
        if i != 0:
            window_sum += cardPoints[i + window_len - 1] - cardPoints[i - 1]
        out = min(out, window_sum)
    return sum(cardPoints) - out

cardPoints = [1,2,3,4,5,6,1]
k = 3
print(maxScore(cardPoints, k))
print(sum(cardPoints))
print(len(cardPoints))
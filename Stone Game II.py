# Common pattern in game problems appears to be minimizing the score of the opposing player

def stoneGameII(piles):
    memo = {}
    def looper(piles, M):
        if (tuple(piles), M) in memo.keys():
            return memo[(tuple(piles), M)]
        if len(piles) <= M * 2:
            return sum(piles)
        scores = []
        for i in range(1, (2 * M) + 1):
            score = looper(piles[i:], max(M, i))
            scores.append(score)
        memo[(tuple(piles), M)] = sum(piles) - min(scores)
        return sum(piles) - min(scores)
    return looper(piles, 1)

if __name__ == "__main__":
    piles = [1,2,3,4,5,100]
    output = stoneGameII(piles)
    print(output)

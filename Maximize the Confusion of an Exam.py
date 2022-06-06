# Initial solution relying on count() was too slow. this dynamic tracking via char_count_dict works
def maxConsecutiveAnswers(answerKey, k):
    left, right = 0, 0
    largest_window = 0
    char_count_dict = {"T": 0, "F": 0}
    while right < len(answerKey):
        char_count_dict[answerKey[right]] += 1
        if char_count_dict["T"] > k and char_count_dict["F"] > k:
            char_count_dict[answerKey[left]] -= 1
            left += 1
        else:
            largest_window = max(largest_window, right - left + 1)
        right += 1
    return largest_window

print(maxConsecutiveAnswers("TTFTTFTT", 1))
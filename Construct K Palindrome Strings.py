def canConstruct(s, k):
    count_dict = {}
    for char in s:
        if char in count_dict.keys():
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    odd_count = sum(count % 2 == 1 for count in count_dict.values())
    if odd_count <= k <= len(s):
        return True
    else:
        return False



s = "annabelle"
k = 2
print(canConstruct(s, k))
s = "leetcode"
k = 3
print(canConstruct(s, k))
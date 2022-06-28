def minimumDeletions(s):
    count_dict = {}
    for char in s:
        count_dict.setdefault(char, 0)
        count_dict[char] += 1
    seen = []
    deletions = 0
    for i in count_dict.values():
        if i in seen:
            while i in seen and i > 0:
                i -= 1
                deletions += 1
        seen.append(i)
    return deletions

s = "accdcdadddbaadbc"
print(minimumDeletions(s))
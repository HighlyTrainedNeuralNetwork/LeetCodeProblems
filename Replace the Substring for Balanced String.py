def balancedString(s):
    countDict = {}
    patternCountDict = {}
    for char in s:
        if char in countDict.keys():
            countDict[char] += 1
        else:
            countDict[char] = 1
    for char in countDict.keys():
        if countDict[char] > len(s) / 4:
            patternCountDict[char] = countDict[char] - len(s) // 4
    smallest_window = len(s)
    left = 0
    right = 0
    while right < len(s):
        right += 1
        considered_window = s[left: right]
        if all(considered_window.count(char) >= patternCountDict[char] for char in patternCountDict.keys()):
            smallest_window = min(smallest_window, len(considered_window))
            while left <= right:
                left += 1
                considered_window = s[left: right]
                if all(considered_window.count(char) >= patternCountDict[char] for char in patternCountDict.keys()):
                    smallest_window = min(smallest_window, len(considered_window))
                else:
                    left -= 1
                    break
    return smallest_window




# balancedString("QQWE")
balancedString("WWEQERQWQWWRWWERQWEQ")
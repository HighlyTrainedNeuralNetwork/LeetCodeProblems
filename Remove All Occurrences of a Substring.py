def removeOccurrences(s, part):
    l = 0
    part_length = len(part)
    while l <= len(s) - part_length and s:
        window = s[l:l + part_length]
        if s[l:l + part_length] == part:
            s = s[:l] + s[l + part_length:]
            l = max(0, l - len(part))
        else:
            l += 1
    return s


s = "axxxxyyyyb"
part = "xy"
print(removeOccurrences(s, part))
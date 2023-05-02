def isMatch(s, p):
    s_pointer, p_pointer = 0, 0
    star_pointer, matched_s = -1, 0

    while s_pointer < len(s):
        if p_pointer < len(p) and (s[s_pointer] == p[p_pointer] or p[p_pointer] == "?"):
            s_pointer += 1
            p_pointer += 1
        # the default assumption is that * corresponds to an empty string
        elif p_pointer < len(p) and p[p_pointer] == "*":
            star_pointer = p_pointer
            matched_s = s_pointer
            p_pointer += 1
        elif star_pointer != -1:
            p_pointer = star_pointer + 1
            matched_s += 1
            s_pointer = matched_s
        else:
            return False

    while p_pointer < len(p) and p[p_pointer] == "*":
        p_pointer += 1

    return p_pointer == len(p)

if __name__ == "__main__":
    s = "adceb"
    p = "*a*b"
    output = isMatch(s, p)
    print(output)

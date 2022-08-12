# Initial recursive metho covering all combinations was too slow. Intended solution seems to rely on stacks and
# additional logic.


def removeKdigits(num, k):
    vals = []
    def getSmallestRemovalCombination(val, removals):
        if removals == 0:
            return True
        for i in range(len(val)):
            temp = val[:i] + val[i + 1:]
            vals.append(int(temp))
            getSmallestRemovalCombination(temp, removals - 1)
        return True
    getSmallestRemovalCombination(num, k)
    return min(vals)

def removeKdigits(num, k):
    stack = []
    for i in num:
        while stack and k and stack[-1] > i:
            stack.pop()
            k -= 1
        stack.append(i)
    if k > 0:
        stack = stack[:-k]
    return "".join(stack).lstrip("0") or "0"

num = "1432219"
k = 3
print(removeKdigits(num, k))
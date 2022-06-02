# This was too slow. I looked at solutions.
def removeDuplicates(s, k):
    def dig(string):
        for i in range(len(string[:-k + 1])):
            if string[i:i + k] == k * string[i]:
                print(string, string[:i] + string[i + k:])
                string = string[:i] + string[i + k:]
                return dig(string)
        return string
    print(dig(s))

def removeDuplicates(s, k):
    stack = [["placeholder", 0]]
    for char in s:
        if char == stack[-1][0]:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop(-1)
        else:
            stack.append([char, 1])
    print(''.join(char * count for char, count in stack))
# removeDuplicates("deeedbbcccbdaa", 3)
removeDuplicates("pbbcggttciiippooaais", 2)
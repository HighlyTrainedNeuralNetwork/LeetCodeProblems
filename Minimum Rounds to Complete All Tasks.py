from collections import Counter

def minimumRounds(tasks):
    counter = Counter(tasks)
    rounds = 0
    for val in counter.keys():
        if counter[val] == 1:
            return -1
        else:
            remainder = counter[val] % 3
            if remainder == 1 or remainder == 2:
                rounds += counter[val] // 3 + 1
            elif remainder == 2:
                rounds += counter[val] // 3 + 2
            else:
                rounds += counter[val] // 3
    return rounds

if __name__ == "__main__":
    # tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
    # tasks = [66,66,63,61,63,63,64,66,66,65,66,65,61,67,68,66,62,67,61,64,66,60,69,66,65,68,63,60,67,62,68,60,66,64,60,60,60,62,66,64,63,65,60,69,63,68,68,69,68,61]
    tasks = [2,2,3,3,2,4,4,4,4,4]
    output = minimumRounds(tasks)
    print(output)
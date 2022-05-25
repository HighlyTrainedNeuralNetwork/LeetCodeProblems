# This is too slow. Accepted solutions seem to be easy "heap" data structure.

def eatenApples(apples, days):
    eaten = 0
    day = 0
    while sum(apples) > 0:
        day += 1
        for i, d in enumerate(days):
            if day > i + d:
                apples[i] = 0
        indexes = sorted(range(len(apples[:day])), key=lambda x: days[x] - apples[x])
        indexes = [index for index in indexes if apples[index] != 0]
        if len(indexes) > 0:
            eaten += 1
            apples[indexes[0]] -= 1
    return eaten

# eatenApples([1,2,3,5,2], [3,2,1,4,2])
# eatenApples([3,0,0,0,0,2], [3,0,0,0,0,2])
eatenApples([2,1,10], [2,10,1])
from math import sqrt
from math import trunc
def bestCoordinate(towers, radius):
    min_x = min(towers, key=lambda x: x[0])[0]
    max_x = max(towers, key=lambda x: x[0])[0]
    min_y = min(towers, key=lambda x: x[1])[1]
    max_y = max(towers, key=lambda x: x[1])[1]
    output = [0, [0, 0]]
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            signal = 0
            for tower in towers:
                distance = (sqrt((x - tower[0]) ** 2 + (y - tower[1]) ** 2))
                if distance <= radius:
                    signal += trunc(tower[2] / (1 + distance))
            if signal > output[0]:
                output[0] = signal
                output[1] = [x, y]
    print(output)
towers = [[32,36,27],[17,22,43],[8,11,41],[46,28,7],[22,4,35],[41,8,33],[32,29,4],[44,32,16],[33,20,16],[3,38,35],[17,47,23],[33,0,29],[29,19,6],[4,50,46],[19,47,6],[48,6,41],[20,26,35]]
radius = 4
bestCoordinate(towers, radius)
# Naive solution passes all test cases but possibly more efficient to consider all points in range to not double count

def countLatticePoints(circles):
    points = set()
    for circle in circles:
        for x in range(circle[0] - circle[2], circle[0] + circle[2] + 1):
            for y in range(circle[1] - circle[2], circle[1] + circle[2] + 1):
                distance = ((x - circle[0]) ** 2 + (y - circle[1]) ** 2) ** 0.5
                if distance <= circle[2]:
                    points.add((x, y))
    return len(points)



if __name__ == "__main__":
    circles = [[2,2,1]]
    output = countLatticePoints(circles)
    print(output)
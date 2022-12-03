def checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2):
    closestX = min(range(x1, x2 + 1), key=lambda x: abs(xCenter - x))
    closestY = min(range(y1, y2 + 1), key=lambda x: abs(yCenter - x))
    distance = ((closestX - xCenter) ** 2 + (closestY - yCenter) ** 2) ** 0.5
    if distance <= radius or (xCenter in range(x1, x2) and yCenter in range(y1, y1)):
        return True
    return False
if __name__ == "__main__":
    radius, xCenter, yCenter, x1, y1, x2, y2 = 2, 102, 50, 0, 0, 100, 100
    output = checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)
    print(output)
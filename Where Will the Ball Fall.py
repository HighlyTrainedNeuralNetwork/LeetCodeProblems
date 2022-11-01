def findBall(grid):
    width = len(grid[0])
    height = len(grid)
    def determineFall(grid, location):
        print(location)
        if grid[location[0]][location[1]] == 1 and location[1] < width - 1 and grid[location[0]][location[1] + 1] != -1:
            location[1] += 1
        elif grid[location[0]][location[1]] == -1 and location[1] > 0 and grid[location[0]][location[1] - 1] != 1:
            location[1] -= 1
        else:
            return -1
        if location[0] == height - 1:
            return location[1]
        else:
            location[0] += 1
            return determineFall(grid, location)

    output = []
    for i in range(width):
        coords = [0, i]
        output.append(determineFall(grid, coords))
    return output


grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
print(findBall(grid))
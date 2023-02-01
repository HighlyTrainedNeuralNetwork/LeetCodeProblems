# Initial naive search solution was too slow
def updateMatrix(mat):
    def get_distance(x, y):
        queue = [(x, y)]
        visited = set()
        distance = 0
        while queue:
            distance += 1
            for i in range(len(queue)):
                local = queue.pop(0)
                localX = local[0]
                localY = local[1]
                if mat[localY][localX] == 0:
                    return distance - 1
                neighbours = [(localX - 1, localY), (localX + 1, localY), (localX, localY - 1), (localX, localY + 1)]
                for neighbour in neighbours:
                    if 0 <= neighbour[0] < len(mat[0]) and 0 <= neighbour[1] < len(mat) and neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)
    outputMat = []
    for y in range(len(mat)):
        outputMat.append([])
        for x in range(len(mat[0])):
            outputMat[y].append(get_distance(x, y))
    return outputMat

def updateMatrix(mat):
        queue = []
        for column in range(len(mat[0])):
            for row in range(len(mat)):
                if mat[row][column] == 0:
                    queue.append((column, row))
                else:
                    mat[row][column] = -1
        while queue:
            current = queue.pop(0)
            currentColumn = current[0]
            currentRow = current[1]
            neighbours = [(currentColumn + 1, currentRow), (currentColumn, currentRow + 1), (currentColumn - 1, currentRow),
                          (currentColumn, currentRow - 1)]
            for neighbour in neighbours:
                if 0 <= neighbour[1] < len(mat) and 0 <= neighbour[0] < len(mat[0]) and mat[neighbour[1]][neighbour[0]] == -1:
                    mat[neighbour[1]][neighbour[0]] = mat[currentRow][currentColumn] + 1
                    queue.append(neighbour)
        return mat

if __name__ == "__main__":
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    output = updateMatrix(mat)
    print(output)
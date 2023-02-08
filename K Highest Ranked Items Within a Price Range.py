def highestRankedKItems(grid, pricing, start, k):
    def get_neighbours(grid, node):
        row, col = node
        neighbours = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        valid = []
        for neighbour in neighbours:
            if 0 <= neighbour[0] < len(grid) and 0 <= neighbour[1] < len(grid[0]):
                val = grid[neighbour[0]][neighbour[1]]
                if val != 0:
                    valid.append(neighbour)
        return valid

    queue = [((start[0], start[1]), 0)]
    visited = set()
    output = []

    while queue:
        current, distance = queue.pop(0)
        if current not in visited:
            if grid[current[0]][current[1]] in range(pricing[0], pricing[1] + 1):
                output.append(([current[0], current[1]], distance))
            visited.add(current)
            neighbours = get_neighbours(grid, current)
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append((neighbour, distance + 1))
    output = sorted(output, key=lambda x: (x[1], grid[x[0][0]][x[0][1]], x[0][0], x[0][1]))[:k]
    return [out[0] for out in output]

if __name__ == "__main__":
    grid = [[57,54,48],
            [652,572,990],
            [632,199,306],
            [38,702,263],
            [431,0,507],
            [673,570,750],
            [316,141,639]]
    pricing = [475,745]
    start = [3, 2]
    k = 4
    output = highestRankedKItems(grid, pricing, start, k)
    print(output)
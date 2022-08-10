def maxAreaOfIsland(grid):
    covered = []
    islands = []
    ones = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col]]
    for one in ones:
        if one not in covered:
            islands.append(1)
            covered.append(one)
            candidate_vertices = [(one[0] - 1, one[1]), (one[0] + 1, one[1]), (one[0], one[1] - 1),
                                  (one[0], one[1] + 1)]
            vertices = [vertex for vertex in candidate_vertices if vertex in ones and vertex not in covered]
            while vertices:
                vertex = vertices.pop(0)
                islands[-1] += 1
                covered.append(vertex)
                sub_candidate_vertices = [(vertex[0] - 1, vertex[1]), (vertex[0] + 1, vertex[1]),
                                          (vertex[0], vertex[1] - 1),
                                          (vertex[0], vertex[1] + 1)]
                sub_vertices = [sub_vertex for sub_vertex in sub_candidate_vertices if (sub_vertex in ones)
                                and (sub_vertex not in covered) and (sub_vertex not in vertices)]
                vertices += sub_vertices
    return max(islands, default=0)

grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(maxAreaOfIsland(grid))

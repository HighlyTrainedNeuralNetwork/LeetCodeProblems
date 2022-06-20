def removeStones(stones):
    covered = []
    unique = 0
    for cur in stones:
        if cur not in covered:
            covered.append(cur)
            vertices = [stone for stone in stones if bool(stone[0] == cur[0]) ^ bool(stone[1] == cur[1])]
            while len(vertices) != 0:
                covered.append(vertices[0])
                sub_vertices = [stone for stone in stones if
                                bool(stone[0] == vertices[0][0]) ^ bool(stone[1] == vertices[0][1])
                                and stone not in covered and stone not in vertices]
                vertices.pop(0)
                vertices += sub_vertices
            unique += 1
    print(len(stones) - unique)

stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# stones = [[0,0]]
removeStones(stones)
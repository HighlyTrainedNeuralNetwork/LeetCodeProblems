# Initial solution that sorted a list of deltas was too slow. I looked at solutions. Solutions seem to require
# the use of a heap where the "sorting" process is more efficient.

import bisect
def furthestBuilding(heights, bricks, ladders):
    gaps = []
    for i in range(len(heights) - 1):
        if heights[i + 1] > heights[i]:
            print(heights[i], heights[i + 1], i)
            gaps.append(heights[i + 1] - heights[i])
            if sum(gaps) - sum(sorted(gaps, reverse=True)[:ladders]) > bricks:
                return i
    return len(heights) - 1

import heapq
def furthestBuilding(heights, bricks, ladders):
    jumps_heap = []
    for i in range(len(heights) - 1):
        delta = heights[i + 1] - heights[i]
        if delta > 0:
            heapq.heappush(jumps_heap, delta)
            if len(jumps_heap) > ladders:
                bricks -= heapq.heappop(jumps_heap)
                if bricks < 0:
                    return i
    return len(heights) - 1

heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2

print(furthestBuilding(heights, bricks, ladders))
# Naive solution of iterating though max time based on smallest trip time is too slow at o(n^2)
# Intended solution appears to be a binary search variation
def minimumTime(time, totalTrips):
    l = 1
    r = totalTrips * min(time)
    while l != r:
        c = (l + r) // 2
        finishedTrips = sum([c // t for t in time])
        if finishedTrips >= totalTrips:
            r = c
        else:
            l = c + 1
    return l


if __name__ == "__main__":
    time = [3, 3, 8]
    totalTrips = 6
    output = minimumTime(time, totalTrips)
    print(output)
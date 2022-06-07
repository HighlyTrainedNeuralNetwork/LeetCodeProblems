def minimumRefill(plants, capacityA, capacityB):
    # [currentCapacity, maxCapacity]
    a_list = [capacityA, capacityA]
    b_list = [capacityB, capacityB]
    refills = 0
    left, right = 0, len(plants) - 1
    while left <= right:
        if left != right:
            if plants[left] > a_list[0]:
                refills += 1
                a_list[0] = a_list[1] - plants[left]
            else:
                a_list[0] -= plants[left]
            if plants[right] > b_list[0]:
                refills += 1
                b_list[0] = b_list[1] - plants[right]
            else:
                b_list[0] -= plants[right]
        else:
            responsible_list = max([a_list, b_list], key=lambda x: x[0])
            if plants[left] > responsible_list[0]:
                refills += 1
        left += 1
        right -= 1
    return refills

print(minimumRefill([2,2,3,3], 3, 4))
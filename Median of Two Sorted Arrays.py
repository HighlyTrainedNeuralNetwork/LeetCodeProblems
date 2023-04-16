def findMedianSortedArrays(nums1, nums2):
    w1, w2 = 0, 0
    output = []
    while w1 < len(nums1) and w2 < len(nums2):
        if nums1[w1] <= nums2[w2]:
            output.append(nums1[w1])
            w1 += 1
        else:
            output.append(nums2[w2])
            w2 += 1
    output.extend(nums1[w1:])
    output.extend(nums2[w2:])
    return (output[(len(output) - 1) // 2] + output[len(output) // 2]) / 2

if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2, 4]
    output = findMedianSortedArrays(nums1, nums2)
    print(output)
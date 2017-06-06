# https://discuss.leetcode.com/topic/16797/very-concise-o-log-min-m-n-iterative-solution-with-detailed-explanation/2
import sys

def findMedianSortedArrays(nums1, nums2):
    N1, N2 = len(nums1), len(nums2)
    if N1 < N2:
        nums1, N1, nums2, N2 = nums2, N2, nums1, N1
    l, r = 0, N2*2
    while l <= r:
        j = (l + r) >> 1
        i = N1 + N2 - j
        L1 = -sys.maxint-1 if i == 0 else nums1[(i-1)>>1]
        L2 = -sys.maxint-1 if j == 0 else nums2[(j-1)>>1]
        R1 = sys.maxint if i == 2*N1 else nums1[i>>1]
        R2 = sys.maxint if j == 2*N2 else nums2[j>>1]
        if L1 > R2: 
            l = j + 1
        elif L2 > R1: 
            r = j - 1
        else:
            return (max(L1, L2) + min(R1, R2))/2.0

if __name__ == "__main__": 
    # nums1 = [1, 3]
    # nums2 = [2]
    # print findMedianSortedArrays(nums1, nums2)

    nums1 = [1, 2]
    nums2 = [3, 4]
    print findMedianSortedArrays(nums1, nums2)
    

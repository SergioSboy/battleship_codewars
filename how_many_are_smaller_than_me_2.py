# This is a hard version of How many are smaller than me?. If you have troubles solving this one, have a look at the easier kata first.
#
#
# function smaller(arr)
# that given an array arr, you have to return the amount of numbers that are smaller than arr[i] to the right.
#
# For example:
# smaller([5, 4, 3, 2, 1]) === [4, 3, 2, 1, 0]
# smaller([1, 2, 0]) === [1, 1, 0]
import bisect
def smaller(arr):
    n = len(arr)
    ans = []
    temp = []
    for i in range(n-1, -1, -1):
        c = bisect.bisect_left(temp, arr[i])
        ans.append(c)
        bisect.insort(temp,arr[i])
    return ans[::-1]
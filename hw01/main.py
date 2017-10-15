def bsearch(a, target): 
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        midVal = a[mid]
        if midVal < target:
            low = mid + 1
        elif midVal > target:
            high = mid - 1
        else:
            return mid
    return -1
data = [1,2,3,4,5]
pt = BinarySearch(data, 3)
print(pt)

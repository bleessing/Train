def left(arr, target):
    start, end = 0, len(arr) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        mid_value = arr[mid]
        if mid_value == target:
            result = mid
            end = mid - 1
        elif mid_value < target:
            start = mid + 1
        else:
            end = mid - 1
    return result
def right(arr, target):
    start, end = 0, len(arr) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        mid_value = arr[mid]
        if mid_value == target:
            result = mid
            start = mid + 1
        elif mid_value < target:
            start = mid + 1
        else:
            end = mid - 1
    return result

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

for target in queries:
    first = left(arr, target)
    last = right(arr, target)
    if first != -1 and last != -1:
        print(first + 1, last + 1)
    else:
        print(-1, -1)
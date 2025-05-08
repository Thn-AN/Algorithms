from typing import List, Tuple

def karatsuba(x: int, y: int) -> int:
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    half = n // 2

    high_x = x // 10**half
    low_x = x % 10**half
    high_y = y // 10**half
    low_y = y % 10**half

    a = karatsuba(high_x, high_y)
    b = karatsuba(low_x, low_y)
    c = karatsuba(high_x + low_x, high_y + low_y)

    z = c - a - b
    return a * 10**(2 * half) + z * 10**half + b

def merge(left: List[int], right: List[int]) -> List[int]:
    res = []
    i = j = 0
    n1, n2 = len(left), len(right)
    while i < n1 or j < n2:
        if j >= n2 or (i < n1 and left[i] <= right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res

def mergeSort(arr: List[int], lo: int, hi, int) -> List[int]:
    if lo >= hi:
        return arr[lo:hi+1]
    mid = (lo + hi) // 2
    left = mergeSort(arr, lo, mid)
    right = mergeSort(arr, mid + 1, hi)
    return merge(left, right)

def naievePartition(arr: List[int], lo: int, hi:int, pivot: int) -> int:
    left = []
    pivots = []
    right = []
    
    for i in range(lo, hi + 1):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] == pivot:
            pivots.append(arr[i])
        else:
            right.append(arr[i])
    arr[lo:hi + 1] = left + pivots + right
    return lo + len(left) + len(pivots) // 2

def hoarePartition(arr: List[int], lo: int, hi: int, p: int) -> int:
    arr[lo], arr[p] = arr[p], arr[lo]
    pivot = arr[lo]
    i = lo + 1
    j = hi
    
    while True:
        while i <= hi and arr[i] <= pivot:
            i += 1
        while j >= lo + 1 and arr[j] > pivot:
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]
    return j

def dutchFlag(arr: List[int], pivot: int) -> Tuple[int,int]:
    lo, mid, hi = 0, 0, len(arr)-1
    while mid <= hi:
        if arr[mid] < pivot:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == pivot:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
    return lo, mid

def countingSort(arr: List[int], u: int) -> None:
    n = len(arr)
    counter = [0] * u
    for i in range(n):
        counter[arr[i]] += 1
    pos = [0] * u
    for v in range(1, u):
        pos[v] = pos[v-1] + counter[v-1]

    temp = [0] * n
    for i in range(n):
        temp[pos[arr[i]]] = arr[i]
        pos[arr[i]] += 1
    for i in range(n):
        arr[i] = temp[i]

def getDigit(num: int, base: int, digit: int) -> int:
    return (num // (base ** (digit - 1))) % base

def radixPass(arr: list, base: int, digit: int) -> None:
    n = len(arr)
    counter = [0] * base
    for num in arr:
        counter[getDigit(num, base, digit)] += 1
    pos = [0]*base
    pos[0] = 1
    for i in range(1, base):
        pos[i] = pos[i-1] + counter[i-1]
    
    temp = [0] * n
    for num in arr:
        current = getDigit(num, base, digit)
        temp[pos[current] - 1] = num
        pos[current] += 1
    
    arr[:] = temp

def radixSort(arr: List, base: int, digits: int) -> None:
    for digit in range(1, digits + 1):
        radixPass(arr, base, digit)
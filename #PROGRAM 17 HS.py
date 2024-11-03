#PROGRAM 16 HS

def heapify(arr, n, i):
    large = i  
    l = 2 * i + 1   
    r = 2 * i + 2  
    if l < n and arr[l] > arr[large]:
        large = l
    if r < n and arr[r] > arr[large]:
        large = r
    if large != i:
        arr[i], arr[large] = arr[large], arr[i] 
        heapify(arr, n, large)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    A = list(map(int, file.readline().strip().split()))
heap_sort(A)
print(" ".join(map(str, A)))
    
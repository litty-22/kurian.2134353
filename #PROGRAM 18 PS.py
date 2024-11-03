#PROGRAM 18 PS

def k_smallest_elements(arr, k):
    arr.sort()
    return arr[:k]
with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    A = list(map(int, file.readline().strip().split()))
    k = int(file.readline().strip())
result = k_smallest_elements(A, k)
print(" ".join(map(str, result)))

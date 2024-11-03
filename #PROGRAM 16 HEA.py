def heapify(A, n, i):
    large = i 
    while True:
        l = 2 * large
        r = 2 * large + 1
        if l <= n and A[l - 1] > A[large - 1]:  
            large = l
        if r <= n and A[r - 1] > A[large - 1]: 
            large = r
        if large == i:
            break  
        A[i - 1], A[large - 1] = A[large - 1], A[i - 1]  
        i = large
def build_max_heap(A):
    n = len(A)
    for i in range(n // 2, 0, -1):
        heapify(A, n, i)
    return A

def main():
    import sys
    input_data = sys.stdin.read().strip().splitlines()
    n = int(input_data[0]) 
    A = list(map(int, input_data[1].split()))  
    max_heap = build_max_heap(A)
    print(' '.join(map(str, max_heap))) 
    
if __name__ == "__main__":
    main()

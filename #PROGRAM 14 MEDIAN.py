#PROGRAM 14 MEDIAN
import random
def quickselect(arr, l, r, k):
    if l == r: 
        return arr[l]
    pivot_ind = random.randint(l, r)
    pivot_val = arr[pivot_ind]
    arr[pivot_ind], arr[r] = arr[r], arr[pivot_ind]
    store_ind = l
    for i in range(l, r):
        if arr[i] < pivot_val:
            arr[store_ind], arr[i] = arr[i], arr[store_ind]
            store_ind += 1
    arr[store_ind], arr[r] = arr[r], arr[store_ind]
    if k == store_ind:
        return arr[store_ind]
    elif k < store_ind:
        return quickselect(arr, l, store_ind - 1, k)
    else:
        return quickselect(arr, store_ind + 1, r, k)

def read_input_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())  
        arr = list(map(int, file.readline().strip().split())) 
        k = int(file.readline().strip()) 
        return arr, k
def main():
    filename = 'input.txt' 
    arr, k = read_input_file(filename)
    result = quickselect(arr, 0, len(arr) - 1, k - 1)
    print(result)

if __name__ == "__main__":
    main()

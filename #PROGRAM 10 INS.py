#PROGRAM 10 INS
def insertion_sort_count(arr):
    swaps = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1  
        arr[j + 1] = key  
    return swaps, arr

def read_array(filename):
        with open(filename, 'r') as file:
            num_elements = int(file.readline().strip())
            array = list(map(int, file.readline().strip().split()))
            return array

def main():
    array = read_array('input.txt')
    if array:
        swaps, sorted_array = insertion_sort_count(array)
        print(swaps)
        
if __name__ == "__main__":
    main()

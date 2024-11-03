#PROGRAM 11 MER

def read_arrays_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_elements_A = int(lines[0].strip())
        array_A = list(map(int, lines[1].strip().split()))  
        num_elements_B = int(lines[2].strip())
        array_B = list(map(int, lines[3].strip().split()))  
        return array_A, array_B

def merge_sorted_arrays(A, B):
    merged_array = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merged_array.append(A[i])
            i += 1
        else:
            merged_array.append(B[j])
            j += 1
    merged_array.extend(A[i:])
    merged_array.extend(B[j:])
    return merged_array

def main():
    filename = 'input.txt'  
    array_A, array_B = read_arrays_from_file(filename)
    if array_A is not None and array_B is not None:
            merged_sorted = merge_sorted_arrays(array_A, array_B)
            print( ' '.join(map(str, merged_sorted)))
if __name__ == "__main__":
    main()

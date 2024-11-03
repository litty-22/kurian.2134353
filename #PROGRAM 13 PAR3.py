#PROGRAM 13 PAR3

def partition_array3(arr):
    pivot = arr[0]
    less_than = []
    equal_to = []
    greater_than = []
    for a in arr:
        if a < pivot:
            less_than.append(a)
        elif a == pivot:
            equal_to.append(a)
        else:
            greater_than.append(a)
    partitioned_array = less_than + equal_to + greater_than
    return partitioned_array

def read_array_from_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip()) 
        arr = list(map(int, file.readline().strip().split())) 
        return arr

def main():
    filename = 'input.txt' 
    arr = read_array_from_file(filename)
    output = partition_array3(arr)
    print("Output:", ' '.join(map(str, output)))

if __name__ == "__main__":
    main()
#PROGRAM 12 PAR
def partition_array(A):
    pivot = A[0] 
    less = []
    greater = []
    for a in A:
        if a < pivot:
            less.append(a)
        else:
            greater.append(a)
    return less + [pivot] + greater
def main():
    import sys
    input_data = sys.stdin.read().strip().splitlines()
    n = int(input_data[0])  
    A = list(map(int, input_data[1].split()))  
    output = partition_array(A)
    print(' '.join(map(str, output))) 

if __name__ == "__main__":
    main()
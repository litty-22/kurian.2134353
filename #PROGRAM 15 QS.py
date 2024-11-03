#PROGRAM 15 QS

def sort_array(n, A):
    A.sort()
    return A
with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    A = list(map(int, file.readline().strip().split()))
ascend_A = sort_array(n, A)
print(" ".join(map(str, ascend_A)))

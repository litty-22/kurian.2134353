#PROGRAM 5 FIB

def rabbit_pairs(n, k):
    F = [0] * (n + 1)
    
    # Base cases
    F[1] = 1 
    if n > 1:
        F[2] = 1  
    for m in range(3, n + 1):
        F[m] = F[m - 1] + k * F[m - 2]

    return F[n]
with open('input.txt', 'r') as file:
    line = file.readline()
    n,k = map(int, line.split())
result = rabbit_pairs(n, k)
print(result)

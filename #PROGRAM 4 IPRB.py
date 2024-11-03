#PROGRAM 4 IPRB
def probability_dominant(k, m, n):
    total = k + m + n
    total_pairs = total * (total - 1) / 2
    result = 0
    
    # AA x AA
    result += (k * (k - 1)) / 2
    
    # AA x Aa
    result += k * m
    
    # AA x aa
    result += k * n
    
    # Aa x Aa
    result += (m * (m - 1)) / 2 * 0.75  # 75% dominant
    
    # Aa x aa
    result += m * n * 0.5  # 50% dominant
    
    probability = result / total_pairs
    
    return round(probability, 5) 

with open('input.txt', 'r') as file:
    line = file.readline()
    k, m, n = map(int, line.split())
result = probability_dominant(k, m, n)
print(result)
def hamming_distance(s, t):
    distance = 0
    for char_s, char_t in zip(s, t):
        if char_s != char_t:
            distance += 1  
    return distance
def read_input_from_file(filename):
    with open(filename, 'r') as file:
        s = file.readline().strip()  
        t = file.readline().strip() 
    return s, t
if __name__ == "__main__":
    input_file = 'input.txt' 
    s, t = read_input_from_file(input_file)
    result = hamming_distance(s, t)
    print(result)


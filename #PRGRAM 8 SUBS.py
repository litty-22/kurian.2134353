def find_substring_locations(s, t):
    locations = []
    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            locations.append(i + 1)
    return locations

def read_input_from_file(filename):
    with open(filename, 'r') as file:
        s = file.readline().strip()  
        t = file.readline().strip()  
    return s, t

if __name__ == "__main__":
    input_file = 'input.txt' 
    s, t = read_input_from_file(input_file)
    result = find_substring_locations(s, t)
    print(' '.join(map(str, result)))

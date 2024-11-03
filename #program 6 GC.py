def gc_content(dna_string):
    g_count = dna_string.count('G')
    c_count = dna_string.count('C')
    total_count = len(dna_string)
    return (g_count + c_count) / total_count * 100 
def read_fasta(filename):
    with open(filename, 'r') as file:
        seq = {}
        cur_id = None
        cur_sequence = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if cur_id is not None:
                    seq[cur_id] = ''.join(cur_sequence)
                cur_id = line[1:]
                cur_sequence = []  
            else:
                cur_sequence.append(line) 
        if cur_id is not None:
            seq[cur_id] = ''.join(cur_sequence)  

    return seq

def main():
    filename = 'input.txt' 
    sequences = read_fasta(filename) 
    max_gc_id = None
    max_gc_value = 0
    for seq_id, dna in sequences.items():
        gc_value = gc_content(dna)
        if gc_value > max_gc_value:
            max_gc_value = gc_value
            max_gc_id = seq_id
    print(max_gc_id)
    print(f"{max_gc_value:.6f}") 
if __name__ == "__main__":
    main()


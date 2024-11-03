#PROGRAM 1 DNA
# Read DNA string from input
with open('input.txt') as f:
    dna_string = f.read().strip()

# Count nucleotides
a_count = dna_string.count('A')
t_count = dna_string.count('T')
c_count = dna_string.count('C')
g_count = dna_string.count('G')

# Print or save results
print(a_count, c_count, g_count, t_count)


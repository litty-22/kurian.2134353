#PROGRAM 3 REVC
with open('input.txt') as f:
   dna_string = f.read().strip()
def rev_string(dna_string):
    new_dna =""
    reversed_dna = dna_string[::-1]
    n=len(dna_string)
    for n in reversed_dna:
        if n =="A":
            new_dna += "T"
        elif  n =="G":
            new_dna += "C"
        elif n =="C":
            new_dna += "G"
        else:
            new_dna += "A"
        
    return(new_dna)
dna_string = rev_string(dna_string)
print(dna_string)
#PROGRAM 2 RNA
with open('input.txt') as f:
   rna_string = f.read().strip()
   def change_t2u(rna_string):
    new_rna_string = ""
    for a in rna_string:
        if a== "T":
            new_rna_string += "U"
        else:
            new_rna_string += a
            
    print(new_rna_string)

rna_string =change_t2u(rna_string)

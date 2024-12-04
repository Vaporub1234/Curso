#Encontrar el recuento de GC de una secuencia de ADN
dna = '''ATGTACTCATTCGTTTCGGAAGAGACAGGTACGTTAATAGTTAATAGCGTACTTCTTTTTCTTGCTTTCG
TGGTATTCTTGCTAGTTACACTAGCCATCCTTACTGCGCTTCGATTGTGTGCGTACTGCTGCAATATTGT
TAACGTGAGTCTTGTAAAACCTTCTTTTTACGTTTACTCTCGTGTTAAAAATCTGAATTCTTCTAGAGTT
CCTGATCTTCTGGTCTAA'''

#((g + c)/ total nucleotidos) * 100

g_count = dna.count("G")
c_count = dna.count("C")

total_gc = g_count + c_count
total_nuc = len(dna)

gc_percent = (total_gc / total_nuc)*100

print(f"El porcentaje de GC en su ADN es {round(gc_percent, 2)}%")

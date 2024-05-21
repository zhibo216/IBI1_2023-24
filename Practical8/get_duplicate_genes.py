import re
fasta_file_path = r"C:\Users\giggity\Desktop\2023-24 IBI1 notes\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all (1).fa"
genes_dict={}
names_dict={}
simplified_name=[]
with open(fasta_file_path, 'r',encoding='UTF-8') as fasta_file:
    for line in fasta_file:
        if line.startswith('>'):
            gene_name = line
            genes_dict[gene_name] = ""
            simplified_name.append(''.join(re.findall(r'gene:(.+?)\s',line)))
        else:
            genes_dict[gene_name] += line.strip()+'\n'
roll=0
with open(r"C:\Users\giggity\Desktop\2023-24 IBI1 notes\IBI1_2023-24\Practical8\duplicate_gene.fa",'w',encoding='UTF-8') as f1:
        for gene_name, gene_sequence in genes_dict.items():
            count = gene_name.count('duplication')
            if count !=0:
                f1.write('>'+str(simplified_name[roll])+'\n'+gene_sequence +'\n')
            roll=roll+1


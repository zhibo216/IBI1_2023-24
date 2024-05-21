a=input('the repetitive sequence:')
file_name=a+str('_duplicate_gene.fa')
import re
import os
os.chdir(r'C:\Users\giggity\Desktop\2023-24 IBI1 notes\IBI1_2023-24\Practical8')
def count(seq,x):  #count the number of an element in a sequence
    c=0
    b=len(seq)
    for i in range(b-len(x)+1):
        if seq[i:i+len(x)]==x:
            c+=1
    return(c)
name=[]
sequence={}
with open('duplicate_gene.fa', 'r',encoding='UTF-8') as fasta_file:
    for line in fasta_file:
        if line.startswith('>'):     #record the gene name
            gene_name=line.strip()
            name.append(gene_name)
            sequence[gene_name]=''
        else:
            sequence[gene_name]+=line.strip()
with open(file_name,'w',encoding='UTF-8') as output_file:
    for gene,sequence in sequence.items():
        Sequence=re.sub(r'\n','',sequence)
        rs=count(sequence,a) #repetitive sequence
        if rs!=0:
            output_file.write(f"{gene} (the repetitive number of the element:{rs})\n {Sequence}\n")
with open(file_name,'r',encoding='UTF-8') as f1:
       print(f1.read())

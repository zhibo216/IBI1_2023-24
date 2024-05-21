import blosum
import re
import os
blosum62 =blosum.BLOSUM(62)
os.chdir(r'C:\Users\giggity\Desktop\2023-24 IBI1 notes\IBI1_2023-24\Practical13')
human=open('SLC6A4_HUMAN.fa','r',encoding='UTF-8')
mouse=open('SLC6A4_MOUSE.fa','r',encoding='UTF-8')
rat=open('SLC6A4_RAT.fa','r',encoding='UTF-8')
def read(seq):
    seq=seq.read()
    x=re.sub(r'>.+?\n','',seq)
    y=re.sub(r'\n','',x)
    return y

human_seq=read(human)
mouse_seq=read(mouse)
rat_seq=read(rat)
def measure(seq1,seq2,blosum62):
    similarity=0
    score=0
    for i in range(len(seq1)):
        if seq1[i]==seq2[i]:
            similarity+=1
        score+=blosum62[seq1[i]][seq2[i]]
    similarity=similarity/len(seq1)
    print(str(similarity*100)+'%')
    print(score)

print('the similarity and score between humans and mouses are:')
measure(human_seq,mouse_seq,blosum62)
print('the similarity and score between humans and rats are:')
measure(human_seq,rat_seq,blosum62)
print('the similarity and score between mouses and rats are:')
measure(mouse_seq,rat_seq,blosum62)



            

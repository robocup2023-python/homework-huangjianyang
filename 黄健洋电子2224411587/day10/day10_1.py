with open('codon.txt','r') as f:
    file=f.readlines()
    codon={}
    for i in file:
        string=i.split()
        a=string[0]
        b=string[1]
        if a!='codon':
            codon[a]=b
    f.close()

def transcript(s):
    trans={'A':'U','C':'G','G':'C','T':'A'}
    v=''
    for i in s:
        v+=trans[i]
    return v

def translate(s):
    i=0
    while s[i:i+3]!='AUG' and i+3<=len(s):
        i+=1
    v=''
    while i+3<=len(s)and codon[s[i:i+3]]!='stop':
        v+=codon[s[i:i+3]]
        i+=3
    return v

with open('seq.fa','r') as f:
    file=f.readlines()
    seq_dict={}
    seq_dict[file[0][1:5]]=file[1][0:-1]
    seq_dict[file[2][1:5]]=file[3][0:-1]
    f.close()
protein_dict={}
for i in list(seq_dict.keys()):
    protein_dict[i]=translate(transcript(seq_dict[i]))
print(protein_dict)
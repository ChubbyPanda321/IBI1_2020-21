import re
def translate(seq):
    code_dict = {
    'ATA':'J', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'B', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Z',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'O', 'TAG':'U',
    'TGC':'C', 'TGT':'C', 'TGA':'X', 'TGG':'W',
    }
    ptseq = ''
    for codenum in range(0,len(seq),3):
        ptseq+=code_dict[seq[codenum:codenum+3]]
    return ptseq
locfile = input('This is a script to extract unknown DNA sequence for your original file and translate them into peptide sequence.\nYour original file path and name:')
try:
    with open(locfile) as allcdna:
        with open('unknown_protein.fa','w') as output:
            seq, getnextseq = '', False
            for line in allcdna:
                if line.startswith('>'):
                    getnextseq = False
                    if 'unknown function' in line:
                        if len(seq) != 0:
                            output.write(f'{name:20}'+str(len(seq))+'\n'+seq+'\n')
                        name = re.search(r'(?<=\bgene:)(\w|-)+', line).group()
                        seq,  getnextseq = '', True
                elif getnextseq:
                    seq += translate(line[:-1])
            output.write(f'{name:20}'+str(len(seq))+'\n'+seq)
    print('File successfuly generated!')
except FileNotFoundError:
    print('Please enter the right file path and name!')
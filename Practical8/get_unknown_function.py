import os
import re
os.chdir('D:\ZJU\IBI\python\IBI1_2020-21\Practical8')
allcdna = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
output = open('unknown_function.fa','w')
seqlinenum = 0
for line in allcdna:
    if line.startswith('>'):
        getnextseq = True
        if 'unknown function' in line:
            if seqlinenum != 0:
                length = len(seq) - seqlinenum
                output.write(f'{name:20}'+str(length)+'\n'+seq)
            name = re.search(r'(?<=\bgene:)\w+', line).group()
            seq, seqlinenum = '', 0
            getnextseq = False
    elif not getnextseq:
        seqlinenum += 1
        seq += line
output.write(f'{name:20}'+str(length)+'\n'+seq)
allcdna.close()
output.close()
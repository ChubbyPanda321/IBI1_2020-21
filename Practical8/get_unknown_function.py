import os
import re
os.chdir('D:\ZJU\IBI\python\IBI1_2020-21\Practical8')
allcdna = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
output = open('unknown_function.fa','w')
seq = ''
seqlinenum = 0
iwantit = False
getone = False
for line in allcdna:
    if line.startswith('>'):
        if 'unknown function' in line:
            name = re.search(r'(?<=\bgene:)(\w|-)+', line)
            iwantit = True
            getone = True
            seq = ''
            seqlinenum = 0
        elif getone and iwantit:
            iwantit = False
            length = len(seq)-seqlinenum
            output.write(f'{name.group():20}'+str(length)+'\n')
            output.write(seq)
    if iwantit:
        seqlinenum += 1
        seq += allcdna.readline()

allcdna.close()
output.close()
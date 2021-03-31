import os, re
os.chdir('D:\ZJU\IBI\python\IBI1_2020-21\Practical8')
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as allcdna:
    with open('unknown_function.fa','w') as output:
        seqlinenum = 0
        for line in allcdna:
            if line.startswith('>'):
                getnextseq = False
                if 'unknown function' in line:
                    if seqlinenum != 0:
                        output.write(f'{name:20}'+str(len(seq)-seqlinenum)+'\n'+seq)
                    name = re.search(r'(?<=\bgene:)\w+', line).group()
                    seq, seqlinenum, getnextseq = '', 0, True
            elif getnextseq:
                seqlinenum += 1
                seq += line
        output.write(f'{name:20}'+str(len(seq)-seqlinenum)+'\n'+seq)
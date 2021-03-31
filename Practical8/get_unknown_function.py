import os, re
os.chdir('D:\ZJU\IBI\python\IBI1_2020-21\Practical8')
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as allcdna:
    with open('unknown_function.fa','w') as output:
        seq = ''
        for line in allcdna:
            if line.startswith('>'):
                getnextseq = False
                if 'unknown function' in line:
                    if len(seq) != 0:
                        output.write(f'{name:20}'+str(len(seq))+'\n'+seq+'\n')
                    name = re.search(r'(?<=\bgene:)(\w|-)+', line).group()
                    seq,  getnextseq = '', True
            elif getnextseq:
                seq += line[:-1]
        output.write(f'{name:20}'+str(len(seq))+'\n'+seq)
import os
os.chdir(r'D:\ZJU\IBI\python\IBI1_2020-21\Practical11')

# make a dict of the matrix
with open('BLOSUM62.txt') as BLOSUM62:
    index = BLOSUM62.readline().split()
    rawdata = list(map(lambda x:x[1:].split(), BLOSUM62.readlines()))
BLOSUM62_dict = {}
for row_num in range(len(index)):
    for column_num in range(len(index)):
        BLOSUM62_dict[(index[row_num],index[column_num])] = int(rawdata[row_num][column_num])

# read the sequences
def readfa_oneseq(filehandle):
    return filehandle.readline().rstrip(), filehandle.readline().rstrip()
with open('RandomSeq.fa') as R:
    rand_name, rand_seq = readfa_oneseq(R)
with open('SOD2_human.fa') as H:
    hum_name, hum_seq = readfa_oneseq(H)
with open('SOD2_mouse.fa') as M:
    mou_name, mou_seq = readfa_oneseq(M)

# compare
def pairwisw_global_alignment(seq1,seq2):
    score = 0
    count = 0
    print_alignment = ''
    for aa1, aa2 in zip(seq1, seq2):
        score += BLOSUM62_dict[(aa1,aa2)]
        if aa1 == aa2:
            count += 1
            print_alignment += '|'
        else:
            print_alignment += ' '
    print('Sequence1:',seq1)
    print('Alignment:',print_alignment)
    print('Sequence2:',seq2)
    print(f'BLOSUM62 Score: {score:<10} Score per aa: {score/len(seq1):<10.2f} Percentage of identity aa: {count*100/len(seq1):.2f}% ')
        
pairwisw_global_alignment(hum_seq, mou_seq)
pairwisw_global_alignment(hum_seq, rand_seq)
pairwisw_global_alignment(mou_seq, rand_seq)

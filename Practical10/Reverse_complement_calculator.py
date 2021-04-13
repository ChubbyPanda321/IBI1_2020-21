def rev_compl(seq:str) -> str:
    '''
    This is a function that convert a DNA sequence to its reverse complement sequence.
    Upper case, lower case or a mix of both are Ok as input.
    The output will be unified as upper case.
    '''
    return seq.upper().replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]

# example
seq = 'ACcCaTtG'
rev_compl_seq = rev_compl(seq)
print(rev_compl_seq)

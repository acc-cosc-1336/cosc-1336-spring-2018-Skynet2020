def get_count_A_C_G_and_T_in_string(dna_string):
    '''
    Create a function named get_count_A_C_G_and_T_in_string with a parameter named dna_string.

    :param dna_string: a DNA string
    :return: the count of As, Cs, Gs, and Ts in the dna_string
    '''
    
    
    dna_string = dna_string.upper()
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0
    for i in dna_string:
        if i == 'A':
            count_A +=1
        elif  i == 'C':
            count_C += 1
        elif  i == 'G':
            count_G += 1
        elif  i == 'T':
            count_T += 1
   
    return count_A, count_C, count_G, count_T

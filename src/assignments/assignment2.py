


def faculty_evaluation_result(nev, rar, som, oft, voft, alw):
''' Write code to calculate faculty evaluation rating according to asssignment instructions

    :param nev: Never
    :param rar: Rarely
    :param som: Sometimes
    :param oft: Often
    :param voft: Very Often
    :param alw: Always
    :return: rating as a string
    '''
    total = nev + rar + som + oft + voft + alw
    nev_ratio = nev / total
    rar_ratio =  rar / total
    som_ratio = som / total
    oft_ratio = oft / total
    voft_ratio = voft / total
    alw_ratio = alw / total

    if alw_ratio + voft_ratio >= 0.9:
        return str("Excellent")
    elif alw_ratio + voft_ratio + oft_ratio >= 0.8:
        return str("Very Good")
    elif alw_ratio + voft_ratio + oft_ratio + som_ratio >= 0.7:
        return str("Good")
    elif alw_ratio + voft_ratio + oft_ratio + som_ratio + rar_ratio >= 0.6:
        return str("Needs Improvement")
    else:
        return str("Unacceptable")
        
  

def get_ratings(nev,rar,som, oft,voft, alw):
    '''
    Students aren't expected to know this material yet!
    '''
    ratings = []
    total = nev + rar + som + oft + voft + alw

    ratings.append(round(alw / total, 2))
    ratings.append(round(voft / total, 2))
    ratings.append(round(oft / total, 2))
    ratings.append(round(som / total, 2))
    ratings.append(round(rar / total, 2))
    ratings.append(round(nev / total, 2))

    return ratings
    

    

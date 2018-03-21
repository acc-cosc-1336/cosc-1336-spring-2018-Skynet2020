'''
Problem
For two strings s1 and s2 of equal length, the p-distance between them, denoted dp(s1,s2), is the
proportion of corresponding symbols that differ between s1 and s2.

For a general distance function d on n taxa s1,s2,…,sn (taxa are often represented by genetic strings),
 we may encode the distances between pairs of taxa via a distance matrix D in which Di,j=d(si,sj).

Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given
in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that
your answer is allowed an absolute error of 0.001.

Sample Dataset
[
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
]

Sample Output
0.00000 0.40000 0.10000 0.10000
0.40000 0.00000 0.40000 0.30000
0.10000 0.40000 0.00000 0.20000
0.10000 0.30000 0.20000 0.00000

'''
##    Pseudocode:
##    1) start
##    2) get a multi-dimensional list (as the argument)
##    3) read elements of the first sublist
##    4) compare the elements one-by-one to elements in each sublist
##    5) if the elements do not match, return 1
##    6) add returned 1s, and divide the sum by 10
##    7) print the result, in format of 1/100,000 ('.5f')
##    8) iterate the same action with each sublist
##    9) end

    
def get_p_distance_matrix(mtrx):
    i = 0
    p = 0
    g = 0
    t = 0
    h = 0
    value = 0
    list_1 =[]
    while g < len(mtrx):
        list_2 = []
        while p < len(mtrx[g]) and i < len(mtrx):
            for r in mtrx[g]:
                if r != mtrx[i][p]:
                    value+=1
                p+=1
            result = value/10
            list_2.append(result)
            p=0
            value = 0
            i+=1
        list_1.append(list_2)
        i=0    
        g+=1
    return list_1

def print_get_p_distance_matrix(result):
    t = 0
    h = 0
    while h < len(result[t]):
        while t < len(result):
            q_string = str(format(result[t][h], '.5f'))
            t+=1            
            print(q_string, end=' ')
        print()  
        h+=1
        t=0

#write import statements for homework 6 functions
from src.homework.homework6 import get_point_mutations
from src.homework.homework6 import get_dna_complement
from src.homework.homework6 import transcribe_dna_into_rna
from src.homework.homework6 import get_gc_content
#from homework6 import
#from homework6 import


def menu_options():
    print()
    print('1) Point Mutations')
    print('2) DNA Complement')
    print('3) DNA to RNA')
    print('4) GC Content')
    print('5) DNA motif')
    print('6) Most likely Ancestor')
    print('7) Exit')
    print()

def run_menu():

    option = -1

    while option != 7:
        menu_options()
        option = int(input("Enter menu choice: "))

        while option < 1 or option > 7:
            print("Valid menu range 1-7")
            option = int(input("Enter menu choice: "))

        if option == 1:
            handle_option_1()
        elif option == 2:
            handle_option_2()
        elif option == 3:
            handle_option_3()
        elif option == 4:
            handle_option_4()
        elif option == 5:
            handle_option_5()
        elif option == 6:
            handle_option_6()


def handle_option_1():
    '''
    Write code to:
    Loop as long as user wants to continue.
    Prompt user for two dna strings of length 10 with letter range A,C,G, and T only.  
    Call the function get_point_mutations and display the mutations to screen.
    Ask user if they want to continue.
    '''
    keep_going = 'y'
    while keep_going == 'y':
        DNA_string_1 = input('Enter a DNA-code using letters A, C, G and T: ')
        
        while len(DNA_string_1) != 10:
            DNA_string_1 = input('Enter a DNA-code using letters A, C, G and T: ')
        
        DNA_string_2 = input('Enter another DNA-code using the same letters: ')
        
        while len(DNA_string_2) != 10:
            DNA_string_2 = input('Enter another DNA-code using the same letters: ')
        
        mutations = get_point_mutations(DNA_string_1, DNA_string_2)
        print(mutations)
        keep_going = input('Do you want to continue? Y/N: ')

def handle_option_2():
    '''
    Write code to read the file dna_complement.dat.
    For each line string call the function get_dna_complment and display the complement to screen.
    '''    
    file_object = open('dna_complement.dat', 'r')
    for line in file_object:
        string_read = line.rstrip('\n')
        print('Original DNA string: ', '\t', string_read)
        get_DNA = get_dna_complement(string_read)
        print('DNA complement string: ', get_DNA)
        print()
        

def handle_option_3():
    '''
    Write the code to read the file transcribe_dna_to_rna.dat.
    For each line string call the function transcribe_dna_to_rna and display rna to screen.
    '''
    file_object = open('transcribe_dna_to_rna.dat', 'r')
    for line in file_object:
        string_read = line.rstrip('\n')
        print('DNA string: ', string_read)
        RNA = transcribe_dna_into_rna(string_read)
        print('RNA string: ', RNA)
        print()

def handle_option_4():
    '''
    Write code to read the file compute_gc_content.dat and for each line
    call the get_gc_content function with the line string as an argument.
    Display the gc_content for each line.
    '''
    file_object = open('compute_gc_content.dat', 'r')
    for line in file_object:
        string_read = line.rstrip('\n')
        gc_content = get_gc_content(string_read)
        print(format(gc_content, ".5f"))
        
def handle_option_5():
    pass #optional 

def handle_option_6():
    pass #optional

'''
Created on Jul 25, 2016

@author: huangww
'''

def single_print(symb):
    print symb

def row_print():
    print '+ - - - -',

def posts_print():
    print '|        ',

def print_grid(counts):
    for t in range(counts):
        row_print()
    
    single_print('+')
    
    for t in range(counts * 4):
        posts_print()
        #print t
        if ((t + 1) % counts == 0):
            single_print('|')
        
def print_grids(counts):
    t = counts
    while (t != 0):
        print_grid(counts)
        t = t - 1
    
    for t in range(counts):
        row_print()
    single_print('+')
    
print_grids(11)
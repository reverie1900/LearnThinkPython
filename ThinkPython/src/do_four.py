'''
Created on Jul 25, 2016

@author: huangww
'''

def print_spam():
    print "spam"

def do_twice(content):
    content()
    content()

def do_four(content):
    do_twice(content)
    do_twice(content)

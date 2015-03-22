#!/bin/python3
""" Add prefix to all latex labels in a given file """

import sys

def add_prefix(prefix, filename):
    """ Add prefix to all latex labels in a given file """
    print("Adding prefix", prefix, "to all labels of file", filename)

def print_usage():
    """ Prints the parameters used to call the program """
    print("Usage:", sys.argv[0], "[PREFIX] [FILES]")

def main():
    """ Parses the command line parameters, calls the appropriate function """
    if len(sys.argv) < 3:
        print_usage()
    else:
        prefix = sys.argv[1]
        for filename in sys.argv[2:]:
            add_prefix(prefix, filename)

if __name__ == "__main__":
    main()

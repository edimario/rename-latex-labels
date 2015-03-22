#!/bin/python3
""" Add prefix to all latex labels in a given file """

import sys, re

def add_prefix(prefix, filename):
    """ Add prefix to all latex labels in a given file """
    print("Adding prefix", prefix, "to all labels of file", filename)
    with open(filename, 'r') as f_obj:
        text = f_obj.read()
    # print(text)
    labels = re.findall(r"(\\(?:label|ref)\{)(.*?)(\})", text)
    # print(labels)
    print("The following replacements will be made:")
    for match in labels:
        original = match[0] + match[1] + match[2]
        replaced = match[0] + prefix + ":" + match[1] + match[2]
        print(original, "\t->\t", replaced)
    do_replacement = input("Type y to continue with replacement\n")
    if do_replacement == "y":
        replaced = re.sub(r"(\\(?:label|ref)\{)(.*?)(\})", r"\1" + prefix + r":\2\3",text)
        with open(filename, 'w') as f_obj:
            f_obj.write(replaced)
        print("Replacement done!")            
    else:
        print("Replacement aborted!")

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

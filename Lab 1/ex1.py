#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Simple file read in/out
# Student Name: Aw Yong Jia Min Kellie
# Student ID: 1005466


# Import libraries
import sys
import argparse
import string

def encrypt(text, key):
    ls = []
    if (key >= 1 and key <= len(string.printable) - 1):
        for character in text:
            new_char = string.printable[(string.printable.index(character) + key) % 100]
            ls.append(new_char)
        return ls
    else:
        print("Key error")

def decrypt(text, key):
    ls = []
    if (key >= 1 and key <= len(string.printable) - 1):
        for character in text:
            new_char = string.printable[(string.printable.index(character) - key) % 100]
            ls.append(new_char)
        return ls
    else:
        print("Key error")


def doStuff(filein, fileout, key, mode):
    if (mode != "e" and mode != "E" and mode != "d" and mode != "D"):
        print("Invalid mode. Please input 'e' for encrpyting or 'd' for decrypting.")
    
    else:
        # open file handles to both files
        fin = open(filein, mode="r", encoding="utf-8", newline="\n")  # read mode
        fin_b = open(filein, mode="rb")  # binary read mode
        fout = open(fileout, mode="w", encoding="utf-8", newline="\n")  # write mode
        fout_b = open(fileout, mode="wb")  # binary write mode
        c = fin.read()  # read in file into c as a str
        
        if (mode == "e" or mode == "E"):
            ls_result = encrypt(c, key)
            result = ''.join(str(i) for i in ls_result)
        elif (mode == "d" or mode == "D"):
            ls_result = decrypt(c, key)
            result = ''.join(str(i) for i in ls_result)

        # and write to fileout
        fout.write(result)

        # close all file streams
        fin.close()
        fin_b.close()
        fout.close()
        fout_b.close()

# our main function
if __name__ == "__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="filein", help="input file")
    parser.add_argument("-o", dest="fileout", help="output file")
    parser.add_argument("-k", dest = "key", type = int, help = "key")
    parser.add_argument("-m", dest = "mode", help = "encrypt or decrypt")

    # parse our arguments
    args = parser.parse_args()
    filein = args.filein
    fileout = args.fileout
    # key = int(args.key)
    key = args.key
    mode = args.mode

    # print(mode)
    # print(type(mode))
    doStuff(filein, fileout, key, mode)

    # all done
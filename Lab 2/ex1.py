# Lab 2 Part I Substituition Cipher
# Name: Aw Yong Jia Min Kellie
# Student ID: 1005466


import re
import string
import matplotlib.pyplot as plt
import argparse
import os

plt.xlabel('Characters')
plt.ylabel('Frequency')

def freq_analysis(text):
    text_char_dict = {}
    for char in text:
        if char not in text_char_dict:
            char_count = text.count(char)
            text_char_dict[str(char)] = char_count

    temp_dict = {}
    for i in sorted(text_char_dict):
        temp_dict[i] = text_char_dict[i]

    text_char_dict = temp_dict
    plt.bar(text_char_dict.keys(), text_char_dict.values(), width=0.3)
    plt.show()
    result = decrypt(text, text_char_dict)
    return result
    

def decrypt(text, dict):
    del dict[max(dict, key = dict.get)]
    # first try to replace the common letters with the letters that appear most frequently
    # ls_common_letters = ['e', 't', 'a', 'i', 'o', 'n', 's', 'h', 'r']
    # second try
    ls_common_letters = ['e', 't', 'i', 'a', 'o', 'n', 's', 'h', 'r']

    # result_1 = text.replace('U', 'e')
    # result_2 = result_1.replace('J', 't')
    # result_3 = result_2.replace('Y', 'a')

    for i in range(len(ls_common_letters)):
        max_char = max(dict, key = dict.get)
        result = text.replace(max_char, ls_common_letters[i])
        text = result
        del dict[max_char]
    
    result = text.replace('M', 'w')
    result1 = result.replace('V', 'f')
    result2 = result1.replace('B', 'l')
    result3 = result2.replace('W', 'g')
    result4 = result3.replace('L','v')
    result5 = result4.replace('T', 'd')
    result6 = result5.replace('K', 'u')
    result7 = result6.replace('O', 'y')
    result8 = result7.replace('S', 'c')
    result9 = result8.replace('R', 'b')
    result10 = result9.replace('C', 'm')
    result11 = result10.replace('F', 'p')
    result12 = result11.replace('A', 'k')
    result13 = result12.replace('N', 'x')
    result14 = result13.replace('Z', 'j')
    result15 = result14.replace('P', 'z')

    return result15

# main function
if __name__ == "__main__":
    # # set up the argument parser
    # parser = argparse.ArgumentParser()

    # # parse our arguments
    # args = parser.parse_args()
    # filein = args.filein
    # fileout = args.fileout

    fin = open('story_cipher.txt', "r")  # read mode
    fout = open('story.cipher.txt', "w")  # write mode
    content = fin.read()  # read in file into c as a str
    # print(freq_analysis(content))
    final_str = freq_analysis(content)
    fout.write(final_str)
    fin.close()
    fout.close()
    # decrypt(content)
    # print(content)

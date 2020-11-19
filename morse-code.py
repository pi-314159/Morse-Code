# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 02:08:02 2016

@author: π
"""

import re
import sys
import time
ISOTIMEFORMAT = '%Y-%m-%d %X'
print("\nThis program was made by PI on April 23, 2016. \n(c) 2016 PI. All rights reserved.")
print('\nAttention! If you want to translate Morse Code into English, \nplease add "^" in front of your Morse Code! \nIf you want to translate English into Morse Code, \nplease write down the text directly! \nAnd it will save a record of your translation automatically \nin a .txt file which called "Morse Code and English". \nPlease using "/" to replace space and " " replace distance between two letters. \nIf you want to quit this program, please enter "$$$$$".')
output = open('Morse Code and English.txt', 'w')
output.write('Hi, thanks for using this program! \nThis program was made by PI in April 23, 2016. \n(c) 2016 PI. All rights reserved.')
output.close()
zero = 0
while zero > -1:
    text = input("\nPlease enter your text here: ")
    if text == '$$$$$':
        sys.exit()
    elif text[0] == "^":
        txt = re.sub('[^ \-./]','',text)
        if len(txt) + 1 != len(text):
            print("Please check your text again!")
        else:
            txt = txt.split(' ')
            op = []
            tf = []
            for i3 in range(len(txt)):
                if txt[i3] in ['.-', '-...', '-.-.', '-..', '.', '..-.',  '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '/', '.----.', '.-.-.-', '---...', '--..--', '..--..', '-.--.-', '.--.-.', '-...-', '-....-', '-..-.', '.-..-.', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-.-', '...---...']:
                    tf.append("True")
                else:
                    tf.append("False")
            if "False" in tf:
                print('\n***Sorry, please check your text again!***')
            elif not "False" in tf:
                文本 = txt
                for i2 in range(len(txt)):
                    if txt[i2] == '.-':
                        op.append("A")
                    elif txt[i2] == '-...':
                        op.append("B")
                    elif txt[i2] == '-.-.':
                        op.append("C")
                    elif txt[i2] == '-..':
                        op.append("D")
                    elif txt[i2] == '.':
                        op.append("E")
                    elif txt[i2] == '..-.':
                        op.append("F")
                    elif txt[i2] == '--.':
                        op.append("G")
                    elif txt[i2] == '....':
                        op.append("H")
                    elif txt[i2] == '..':
                        op.append("I")
                    elif txt[i2] == '.---':
                        op.append("J")
                    elif txt[i2] == '-.-':
                        op.append("K")
                    elif txt[i2] == '.-..':
                        op.append("L")
                    elif txt[i2] == '--':
                        op.append("M")
                    elif txt[i2] == '-.':
                        op.append("N")
                    elif txt[i2] == '---':
                        op.append("O")
                    elif txt[i2] == '.--.':
                        op.append("P")
                    elif txt[i2] == '--.-':
                        op.append("Q")
                    elif txt[i2] == '.-.':
                        op.append("R")
                    elif txt[i2] == '...':
                        op.append("S")
                    elif txt[i2] == '-':
                        op.append("T")
                    elif txt[i2] == '..-':
                        op.append("U")
                    elif txt[i2] == '...-':
                        op.append("V")
                    elif txt[i2] == '.--':
                        op.append("W")
                    elif txt[i2] == '-..-':
                        op.append("X")
                    elif txt[i2] == '-.--':
                        op.append("Y")
                    elif txt[i2] == '--..':
                        op.append("Z")
                    elif txt[i2] == '...---...':
                        op.append("SOS")
                    elif txt[i2] == '.-.-':
                        op.append("\n   ")
                    elif txt[i2] == '-----':
                        op.append("0")
                    elif txt[i2] == '.----':
                        op.append("1")
                    elif txt[i2] == '..---':
                        op.append("2")
                    elif txt[i2] == '...--':
                        op.append("3")
                    elif txt[i2] == '....-':
                        op.append("4")
                    elif txt[i2] == '.....':
                        op.append("5")
                    elif txt[i2] == '-....':
                        op.append("6")
                    elif txt[i2] == '--...':
                        op.append("7")
                    elif txt[i2] == '---..':
                        op.append("8")
                    elif txt[i2] == '----.':
                        op.append("9")
                    elif txt[i2] == '/':
                        op.append(" ")
                    elif txt[i2] == '.----.':
                        op.append("'")
                    elif txt[i2] == '.-.-.-':
                        op.append('.')
                    elif txt[i2] == '---...':
                        op.append(":")
                    elif txt[i2] == '--..--':
                        op.append(",")
                    elif txt[i2] == '..--..':
                        op.append("?")
                    elif txt[i2] == '-.--.-':
                        op.append("(")
                    elif txt[i2] == '.--.-.':
                        op.append("@")
                    elif txt[i2] == '-...-':
                        op.append("=")
                    elif txt[i2] == '-....-':
                        op.append("-")
                    elif txt[i2] == '-..-.':
                        op.append("/")
                    elif txt[i2] == '.-..-.':
                        op.append('"')     
                op = ''.join(op)
                output = open('Morse Code and English.txt', 'a')
                output.write("\n\n\n{:} (GMT)" .format(time.strftime(ISOTIMEFORMAT, time.gmtime( time.time()))))
                output.write('\nMorse Code: \n    {:}' .format(文本))
                output.write('\nEnglish: \n    {:}' .format(op))
                output.close()
                print("***English:*** \n    ", op)
    else:
        TEXT = text
        text = text.lower()
        txt = re.sub('[^ \-,.():=?\'/"@a-z0-9]','',text)
        if len(txt) != len(text):
            print("\nPlease check your text again!")
        else:
            txt = '&'.join(txt)
            txt = txt.split('&')
            op = []
            for i2 in range(len(txt)):
                if txt[i2] == 'a':
                    op.append(".- ")
                elif txt[i2] == 'b':
                    op.append("-... ")
                elif txt[i2] == 'c':
                    op.append("-.-. ")
                elif txt[i2] == 'd':
                    op.append("-.. ")
                elif txt[i2] == 'e':
                    op.append(". ")
                elif txt[i2] == 'f':
                    op.append("..-. ")
                elif txt[i2] == 'g':
                    op.append("--. ")
                elif txt[i2] == 'h':
                    op.append(".... ")
                elif txt[i2] == 'i':
                    op.append(".. ")
                elif txt[i2] == 'j':
                    op.append(".--- ")
                elif txt[i2] == 'k':
                    op.append("-.- ")
                elif txt[i2] == 'l':
                    op.append(".-.. ")
                elif txt[i2] == 'm':
                    op.append("-- ")
                elif txt[i2] == 'n':
                    op.append("-. ")
                elif txt[i2] == 'o':
                    op.append("--- ")
                elif txt[i2] == 'p':
                    op.append(".--. ")
                elif txt[i2] == 'q':
                    op.append("--.- ")
                elif txt[i2] == 'r':
                    op.append(".-. ")
                elif txt[i2] == 's':
                    op.append("... ")
                elif txt[i2] == 't':
                    op.append("- ")
                elif txt[i2] == 'u':
                    op.append("..- ")
                elif txt[i2] == 'v':
                    op.append("...- ")
                elif txt[i2] == 'w':
                    op.append(".-- ")
                elif txt[i2] == 'x':
                    op.append("-..- ")
                elif txt[i2] == 'y':
                    op.append("-.-- ")
                elif txt[i2] == 'z':
                    op.append("--.. ")
                elif txt[i2] == '0':
                    op.append("----- ")
                elif txt[i2] == '1':
                    op.append(".---- ")
                elif txt[i2] == '2':
                    op.append("..--- ")
                elif txt[i2] == '3':
                    op.append("...-- ")
                elif txt[i2] == '4':
                    op.append("....- ")
                elif txt[i2] == '5':
                    op.append("..... ")
                elif txt[i2] == '6':
                    op.append("-.... ")
                elif txt[i2] == '7':
                    op.append("--... ")
                elif txt[i2] == '8':
                    op.append("---.. ")
                elif txt[i2] == '9':
                    op.append("----. ")
                elif txt[i2] == ' ':
                    op.append("/ ")
                elif txt[i2] == "'":
                    op.append(".----. ")
                elif txt[i2] == '-':
                    op.append("-....- ")
                elif txt[i2] == '/':
                    op.append("-..-. ")
                elif txt[i2] == '.':
                    op.append(".-.-.- ")
                elif txt[i2] == ',':
                    op.append("--..-- ")
                elif txt[i2] == '(':
                    op.append("-.--.- ")
                elif txt[i2] == ')':
                    op.append("-.--.- ")
                elif txt[i2] == '"':
                    op.append(".-..-. ")
                elif txt[i2] == ':':
                    op.append("---... ")
                elif txt[i2] == '?':
                    op.append("..--.. ")
                elif txt[i2] == '@':
                    op.append(".--.-. ")
                elif txt[i2] == '=':
                    op.append("-...- ")
            op = ''.join(op)
            output = open('Morse Code and English.txt', 'a')
            output.write("\n\n\n{:} (GMT)" .format(time.strftime(ISOTIMEFORMAT, time.gmtime( time.time()))))
            output.write('\nEnglish: \n    {:}' .format(TEXT))
            output.write('\nMorse Code: \n    {:}' .format(op))
            output.close()
            print('Morse Code: \n{:}' .format(op))
    zero = zero + 1

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:14:58 2016

@author: π
"""

import re
import sys
import platform
import time
print("\nThis program was made by PI in April 28, 2016. \n(c) 2016 PI. All rights reserved. \nIf you want to quit, please enter '$$$$$'.")
zero = 0
while zero > -1:
    text = input("\nPlease enter your Morse Code here: ")
    if text == '$$$$$':
        sys.exit()
    else:
        txt = re.sub('[^ \-./]','',text)
        mc = txt
        if len(txt) != len(text):
            print("Please check your Morse Code again!")
        else:
            txt = txt.split(' ')
            tf = []
            for i3 in range(len(txt)):
                if txt[i3] in ['.-', '-...', '-.-.', '-..', '.', '..-.',  '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '/', '.----.', '.-.-.-', '---...', '--..--', '..--..', '-.--.-', '.--.-.', '-...-', '-....-', '-..-.', '.-..-.', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-.-', '...---...']:
                    tf.append("True")
                else:
                    tf.append("False")
            if "False" in tf:
                print('\nSorry, please check your Morse Code again!')
            elif not "False" in tf:
                mc = '%'.join(mc)
                mc = mc.split('%')
                print(mc)
                for i4 in range(len(mc)):
                    platforms = platform.system()
                    if platforms == "Windows":
                        import winsound
                        if mc[i4] == ".":
                            winsound.Beep(4000, 200) 
                            time.sleep(0.5)
                        elif mc[i4] == '-':
                            winsound.Beep(4000, 1000)
                            time.sleep(0.36)
                        elif mc[i4] == ' ':
                            time.sleep(2.4)
                        elif mc[i4] == '/':
                            time.sleep(6)
                    elif platforms == "Darwin":
                        if mc[i4] == '.':
                            sys.stdout.write('\a')
                            sys.stdout.flush()
                            time.sleep(1)
                        elif mc[i4] == '-':
                            sys.stdout.write('\a')
                            sys.stdout.flush()
                            print(' ')
                            time.sleep(0.1)
                            sys.stdout.write('\a')
                            sys.stdout.flush()
                            print(' ')
                            time.sleep(0.1)
                            sys.stdout.write('\a')
                            sys.stdout.flush()
                            print(' ')       
                            time.sleep(0)
                            sys.stdout.write(' ')
                            sys.stdout.flush()
                            time.sleep(2)    
                        elif mc[i4] == ' ':
                            time.sleep(1.8)
                        elif mc[i4] == '/':
                            time.sleep(3.6)
    zero = zero + 1
                            
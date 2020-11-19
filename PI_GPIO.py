#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import RPi.GPIO as GPIO
import time
print("\nThis program was made by PI in October 19, 2018. \n(c) 2018 PI. All rights reserved. \nIf you want to quit, please enter '$$$$$'.")
GPIO_Port = int(input("Please enter the GPIO Port: "))
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
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(GPIO_Port, GPIO.OUT)
                for i4 in range(len(mc)):
                    if mc[i4] == ".":
                        GPIO.output(GPIO_Port, True)
                        time.sleep(0.5)
                        GPIO.output(GPIO_Port, False)
                        time.sleep(0.5)
                    elif mc[i4] == '-':
                        GPIO.output(GPIO_Port, True)
                        time.sleep(1.5)
                        GPIO.output(GPIO_Port, False)
                        time.sleep(0.5)
                    elif mc[i4] == ' ':
                        time.sleep(1)
                    elif mc[i4] == '/':
                        time.sleep(1)
                GPIO.cleanup()
    zero = zero + 1

from engi1020.arduino.api import *
from time import sleep
import caesar
import random

analogPin = analog_read(0)
passwords = ['aaa', 'cows', 'berry', 'decors']
shifters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = random.choice(shifters)
plaintext = random.choice(passwords)
turn = 0
rgb_lcd_colour(0, 0, 0)

while True:
    sleep(1)
    start = digital_read(6)
    if start:
        break
    else:
        print('You must press the button to begin the game')
if analogPin > 523:
    oled_print(plaintext)
    while turn < 3:
        print('Check the OLED screen for the orignal word and figure out the shift!')
        print(f'The encoded password is {caesar.encode(plaintext, key)}')
        keyGuess = int(input('What is the password shifted by?: '))
        if keyGuess == key:
            rgb_lcd_colour(0, 255, 0)
            buzzer_note(5, 450, 3)
            sleep(3)
            # turn rgb led green
            print('That is Correct!')
            break
        else:
            turn += 1
            # turn rgb led red
            rgb_lcd_colour(255, 0, 0)

            print(f"You have {3 - turn} turns left!")

else:
    ciphertext = caesar.encode(plaintext, key)
    print(f' The ciphertext is {ciphertext}')
    print(f'The key is {key}')
    while turn < 3:
        oled_print(caesar.decode(ciphertext, key))
        wordGuess = input('What is the original password?: ')
        if wordGuess == plaintext:
            rgb_lcd_colour(0, 255, 0)
            buzzer_note(5, 450, 3)
            sleep(3)
            # turn rgb led green
            print('That is Correct!')
            break
        else:
            turn += 1
            # turn rgb led red
            rgb_lcd_colour(255, 0, 0)
            print(f"You have {3 - turn} turns left!")

rgb_lcd_colour(0, 0, 0)

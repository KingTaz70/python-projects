####  pytrixgame1  #####

# print ("\n\nTHE PY.TRIX")



import time
import sys
import random
import os
# os.system("color")

def pytrix_game():

### typing effect ###

    def typingprint(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)

    def typinginput(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        value = input()  
        return value
####_____________________________________________________________________________________________
### Hadi Extra code ####

    def print_pause(text, character=''):
        end_color = "\033[0m"
        if character == "U":
            color = "\033[1;34;40m"
        elif character == "A":
            color = "\033[1;31;40m"
        elif character == "S":
            color = "\033[1;31;40m"
        elif character == "T":
            color = "\033[1;34;40m"
        elif character == "L":
            color = "\033[1;33;40m"
        elif character == "M":
            color = "\033[1;35;40m"
        else:
            color = "\033[1;32;40m"
        for character in text:
            sys.stdout.write(f'{color}{character}{end_color}')
            sys.stdout.flush()
            time.sleep(0.05)
        print()

    def respond(question, *args):
        print_pause(question)
        for arg in args:
            print_pause(arg)
        print_pause('Answer: ')
        return input().lower()

    def game_over():
        while True:
            answer = respond('You were captured by the agents. Restart level? Y/N?')
            if answer == 'y':
                act_one() #####
            elif answer == 'n':
                exit()


###______________________________________________________________________________________________
    typingprint ("\n\nTHE PY.TRIX\n\n")

    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
    print("あぁかさたなはまやゃらわがざつぬふあぁかさたなはまやゃらわがざだばぱぴぢじぎゐりむゆゅるぐずづぇえた")
    print("あぁかさたなはまやゃらわがざつぬふあぁかさたなはまやゃらわがざだばぱぴぢじぎゐりむゆゅるぐずづぇえた")
    print("001000100010100100101010110110110101101011000101001001010100101100100100101001001001000000000000000")
    print("110001010010100100101001001010001010010010100010101000100100101001001001001010010010100100101001001")
    print("100.===========================================================================================.100")
    print("101.                                                                                           .010")
    print("010.                                                                                           .010")
    print("101.                                                                                           .011")
    print("101.                                                                                           .011")
    print("010.                                                                                           .010")
    print("001.                                                                                           .000")
    print("110.                         いらっしゃいませ                                                  .001")
    print("100.                                                                                           .101")
    print("101.                         ENTER PYTRIX GAME [Y/N]                                           .010")
    print("100.                                                                                           .000")
    print("101.                         ゲームに参加しますか                                              .010")
    print("110.                                                                                           .001")
    print("100.                                                                                           .100")
    print("101.                                                                                           .010")
    print("010.                                                                                           .010")
    print("101.                                                                                           .011")
    print("000.                                                                                           .010")
    print("000.                                                                                           .010")
    print("001.===========================================================================================.000")
    print("110001010010100100101001001010001010010010100010101000100100101001001001001010010010100100101001001")
    print("100100101001010010010100101101010011111000101001001010010010010110101010101010101010101010101010100")
    print("Dream Team Software Development 2021 - Pytrix v1 ed1      なはじみうぅくすつぬふむゆゅるぐずづぶぷぺ")
    print("あぁかさたなはまやゃらわがざつぬふあぁかさたなはまやゃらわがざだばぱぴぢじぎゐりむゆゅるぐずづぇえた")


    typingprint ("\033[1;37;40m\n\nThe phone rings \n \nBRRRIIIING!........BRRRIIIING........!BRRRIIIING!........BRRRIIIING!\n\nBeads of sweat drip down your brow, as you are awoken from your persistent recurring nightmare...\n\nYou are disoriented\n\nThe gloomy still of the night is choking as your eyes open.\n\nNobody calls at this time of the night!\n\nThis had better be important!\n\n")

#_________________________________________________________________________________________________________________________________________
### enter your name ###

    def name():
        global first_name, surname, alias, title
        title = typinginput ("\n\033[1;37;40mTitle:?\n\n")
        title = title.capitalize
        first_name =typinginput ("\n\033[1;37;40mFirst name?\n\n")
        first_name = first_name.capitalize()
        surname =typinginput("\nSurname? \n\n")
        surname = surname.capitalize()
        print(f"\nName Confirmation {first_name.capitalize()} {surname.capitalize()} \n")
        alias = typinginput("\nAlias? \n\n")
        alias = alias.capitalize()
        typingprint(f"\nYou will be known as {alias.capitalize()}...\n\n\n\n\n\n\n\n\n")
        game_entry_graph()
        
#_______________________________________________________________________________________________________________________________________

    def game_entry_graph():
        print("あぁかさたなはまやゃらわがざつぬふあぁかさたなはまやゃらわがざだばぱぴぢじぎゐりむゆゅるぐずづぇえた")
        print("あぁかさたなはまやゃらわがざつぬふあぁかさたなはまやゃらわがざだばぱぴぢじぎゐりむゆゅるぐずづぇえた")
        print("001000100010100100101010110110110101101011000101001001010100101100100100101001001001000000000000000")
        print("110001010010100100101001001010001010010010100010101000100100101001001001001010010010100100101001001")
        print("100.===========================================================================================.100")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("001.===========================================================================================.000")
        print("110001010010100100101001001010001010010010100010101000100100101001001001001010010010100100101001001")
        print("100100101001010010010100101101010011111000101001001010010010010110101010101010101010101010101010100")
        print("Dream Team Software Development 2021 - Pytrix v1 ed1     なはじみうぅくすつぬふむゆゅるぐずづぶぷぺ")
        print("あぁかさたなはまやゃらわがざつぬふあぁかさたなはまやゃらわがざだばぱぴぢじぎゐりむゆゅるぐずづぇえた")
        act_one()
#______________________________________________________________________________________________________________________________________

#### Ttinity choices #####

    def act_one():
        print_pause('\n\nTime to work...\n')
        while True:
            answer = respond('Choices:\n ', 'a)  Get to work.\n', 'b)  Go back to sleep.\n')
            if answer == 'b':
                game_over()
            elif answer == 'a':
                print_pause(f"Your phone is ringing {first_name}. Answer it...\n")
                while True:
                    answer = respond('Choices:\n ', 'a) Ignore call.\n', 'b) Answer phone.\n')
                    if answer == 'a':
                        game_over()
                    elif answer == 'b':
                        print_pause(f"You hear that bang? Agents have just broken in. They’re after you {first_name}.. Do exactly as I say if you want to survive.\n", 'U')
                        while True:
                            answer = respond('Choices:\n ', 'a) Confront agents.\n', 'b) Hang up.\n', 'c) Who is this?\n')
                            if answer == 'a':
                                game_over()
                            elif answer == 'b':
                                game_over()
                            elif answer == 'c':
                                act_two()


    def act_two():
        print_pause('No time for that. They’re about to break in and head to your room. Leave your room and head to the bathroom opposite your bedroom. Get in and shut the door.', 'U')
        choices = ['a) Follow instructions and go to bathroom.\n', 'b) Don’t tell me what to do.\n', "c) I’ll just call the police.\n"]
        while True:
            answer = respond('Choices:\n ', *choices)
            if answer == 'b' and 'b) Don’t tell me what to do.' in choices:
                print_pause('If you want to live, be quiet and listen.', 'U')
                choices = ['a) Follow instructions and go to bathroom.', "c) I’ll just call the police."]
            elif answer == 'c' and "c) I’ll just call the police." in choices:
                print_pause(f"I’m afraid I’m your only hope {first_name}.", 'U')
                choices = ['a) Follow instructions and go to bathroom.', 'b) Don’t tell me what to do.']
            elif answer == 'a':
                print_pause('Now open the cistern. There’s a box inside. Open it.', 'U')
                choices = ['\na) Open box.\n', 'b) Flush toilet.\n', "c) Attempt to go down fire escape.\n"]
                while True:
                    answer = respond('\nChoices: ', *choices)
                    if answer == 'b':
                        print_pause('You made too much noise.')
                        game_over()
                    elif answer == 'c' and "c) Attempt to go down fire escape." in choices:
                        print_pause('Window won’t open.')
                        choices = ['\na) Open box.\n', 'b) Flush toilet.\n']
                    elif answer == 'a':
                        print_pause('Take the gun out and screw in the suppressor. Then aim the gun just below the towel hook on the back of the door.\n', 'U')
                        choices = ['\na) Aim gun at window.\n', 'b) Aim gun at door.\n', "c) Aim gun at self\n."]
                        while True:
                            answer = respond('\nChoices: ', *choices)
                            if answer == 'a' and 'a) Aim gun at window\n.' in choices:
                                print_pause(f'{first_name}, focus. Aim at the door.\n', 'U')
                                choices = ['\nb) Aim gun at door.', "c) Aim gun at self."]
                            elif answer == 'c':
                                print_pause('Sure you wanna do that? You’ll be putting our lives at risk.\n', 'U')
                                while True:
                                    answer = respond('\nChoices: ', 'Y/N')
                                    if answer == 'y':
                                        game_over()
                                    elif answer == 'n':
                                        choices = ['\na) Aim gun at window.\n', 'b) Aim gun at door\n.']
                                        break
                            elif answer == 'b':
                                act_three()


    def act_three():
        print_pause('Good. Hold your exact position. When I say, you need to pull the trigger twice. Get ready...\n', 'U')
        choices = ['\na) I’m ready...\n', 'b) I’m too scared.\n', "c) I don’t want any part of this.\n"]
        while True:
            answer = respond('\nChoices: ', *choices)
            if answer == 'b' and 'b) I’m too scared.\n' in choices:
                print_pause('Do you want to make it out of here alive or not?\n', 'U')
                choices = ['a) I’m ready...\n', "c) I don’t want any part of this\n."]
            elif answer == 'c' and "c) I don’t want any part of this." in choices:
                while True:
                    answer = respond('Are you sure you want to quit? Y/N')
                    if answer == 'y':
                        game_over()
                    elif answer == 'n':
                        choices = ['a) I’m ready...\n', 'b) I’m too scared.\n']
                        break
            elif answer == 'a':
                print_pause('Okay... Fire.\n', 'U')
                choices = ['\na) Fire one shot.\n', 'b) Fire two shots.\n', "c) Fire three shots.\n"]
                while True:
                    answer = respond('\nChoices: ', *choices)
                    if answer == 'a':
                        print_pause('An agent found you.')
                        game_over()
                    elif answer == 'c':
                        print_pause('An agent below heard bodies dropping.')
                        game_over()
                    elif answer == 'b':
                        print_pause('That’s it. Both agents are down.\n', 'U')
                        print_pause('Step out of the room you’re in. Ignore the bodies. Two agents left below. Head downstairs quietly and stand behind the couch.\nKeep the phone to your ear. When I tell you, drop to the ground.\n', 'U')
                        while True:
                            answer = respond('\nChoices: \n', 'a) Get in position.\n', 'b) Stay in the bathroom.\n')
                            if answer == 'b':
                                game_over()
                            elif answer == 'a':
                                final_act()
    
    
    def final_act():
        print_pause('Press a number on your phone’s keypad to tell me when you’re there.\n', 'U')
        respond('\nChoices: ', '\nEnter [ANY] key to tell the caller you’re stood behind the couch.\n')
        print_pause('We’ve found him!\n', 'A')
        print_pause('Drop!\n', 'U')
        while True:
            answer = respond('Choices:\n ', 'a) Stand still\n', 'b) Drop to ground\n', 'c) Fire weapon\n')
            if answer == 'a':
                print_pause('You were shot by agents.\n')
                game_over()
            elif answer == 'c':
                print_pause('Agents dodged your bullets and fired back successfully.\n')
                game_over()
            elif answer == 'b':
                print_pause('Agents are down. Were you hit?\n', 'U')
                while True:
                    answer = respond('\nChoices:\n ', 'a) What’s going on?\n', 'b) No but... You let them see me?\n')
                    if answer == 'a' or answer == 'b':
                        print_pause('I had to get the drop on them. Follow me. My bike’s outside.\n', 'U')
                        while True:
                            answer = respond('Respond a) Who are you?\n')
                            if answer == 'a':
                                print_pause('Wear this helmet. My name is Trinity.\n', 'U')
                                while True:
                                    answer = respond('\nChoices:\n ', 'a) Get on bike to finish level.\n')
                                    if answer == 'a':
                                        print_pause('Level One Completed.\n')
                                        print_pause('..............\n')
                                        morpheus()


#_______________________________________________________________________________________________________________________________________

### story block meeting with Morpheus ###

    def morpheus():

        typingprint ("\033[1;32;40m\n \n.........You are taken into a poorly lit room.\nThe overhead strip light flickers,\nYou see a figure sat facing toward you. He identifies himself as Morpheus.\n\n")

        typingprint ("\n\033[1;35;40mDo you want to know what it is? \nThe Pytrix is All Around Us.Even in this room .\n\nYou can feel it when you go to work, when you go to Church, when you pay your taxes.\nIt is the World that has been pulled over your eyes to blind you from the truth…\nUnfortunately, nobody can be told what the Pytrix  is ....\n\nYou have to see it for yourself.\nThis is your last chance\nAfter this there is no turning back......\nYou take the Blue Pill\nThe story ends you wake up in your bed and believe whatever you want to believe.\nYou take the Red Pill\nYou stay in Wonderland, And I’ll show you how deep the Rabbithole goes.\n\nRemember, All I’m Offering Is The TRUTH! Nothing More\n")

        typingprint ("\033[1;37;40m")
        enter_pytrix_func()

#__________________________________________________________________________________________________________________________________________________________
#### red or blue ###

    def enter_pytrix_func():
        enter_pytrix = typinginput (" \033[1;32;40m \nDo you want to know the truth? \n\n \033[1;31;40m [R - take the red pill and know the truth ?]\n\n \033[1;34;40m [B - take the blue pill and carry on ? ] \n\n \033[1;32;40m [?] \n\n")
        if enter_pytrix == "R" or enter_pytrix == "r" or enter_pytrix == "Red" or enter_pytrix == "red" or enter_pytrix == "RED":
            typingprint ("\nWelcome to the TRUTH!\n\n")
            pytrix_graph()   
        elif enter_pytrix == "B" or enter_pytrix == "b" or enter_pytrix == "Blue" or enter_pytrix == "blue" or enter_pytrix == "BLUE":
            typingprint ("You have chosen to remain a battery \n")
            enter_pytrix_func()
        else:
            typingprint ("If you find that question hard, you're in for a shock !..... why not try again? \n")
            enter_pytrix_func()


#_________________________________________________________________________________________________________________________________
    def pytrix_graph():
        print("\n\n\n\n\n\n\n\n\n\n")
        print("\033[1;32;40mあぁかさたなはまやゃらわがざつぬふあぁかさたなはまやゃらわがざだばぱぴぢじぎゐりむゆゅるぐずづぇえた")
        print("\033[1;32;40mあぁかさたなはまやゃらわがざつぬふあぁかさたなはまやゃらわがざだばぱぴぢじぎゐりむゆゅるぐずづぇえた")
        print("\033[1;32;40m001000100010100100101010110110110101101011000101001001010100101100100100101001001001000000000000000")
        print("\033[1;32;40m110001010010100100101001001010001010010010100010101000100100101001001001001010010010100100101001001")
        print("\033[1;32;40m100.===========================================================================================.100")
        print("\033[1;32;40m101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  ........ |  |..|  |..|  |  ........ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  00000000 |  |00|  |00|  |  00000000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  00 |  |  |00|  |00|  |  00 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  00 |  |  |0000O000|  |  00000000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  00 |  |  |00|  |00|  |  00 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  00 |  |  |00|  |00|  |  00000000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  .......  |..    ..|  |  |  ........ |  ......|  |  |...  | ..      ..|  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  0000000  |000  000 |  |  | 00000000 |  OOOOOO|  |  |OOO  |  00    00 |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  00 |  00 |  00 00  |  |  |  | 00 |  |  00 | 00  |  |000  |  | 00 00  |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  00 | 00  |  |00   |  |  |  |  00 |  |  00 00 |  |  |000  |  |  000|  |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  00000 |  |  |00   |  |  |  |  00 |  |  OOOO  |  |  |000  |  | 00000  |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  00 |  |  |  |00   |  |  |  |  00 |  |  00 OOO|  |  |000  |  |00   00 |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  00 |  |  |  |00|   000  |  |  00 |  |  00|  OOO |  |000  |  00|    00|  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("\033[1;32;40m101. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  .010")
        print("\033[1;32;40m001.===========================================================================================.000")
        print("\033[1;32;40m110001010010100100101001001010001010010010100010101000100100101001001001001010010010100100101001001")
        print("\033[1;32;40m100100101001010010010100101101010011111000101001001010010010010110101010101010101010101010101010100")
        print("\033[1;32;40mDream Team Software Development 2021 - Pytrix v1 ed1     なはじみうぅくすつぬふむゆゅるぐずづぶぷぺ")
        print("\033[1;32;40mあぁかさたなはまやゃらわがざつぬふあぁかさたなはまやゃらわがざだばぱぴぢじぎゐりむゆゅるぐずづぇえた")

        typingprint("\033[1;32;40m100100101001010010010100101101010011111000101001001010010010010110101010101010101010101010101")
        traing_graph()
#__________________________________________________________________________________________________________________________________
    def traing_graph():
        print("\n\n\n\n\n\n\n\n\n\n")
        print("\033[1;32;40mThe Pytrix §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
        print("\033[1;32;40m§§ぁかさたなはまやゃらわがざつぬふあぁかさたなはまやV1らわがざだばぱぴぢじぎゐりむゆゅるぐずえた§§")
        print("\033[1;32;40m§§ぁかさたなはまやゃらわがざつぬふあぁかさたなはまやゃらわがざだばぱぴぢじぎゐりむゆゅるづぇえた§§")
        print("\033[1;32;40m§§00100010001010010010101011011011010110101100010100100101010010110010010010100100100100000000000§§")
        print("\033[1;32;40m§§11000101001010010010100100101000101001001010001010100010010010100100100100101001001010010001001§§")
        print("\033[1;32;40m§§100.=======================================================================================.100§§")
        print("\033[1;32;40m§§101.101001101 11100101001010010010100100101001001010010101010100101001001001011100001111101.010§§")
        print("\033[1;32;40m§§010.010100101001010100101010100101-0101010=101010 01010101010101010101010101010101010101010.010§§")
        print("\033[1;32;40m§§101.010101-1010101010101010 101010101001010101010101010101001010101011010100010101 01010010.011§§")
        print("\033[1;32;40m§§010.010100101001010010010100100101010010100101001010010-10010100100100101010100100101001010.010§§")
        print("\033[1;32;40m§§001.010010010100100100-01010010111010110100100101001001010011001 01010010010100100101001001.000§§")
        print("\033[1;32;40m§§110.01010101010101010101010101010101010101010101010 0101010101010101=1010101010101001001101.101§§")
        print("\033[1;32;40m§§101.10                                                                        0101010101000.001§§")
        print("\033[1;32;40m§§100.01       TRAINING SEQUENCE INITIATED                                      01-00000- 0 0.100§§")
        print("\033[1;32;40m§§101.10                                                                        00100001000 1.010§§")
        print("\033[1;32;40m§§101.01       YOU MUST COMPLETE ALL LEVELS TO PROGRESS FURTHE                  1010010 10100.010§§")
        print("\033[1;32;40m§§101.01                                                                        0100110010010.010§§")
        print("\033[1;32;40m§§101.0100100109091010010010101010010010100 0§1001001000100 10010010010010 100100100100100101.010§§")
        print("\033[1;32;40m§§010.100010100100110 10100100101001001010 1001001010010010 010100 1010010010100101001010 010.010§§")
        print("\033[1;32;40m§§101.0100101 0100101001010101001 100100101101001 0010100100101001100101010 10010101000101000.011§§")
        print("\033[1;32;40m§§000.10000100101001 100100101001010100101 01101001010010101001001010010010100101 01101001001.010§§")
        print("\033[1;32;40m§§001.=======================================================================================.000§§")
        print("\033[1;32;40m§§11000101001100101001001010001010010010100010101000100100101001001001001010010010100100101101001§§")
        print("\033[1;32;40m§§10010011010010010100101101010011111000101001001010010010010110101010101010101010101010010101100§§")
        print("\033[1;32;40m§§Dream Team Software Development 2021 - Pytrix v1 ed1     なはじみうぅくすつぬふむゆゅ0るぐyぷぺ§§")
        print("\033[1;32;40m§§あぁかさたなはまやゃらわがざつぬふあぁかさたなはま やゃらわがざだばぱぴぢじぎゐりむぐずづ0ぇた§n§")
        print("§\033[1;32;40m§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
        choices_func()

#__________________________________________________________________________________________________________________________________
##### Training time ###

    def choices_func():
        typingprint ("\n\033[1;34;40mNow that you have joined us in Zion, you must complete basic training in our Secret Facility. You must complete ALL of the Levels to become Battle Ready. Make haste\n")

        training_choices = typinginput("\033[1;34;40mYou need to train to survive in the Py-trix. \n\nDo you want to start with \n\n[a] - Coding? \n\n[b] - Weapons training?\n\n[c] - Combat training?\n\n[d] - Quit \n\n[e] - I am ready \n\n")
        if training_choices.lower() == "a":
            typingprint("You're a nerd!\n\n")
            pymaster()
        elif training_choices.lower() == "b":
            typingprint("You're a shooter!\n\n")
            bulls_eye_func ()
        elif training_choices.lower() == "c":
            typingprint("You're a fighter!\n\n")
            combat_func()
        elif training_choices.lower() == "d":
            typingprint("So you want to quit?.... well that's not an option")
            choices_func()
        elif training_choices.lower() == "e":
            typingprint("You've mastered everything? Are you ready to face the biggest challenge?\n\n")
            between_training_and_doors() 
        else:
            choices_func()
    
#___________________________________________________________________________________________________________
### Pymaster ###

    def pymaster():
        print_pause('Morpheus!\n', 'T')
        print_pause('What is happening, Trinity?\n', 'M')
        print_pause('Sir, the machines are installing a programme to block us from the Matrix.\n', 'L')
        print_pause('We have to break it. Where is Neo?\n', 'M')
        print_pause('He’s on his way, sir. ETA 6 minutes.\n', 'L')
        print_pause('That’s too long.', 'T')
        print_pause('Damn, this thing’s coming in fast! \n', 'L')
        print_pause('Plug me in. If I can get past the agents and destroy their serv...\n', 'T')
        print_pause('Wait a minute... What’s this? A programming company?\n', 'L')
        print_pause('Oh no...', 'T')
        print_pause('We have been discovered.', 'M')
        print_pause('Huh?', 'L')
        print_pause('They made us believe they were unaware of our decoy institutions so they could use our own data to destroy us.\n', 'M')
        print_pause('Wait, what?\n', 'L')
        print_pause('Me and Morpheus set up a programming school in the Matrix to find recruits.\n', 'T')
        pymaster1()

    def pymaster1():
        print_pause(f"I’m assigning {first_name}).\n", 'M')
        print_pause('Morpheus, even if he worked on this programme, Neo’s the only one who can manipulate c...\n', 'T')
        print_pause('We just need a bend. This will be his knowledge test.\n', 'M')
        print_pause('Great idea, sir. A bend will delay the installation. Hey newbie, park your behind.\n', 'L')
        pymaster2()

    def pymaster2():
        print_pause(f"Okay {first_name} let’s see what you got.\n", 'L')
        print_pause('They’re deleting data from your programming system. The only way to slow the virus down is by refilling the missing code. Use every resource you have.\n', 'L')
        print_pause('Type in the missing data.')
        first_interaction()

    def first_interaction():
        while True:
            answer = respond('\nRespond: ', 'a) You mean I was working for you this whole time?\n', 'b) How dare you? I quit!\n')
            if answer == 'a':
                print_pause('Get over it\n', 'T')
                first_interaction
            elif answer == 'b':
                while True:
                    print_pause('You can’t quit, newbie! Not now!\n', 'L')
                    quit_game = respond('Exit Game? Y/N? ')
                    if quit_game == 'y':
                        print_pause('You failed to save the humans.\n Game over.\n')
                        pymaster()   ###  exit() ### ???
                    elif quit_game == 'n':
                        print_pause('Get over it\n', 'T')
                        second_interaction()
                    else:
                        print_pause('Invalid response.\n')
                        first_interaction()
            else:
                print_pause('Invalid response.\n')
                first_interaction()

    def second_interaction():
        choices = ['a) Use computer\n', 'b) Stare into space\n', 'c) Make a hot chocolate\n']
        while True:
            answer = respond('\nChal 2 Choices:', *choices)
            if answer == 'a':
                quiz()
            elif answer == 'b' and 'b) Stare into space\n' in choices:
                print_pause('Yo man wake up we need you!\n', 'L')
                choices = ['a) Use computer\n', 'c) Make a hot chocolate\n']
            elif answer == 'c' and 'c) Make a hot chocolate\n' in choices:
                print_pause(f"No time for that, SIT DOWN, {first_name}.\n", 'M')
                choices = ['a) Use computer\n', 'b) Stare into space\n']
            else:
                print_pause('You failed to save humanity. G.\n')
                pymaster()

    def quiz():
        while True:
            answer = respond('\nWhat programme were you using?', 'a) Python\n', 'b) CSS\n', 'c) HTML\n')
            if answer == 'a':
                while True:
                    answer = respond('Who designed it?', 'a) Bill Gates\n', 'b) Steve Irwin\n', 'c) Rossum\n')
                    if answer == 'c':
                        print_pause('The code is starting to bend, Sir.\n', 'L')
                        print_pause('Oh my G... They’ve hacked into our main server and are deleting personal files on Neo. Trinity, don’t you know these answers?\n', 'L')
                        print_pause('...\n', 'T')
                        print_pause(f"{first_name} can find the answer.\n", 'M')
                        
                        while True:
                            answer = respond('\nWhat is Neo’s height in metres?', 'a) 1.85\n', 'b) 1.86\n', 'c) 6"1\n')
                            if answer == 'b':
                                print_pause('Yes! There’s just one more!!!\n', 'L')
                                
                                while True:
                                    answer = respond('\nWho played morpheus in a spoof version?\n', 'a) Samuel L. Jackson\n', 'b) Eddie Griffin\n', 'c) Lawrence Fishburn\n')
                                    if answer == 'a':
                                        print_pause('Wrong try again.', 'L')
                                    elif answer == 'c':
                                        print_pause('No. Use your head.\n', 'L')
                                    elif answer == 'b':
                                        print_pause('He did it.\n', 'T')
                                        print_pause(f"Neo just arrived. You saved us {first_name}.\n", 'L')
                                        print_pause(f'Congratulations {first_name}.\n', 'M')
                                        
                                        print("Sellect your next training Module")
                                        choices_func() ### exit ???##
                                    else:
                                        print_pause('Invalid response.')
                                        quiz()
                                # break
                            elif answer == 'a':
                                print_pause('You were close. Hunt the answer!\n', 'L')
                                quiz()
                            elif answer == 'c':
                                print_pause('That didn’t work.\n', 'L')
                                quiz()
                            else:
                                print_pause('Invalid response.\n')
                                quiz()
            #         else:
            #             print_pause('Invalid response.\n')
            #             quiz()
                    
            # else:
            #     print_pause('Invalid response.\n')


#___________________________________________________________________________________________________________

### Bulls eye ###

    def bulls_eye_func():
        weapon_choice = typinginput ("\033[1;33;40m\nYou need to pick a gun, you have three to choose from \033[1;31;40m\n\n[1 - Pistol]\n\n[2 - Rifle]\n\n[3 - Tickle stick]\n\n[4 - Training complete]\n\n")
        if weapon_choice == "1":
            typingprint ("\n\033[1;33;40mLoad your Pistol\n")
            target_practice_1 ()
        elif weapon_choice == "2":
            typingprint ("\nLoad your Rifle\n")
            target_practice_2 ()
        elif weapon_choice == "3":
            typingprint ("\nGrab your Tickle Stick\n")
            tickle_stick ()
        elif weapon_choice == "4":
            typingprint ("Your training is complete, maybe there is hope")
            choices_func()
        else:
            bulls_eye_func()

#______________________________________________________________________________________________________________________________________
## Pistol Training / target practice 1 ###

    def target_practice_1(): 
        
        Pistol = typinginput ("\nYou will see three targets, take aim and fire at each one. Just hit [F] to fire\n")
        if Pistol.upper() == "F":
            Pistol_chance =random.randint(0, 100)
            if (Pistol_chance <= 30):
                typingprint ("You've got work to do")
                target_practice_1()
            elif (Pistol_chance >= 31) and (Pistol_chance <= 70):
                typingprint ("You're getting there, but keep training ")
                target_practice_1()
            elif (Pistol_chance >= 71) and (Pistol_chance <= 90):
                typingprint ("Amazing! Move on to the next weapon")
                bulls_eye_func()
        else:
            typingprint ("You need to actually PULL the trigger")
            target_practice_1()

#___________________________________________________________________________________________________________

## Rifle training target_practice_2 ## 

    def target_practice_2():
        Rifle = typinginput ("\033[1;34;40m\nSometimes you need something with a bit more firepower. Sellect a number between 1 and 9 to see if you can hit your target\n\n")
        if Rifle in ("1", "2", "5", "7", "9"):
            typingprint ("MISS! Try again")
            target_practice_2()
        elif Rifle in("3", "4", "6", "8"):
            typingprint ("GOOD shot, move on to next weapon")
            bulls_eye_func()
        else:
            target_practice_2()

#___________________________________________________________________________________________________________

##Tickle Stick##

    def tickle_stick():
        tickle = typinginput ("\nIf you have got that close to your enemy and you think this is an option, it really is ALL OVER! Select [Y] OR [N]\n\n")
        if tickle.upper == "Y":
            typingprint ("Oh well it was fun while it lasted")
            bulls_eye_func()  ## should this option take you out of the game? back to the name stage? ##
        elif tickle.upper == "N":
            typingprint ("A wise choice, lets get some training done")
            bulls_eye_func()
        else:
            bulls_eye_func()
        tickle_stick()
#___________________________________________________________________________________________________________
### Ninja ###    #####  alias needs to refer to "alias" that is generated in the name function ####

    
    def combat_func():
        
        morpheus_text = typinginput(f"\033[1;35;40mNow, hit me, if you can.\n\n[a] - Kick chest \n\n[b] - Kick legs\n\n[c] - Wait\n\n[d] - Lets move on\n\n")
        if morpheus_text == ("a"):
            typingprint("\nDo you believe that my being stronger or faster has anything to do with my muscles in this place? Hmm...\n\n")
            again_func()
        elif morpheus_text == ("b"):
            typingprint(f"\nGood {alias}. But your weakness is not your technique.\n\n")
            again_func()
        elif morpheus_text == ("c"):
            typingprint(f"\n\n{alias}, what are you waiting for? Hit me.\n\n")
            combat_func()
        elif morpheus_text == ("d"):
            typingprint(f"\n\n{alias}, You think your ready?")
            choices_func()  ### there was a bracket missing ##
        else:
            combat_func()

    def again_func():
        
        morpheus_again = typinginput(f"Come on. Again!\n\n[a] - Run up wall\n\n[b] - Quick hands\n\n[c] - Wait\n\n[d] - Return to weapons choice\n\n[d] - I'm good enough")
        if morpheus_again == ("a"):
            typingprint("Good. Adaptation, improvisation.\n\nOk. You are ready for the next stage.\n\n")
            again_func()
        elif morpheus_again == ("b"):
            typingprint("Good. Adaptation, improvisation.\n\nOk. You are ready for the next stage.\n\n")
            again_func()
        elif morpheus_again == ("c"):
            typingprint(f"{alias}, I'm trying to free your mind.\n\n")
            again_func()
        elif morpheus_again == ("d"):
            typingprint("So you think your good enough? OK then pick a different training sym")
            choices_func()
        else:
            typingprint(f"{alias}, I'm trying to free your mind.\n\n")
            again_func()
        

#___________________________________________________________________________________________________________

### Final challenge in Building speeking section###

    def between_training_and_doors():
        typingprint(f"\n\n\033[1;35;40mExcellent, {first_name}.  You have successfully completed training.\n\n")
        typingprint(f"\033[1;35;40mYou will now be known as {alias}; the new member of the resistance.\n\n")
        typingprint("\033[1;35;40mThere is however a pressing issue.\n\n")
        typingprint("\033[1;35;40mNeo has stopped the virus upload...etc.\n\n")
        typingprint("\033[1;35;40m........... But it is not enough to protect Zion.\n\n") # Morpheus
        typingprint("\033[1;34;40m\n\nHe’ll have to destroy their main server.\n\n") # Trinity
        typingprint("\033[1;35;40m\n\nPrecisely, Trinity. He will need our help.\n\n") # Morpheus
        typingprint("\033[1;33;40m\n\nHe’s there already but the building’s blocking his signal. He’ll need backup too.\n\n") # Link
        typingprint(f"\033[1;34;40m\n\nLink, plug me in with {alias}. If we find Neo, we find the server.. \n\nWe’ll back him up while he destroys it.\n\n") # Trinity
        typingprint(f"\033[1;33;40m\n\nAre you ready, {alias}?\n") # Link
        typingprint("\033[1;34;40m\n\nHe can handle it?\n") # Trinity
        typingprint("\033[1;35;40m\n\nLet’s go...\n\n") # Morpheus
        door_one()

#____________________________________________________________________________________________________________

    
    def door_one():
        choose = typinginput("\033[1;36;40m\nEach door leads you to a destination.\n\nI can only show you the doors. \n\nYou must choose which one to take.\n\na) The door on your left\n\nb) The door in front of you.\n\nc) The door to your right\n\n")
        if choose.upper() == "A" or choose.upper() == "B" or choose.upper() == "C":
            typingprint("\033[1;37;40m\nYou open the door slowly and you walk through...\n\nYou walk into a corridor where you see the same three doors.\n\n")
            door_two()
        else:
            typingprint("\nYou tried to open the window. Come back and try a door.\n\n")
        door_one()

    def door_two():
        choose = typinginput(f"\033[1;36;40mTry another door. {alias}. Press a) b) or (c\n\n")
        if choose.upper() == "A" or choose.upper() == "B" or choose.upper() == "C":
            typingprint(f"\n\033[1;37;40mThe door opens to a brick wall.\n\nYou have one more try, {alias}.\n\n")
            door_three()
        else:
            door_two()

    def door_three():
        choose = typinginput(f"\033[1;36;40mTry another door. {alias}. If we fail, Zion is finished. a), b) or c)\n\n")
        if choose.upper() == "A" or choose.upper() == "B" or choose.upper() == "C":
            typingprint(f"\n\033[1;37;40mThe door opens to a room.\n\nYou enter...\n\nThe door closes behind you and you hear a voice...\n\n")
            end_game() 
        else:
            door_three()
#___________________________________________________________________________________________________________
## end of game dialogue ##

    def end_game():
        print_pause('Wait….something’s wrong.\n', 'T')
        print_pause(f"{surname}.", 'S')
        print_pause(f"Smith!!!{alias}, I can’t move. They’ve got me!\n", 'T')
        print_pause('It seems your programs are not as sophisticated as you expected.\n', 'S')
        print_pause('We had your team believe you were to be recruited and trained to defeat us.\n', 'S')
        print_pause('When in fact, you were training to become us.\n', 'S')
        print_pause('You trying to help your precious anomaly destroy us is somewhat...amusing.\n', 'S')
        print_pause('We have guided him to a different location without the possibility of communication.\n', 'S')
        print_pause('No!\n', 'T')
        print_pause(f"We control the anomaly, just like we control you,{surname}\n", 'S')
        print_pause('You do not control your inconsequential programs because we control them.\n', 'S')
        print_pause(f"We have been watching you for a long time {surname}\n", 'S')
        print_pause('Destiny cannot be escaped.\n', 'S')
        print_pause('MORPHEUS!!! LINK!!!\n', 'T')
        print_pause('Your first mission was to lead your accomplice to us.\n', 'T')
        print_pause('Successfully completed, if may add.\n', 'S')
        print_pause('You are a valuable asset, (title)(surname), and we are pleased to have you join us in achieving the inevitable destruction of our enemy.\n', 'S')
        print_pause('And now...it is time to...\n', 'S')
        print_pause('Neo?\n', 'T')
        typingprint("\033[1;32;40mThe Pytrix §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
        congratulations()
#___________________________________________________________________________________________________________

    def congratulations():
        print("\033[1;32;40mThe Pytrix §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
        print("\033[1;32;40m§§ぁかさたなはまやゃらわがざつかさたなはまやV1らFAIL!わがざだばぱぴぢじぎゐりむゆゅるぐずづぇえた§§")
        print("\033[1;32;40m§§ぁかさたなはまやゃらわがざ110110101101011000101001001010100101100100100101001001010000000000000§§")
        print("\033[1;32;40m§§11000101001010010010100010001010010010100010101000100100101001001001001010010010100100101001001§§")
        print("\033[1;32;40m§§100.=======================================================================================.100§§")
        print("\033[1;32;40m§§101.                                                                                       .010§§")
        print("\033[1;32;40m§§010.                                                                                       .010§§")
        print("\033[1;32;40m§§101.                                                                                       .011§§")
        print("\033[1;32;40m§§010.                                                                                       .010§§")
        print("\033[1;32;40m§§001.                       IMPORTANT MESSAGE                                               .000§§")
        print("\033[1;32;40m§§110.                                                                                       .101§§")
        print("\033[1;32;40m§§101.                       C O N G R A T U L A T I O N S !                                 .010§§")
        print("\033[1;32;40m§§100.                       You Have succeeded with This Mission                            .000§§")
        print("\033[1;32;40m§§101.                       あなたはこの使命で成功しました                                 .010§§")
        print("\033[1;32;40m§§110.                                                                                       .001§§")
        print("\033[1;32;40m§§100.                       Zion Lives to Fight Another Day                                .100§§")
        print("\033[1;32;40m§§101.                       シオンは別の日に戦うために生きています！                         .010§§")
        print("\033[1;32;40m§§101.                                                                                       .010§§")
        print("\033[1;32;40m§§101.                       Thank You For Your Efforts                                      .010§§")
        print("\033[1;32;40m§§101.                       頑張ってくれてありがとう                                          .010§§")
        print("\033[1;32;40m§§010.                                                                                       .010§§")
        print("\033[1;32;40m§§101.                                                                                       .011§§")
        print("\033[1;32;40m§§000.                                                                                       .010§§")
        print("\033[1;32;40m§§001.=======================================================================================.000§§")
        print("\033[1;32;40m§§11000101001010010010100100101010010010100010101000100100101001001001001010010010100100101001001§§")
        print("\033[1;32;40m§§10010010100101001001010010110011111000101001001010010010010110101010101010101010101010101010100§§")
        print("\033[1;32;40m§§Dream Team Software Development 2021 - Pytrix v1 ed1     なはじみうぅくすつぬゅるぐずづぶぷぺ§§§§")
        print("\033[1;32;40m§§§あぁかさたなはまやゃらわがざつぬふあぁかさたなはま やゃらわがざだばぱぎゐりむゆゅるぐずづぇた§§§")
        print("\033[1;32;40m§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
        name()
#___________________________________________________________________________________________________________
    # def play_game():
    #     print("\n")
    #     act_one()
    #     # act_two()
    #     # act_three()
    #     # final_act()

#__________________________________________________________________________________________________________

    # def play_game():
    #     print("\n")
    #     pymaster()
    #     first_interaction()
    #     pymaster1()
    #     second_interaction()
    #     pymaster2()
    #     quiz()
#__________________________________________________________________________________________________________
    
    print("\n")
    name()
    
    
pytrix_game()
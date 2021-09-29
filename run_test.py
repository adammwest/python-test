import os
import time
import sys
import answers
import practical2 as practical

DELAY_PRINT = True
SHOW_BREAKDOWN = True
CHARACTER_DELAY_SECS= 0.07


def delay_print(text):
    global CHARACTER_DELAY_SECS

    if DELAY_PRINT:
        for char in text:
            print(char,end='',flush=sys.stdout)
            time.sleep(CHARACTER_DELAY_SECS)
    else:
        print(text)

def get_yn(text):
    while True:
        delay_print(text)
        inp = input()
        inp = inp.lower()

        if inp == 'y':
            return True

        if inp == 'n':
            return False

def clear_screen():
    os.system('cls')

def pre_checks():
    files_expected = ['answers.py','knowlage.py','practical.py','task1.json','wordsearch.csv']
    files_in_dir = os.listdir(os.path.join(os.path.abspath(__file__),'../'))
    print('<Python Test> pre-checks ',end='')

    #check all files present
    if set(files_expected).issubset(set(files_in_dir)) == True:
        print('PASS')
    else:
        print('FAIL')
        sys.exit(3)

def run():
    global DELAY_PRINT
    global SHOW_BREAKDOWN

    delay_print('Hello Denis, maybe Janice?\nWelcome to Adam\'s test\nGood luck\n')
    
    if get_yn('Delayed text? (y/n) ') == False:
        DELAY_PRINT = False

    if get_yn('Show answer breakdown? (y/n) ') == False:
        SHOW_BREAKDOWN = False

    clear_screen()
    p1,p2,p3,p4,p5,p6,p7 = practical.run_test()

    P = answers.compare_practical_answers(SHOW_BREAKDOWN,p1,p2,p3,p4,p5,p6,p7)

    delay_print('Thats it!\nThanks :)')





if __name__ == "__main__":
    pre_checks()
    run()

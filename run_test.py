import os
import time
import sys
import knowlage
import practical
import answers

SKIP_CORRECT_QUESTIONS = True
DELAY_PRINT = False
CHARACTER_DELAY_SECS= 0.08


def delay_print(text):
    global CHARACTER_DELAY_SECS

    if DELAY_PRINT:
        for char in text:
            print(char,end='',flush=sys.stdout)
            time.sleep(CHARACTER_DELAY_SECS)
    else:
        print(text)

def pre_checks():
    print('<python-test> pre-checks ',end='')
    print('PASS')

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

def run():
    global DELAY_PRINT
    global SKIP_CORRECT_QUESTIONS
    delay_print('hello denis, maybe janice?\nwelcome to adams test\nthere will be 2 sections\n1. knowlage section\n2. practical section\n')
    
    if not get_yn('delayed text? (y/n) '):
        DELAY_PRINT = False

    if not get_yn('skip correct questions when restarting? (y/n) '):
        SKIP_CORRECT_QUESTIONS = True

    clear_screen()
    delay_print('Python-test\n')


    knowlage_answers = knowlage.run_test()
    practical_answers = practical.run_tests()

    A = answers.compare_knowlage_answers(knowlage_answers)
    B = answers.compare_practical_answers(practical_answers)

    answers.print_final_score(A,B)

    delay_print('Thats it!')
    if get_yn('try again? (y/n)  '):
        run()





if __name__ == "__main__":
    pre_checks()
    run()

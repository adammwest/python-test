import time
import sys
import knowlage
import practical
import answers

RM_CORRECT_QUESTIONS = True
DELAY_PRINT = True
CHARACTER_DELAY_SECS= 0.08


def delay_print(text,delay=CHARACTER_DELAY_SECS,use_delay=DELAY_PRINT):
    if use_delay:
        for char in text:
            print(char,end='',flush=sys.stdout)
            time.sleep(delay)
    else:
        print(text)

def pre_checks():
    print('prechecks... ',end='')
    print('PASS')

def get_yn(text):
    while True:
        inp = input(text)
        inp = inp.lower()

        if inp == 'y':
            return True

        if inp == 'n':
            return False

def run():
    delay_print('hello denis, maybe janice?\nwelcome to adams test\nthere will be 2 sections\n1. knowlage section\n2. practical section\n')
    
    if not get_yn('delayed text? (y/n)  '):
        DELAY_PRINT = False

    if not get_yn('remove correct questions when restarting? (y/n)  '):
        RM_CORRECT_QUESTIONS = True


    delay_print('we are now ready\n',use_delay=DELAY_PRINT)


    knowlage_answers = knowlage.run_test()
    practical_answers = practical.run_tests()

    A = answers.compare_knowlage_answers(knowlage_answers)
    B = answers.compare_knowlage_answers(practical_answers)

    answers.print_final_score(A,B)

    delay_print('Thats it!',use_delay=DELAY_PRINT)
    if get_yn('try again? (y/n)  '):
        run()





if __name__ == "__main__":
    pre_checks()
    run()

import random
import time

def question_genarator():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    oprator = ['+', '-', '*']
    c = random.choice(oprator)


    print(f'{a} {c} {b} = ?')

    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    else:
        return a * b
    
question_limit = 5
question = 0
score = 0
ok_time = 5

while question < question_limit:
    try:
        result = question_genarator()
        start_time = time.time()
        answer = int(input('Enter your answer: '))
        end_time = time.time()

        if end_time - start_time > ok_time:
            print('you are too late')
        else:
            if result == answer:    
                score += 1
                print('well done')
            else:
                print('you wrong!')
        question += 1
    except:
        print('You must send valid number')

print(f'your score is {score} out of {question_limit}')
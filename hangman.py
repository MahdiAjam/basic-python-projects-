import random

my_list = ['Mahdi', 'Zeinab', 'Zahra', 'Mohammad', 'Yasin', 'Ali', 'Maryam', 'Aylin', 'Shaghayegh']

computer_choice = random.choice(my_list).lower()
person_select = len(computer_choice)

answer = ['-'] * len(computer_choice)
print(answer)

while person_select > 0:
    person_choice = input('Enter your guess: ')
    
    if person_choice.isalpha():
        if person_choice in computer_choice:
            if person_choice in answer:
                print('you have guessded before, try new char: ')
            else:
                for idx, char in enumerate(computer_choice):
                    if char == person_choice:
                        answer[idx] = char
                resualt = ''.join(person_choice)
                print(f'Perfect => {answer}')

                if '-' not in answer:
                    print('you win!!!!!!')
                    break

        else:
            person_select -= 1
            if person_select == 0:
                print('you lose!!!')
            else:
                print(f'you have {person_select} chance => guess again: ')
    else:
        print('Enter a vallid charactore')


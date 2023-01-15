import time
i = 1
try:
    print('1.Downgrade all text\n2.Boost all text\n3.Capitalize the first word of a sentence')
    your_answer = int(input('Your answer should contain only the code of the desired function : '))


    while i < 10:
        new_text = str(input('Enter text : '))
        if 1 == your_answer:
            print(f'<<<\n ' + new_text.lower() + '\n>>>')
        elif 2 == your_answer:
            print(f'<<<\n ' + new_text.upper() + '\n>>>')
        elif 3 == your_answer:
            print(f'<<<\n ' + new_text.capitalize() + '\n>>>')
except Exception:
    print('Incorrect data entered. Please restart the program and enter the data according to the instructions.')

time.sleep(5)


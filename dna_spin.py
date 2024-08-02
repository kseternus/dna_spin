import random
import sys
import time
import keyboard

exit_app = False
period = 0.2  # from 0.0 to 0.5
rows = [
    '         ##',
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#'
]


def quit_app():
    global exit_app
    exit_app = True


keyboard.add_hotkey('q', lambda: quit_app())

print('Welcome to DNA SPIN!!!')
print('''You spin me right 'round, baby, right 'round
Like a record, baby, right 'round, 'round, 'round
You spin me right 'round, baby, right 'round
Like a record, baby, right 'round, 'round, 'round''')
print('\nPress Q to quit.')
input('\npress enter to continue...\n')
time.sleep(2)
row_index = 0
while not exit_app:
    row_index = row_index + 1
    if row_index == len(rows):
        row_index = 0
    if row_index == 0 or row_index == 9:
        print(rows[row_index])
        continue
    random_selection = random.randint(1, 4)
    if random_selection == 1:
        lef_nucleotide, right_nucleotide = 'A', 'T'
    elif random_selection == 2:
        lef_nucleotide, right_nucleotide = 'T', 'A'
    elif random_selection == 3:
        lef_nucleotide, right_nucleotide = 'C', 'G'
    elif random_selection == 4:
        lef_nucleotide, right_nucleotide = 'G', 'C'
    print(rows[row_index].format(lef_nucleotide, right_nucleotide))
    time.sleep(period)

print('\nBye!')
sys.exit()

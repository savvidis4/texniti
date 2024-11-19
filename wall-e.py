# print()
# print('  __      _____ ____')
# print(' /---__  ( (O)|/(O) )')
# print('\\ \\ \\ \\/  \\___U\\___/')
# print('    L\\       ||')
# print('     \\\\ ____|||_____')
# print('      \\\\|==|[]__/=|\\--|')
# print('       \\|* ||||\\==|/--|')
# print('    ____| *|[][-- |__')
# print('   ||EEE|__EEEE_[ ]_|EE\\')
# print('   ||EEE|=O      O|=|EEE|')
# print('   \\ LEEE|         \\|EEE|_))')
# print('                          ```')

import random

cell_number = input("State the number of cells you would like the world to be created into (>3): ")
fruits = int(cell_number) // 3
devil_fruit = 1
pacman = 1

state = []
indexes = []

for i in range (0,int(cell_number)):
    state.append(['',''])

for i in range (0, fruits + devil_fruit + pacman):

    index = random.randint(0,int(cell_number)-1)

    while index in indexes:
        
        index = random.randint(0,int(cell_number)-1)
    
    indexes.append(index)

print(indexes)

for i in range (0, devil_fruit):

    

    findex = random.choice(indexes)

    state[findex][1] = 'd'

    indexes.remove(findex)
    


for i in range (0, fruits):

    findex = random.choice(indexes)

    state[findex][1] = 'f'

    indexes.remove(findex)

for i in range (0, pacman):

    findex = random.choice(indexes)

    state[findex][0] = 'p'

    indexes.remove(findex)

print(state)
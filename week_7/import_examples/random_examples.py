import random

def pause():
    """Pauses the script and waits for user input to continue."""
    if input('continue? [y/n] ').lower() != 'y':
        exit()

print('--------------------[1 Random integer]----------------------------')
print('\n\n')

# 1. Random integer
print('randint:', random.randint(1, 10))
pause()

print('\n\n')
print('--------------------[2 Random float]----------------------------')
print('\n\n')

# 2. Random float
print('random:', random.random())
pause()

print('\n\n')
print('--------------------[3 Random choice]----------------------------')
print('\n\n')

# 3. Random choice
print('choice:', random.choice(['apple', 'banana', 'cherry']))
pause()

print('\n\n')
print('--------------------[4 Random sample]----------------------------')
print('\n\n')

# 4. Random sample
print('sample:', random.sample([1, 2, 3, 4, 5], 3))
pause()

print('\n\n')
print('--------------------[5 Shuffle list]----------------------------')
print('\n\n')

# 5. Shuffle list
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print('shuffled:', lst)
pause()

print('\n\n')
print('--------------------[6 Seed random]----------------------------')
print('\n\n')

# 6. Seed random
random.seed(42)
print('seeded random:', random.random())
pause()

print('\n\n')
print('--------------------[7 Uniform float]----------------------------')
print('\n\n')

# 7. Uniform float
print('uniform:', random.uniform(1, 10))
pause()

print('\n\n')
print('--------------------[8 Random choices with weights]----------------------------')
print('\n\n')

# 8. Random choices with weights
print('choices:', random.choices(['a', 'b', 'c'], weights=[10, 1, 1], k=5))
pause()

print('\n\n')
print('--------------------[9 Random range]----------------------------')
print('\n\n')

# 9. Random range
print('randrange:', random.randrange(0, 100, 5))
pause()

print('\n\n')
print('--------------------[10 Random boolean]----------------------------')
print('\n\n')

# 10. Random boolean
print('random boolean:', random.choice([True, False]))
pause()

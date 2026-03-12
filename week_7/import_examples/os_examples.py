import os

def pause():
    """Pauses the script and waits for user input to continue."""
    if input('continue? [y/n] ').lower() != 'y':
        exit()

print('--------------------[1 Get current working directory]----------------------------')
print('\n\n')

# 1. Get current working directory
print('Current directory:', os.getcwd())
pause()

print('\n\n')
print('--------------------[2 List files in current directory]----------------------------')
print('\n\n')

# 2. List files in current directory
print('Files:', os.listdir())
pause()

print('\n\n')
print('--------------------[3 Make a new directory]----------------------------')
print('\n\n')

# 3. Make a new directory
os.mkdir('test_dir')
print('Created test_dir')
pause()

print('\n\n')
print('--------------------[4 Remove a directory]----------------------------')
print('\n\n')

# 4. Remove a directory
os.rmdir('test_dir')
print('Removed test_dir')
pause()

print('\n\n')
print('--------------------[5 Check if a path exists]----------------------------')
print('\n\n')

# 5. Check if a path exists
print('Path exists:', os.path.exists('test_dir'))
pause()

print('\n\n')
print('--------------------[6 Join paths]----------------------------')
print('\n\n')

# 6. Join paths
print('Joined path:', os.path.join('folder', 'file.txt'))
pause()

print('\n\n')
print('--------------------[7 Split path]----------------------------')
print('\n\n')

# 7. Split path
print('Split path:', os.path.split('/home/user/file.txt'))
pause()

print('\n\n')
print('--------------------[8 Get file size]----------------------------')
print('\n\n')

# 8. Get file size
with open('temp.txt', 'w') as f:
    f.write('hello')
print('File size:', os.path.getsize('temp.txt'))
os.remove('temp.txt')
pause()

print('\n\n')
print('--------------------[9 Rename a file]----------------------------')
print('\n\n')

# 9. Rename a file
with open('old.txt', 'w') as f:
    f.write('data')
os.rename('old.txt', 'new.txt')
print('Renamed old.txt to new.txt')
os.remove('new.txt')
pause()

print('\n\n')
print('--------------------[10 Get environment variable]----------------------------')
print('\n\n')

# 10. Get environment variable
print('HOME env:', os.environ.get('HOME'))
pause()

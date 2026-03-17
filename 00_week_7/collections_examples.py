from collections import Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap

def pause():
    """Pauses the script and waits for user input to continue."""
    if input('continue? [y/n] ').lower() != 'y':
        exit()

print('--------------------[1 Counter]----------------------------')
print('\n\n')

# 1. Counter example
c = Counter('banana')
print('Counter:', c)
for key in c:
    print(f'{key} : {c[key]}')
pause()

print('\n\n')
print('--------------------[2 defaultdict]----------------------------')
print('\n\n')

# 2. defaultdict example
dd = defaultdict(int)
dd['a'] += 1
print('defaultdict:', dd)
pause()

print('\n\n')
print('--------------------[3 deque]----------------------------')
print('\n\n')

# 3. deque example
dq = deque([1, 2, 3])
dq.appendleft(0)
print('deque:', dq)
pause()

print('\n\n')
print('--------------------[4 namedtuple]----------------------------')
print('\n\n')

# 4. namedtuple example
Point = namedtuple('Point', 'x y')
p = Point(1, 2)
print('namedtuple:', p)
pause()

print('\n\n')
print('--------------------[5 OrderedDict]----------------------------')
print('\n\n')

# 5. OrderedDict example
od = OrderedDict()
od['a'] = 1
od['b'] = 2
print('OrderedDict:', od)
pause()

print('\n\n')
print('--------------------[6 ChainMap]----------------------------')
print('\n\n')

# 6. ChainMap example
cm = ChainMap({'a': 1}, {'b': 2})
print('ChainMap:', cm)
pause()

print('\n\n')
print('--------------------[7 Counter update]----------------------------')
print('\n\n')

# 7. Counter update
c.update('apple')
print('Counter update:', c)
pause()

print('\n\n')
print('--------------------[8 deque pop]----------------------------')
print('\n\n')

# 8. deque pop
print('deque pop:', dq.pop())
pause()

print('\n\n')
print('--------------------[9 defaultdict with list]----------------------------')
print('\n\n')

# 9. defaultdict with list
ddl = defaultdict(list)
ddl['fruits'].append('apple')
print('defaultdict list:', ddl)
pause()

print('\n\n')
print('--------------------[10 namedtuple fields]----------------------------')
print('\n\n')

# 10. namedtuple fields
print('namedtuple fields:', p._fields)
pause()

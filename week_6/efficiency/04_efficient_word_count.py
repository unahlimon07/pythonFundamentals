#[1] word counting
myStr = "From From fairest creatures we desire increase,\n"\
        "That thereby beauty's rose might never die,\n"\
        "But as the riper should by time decease,\n"\
        "His tender heir might bear his memory:\n"\
        "But thou contracted to thine own bright eyes,\n"\
        "Feed'st thy light's flame with self-substantial fuel,\n"\
        "Making a famine where abundance lies,\n"\
        "Thy self thy foe, to thy sweet self too cruel:\n"\
        "Thou that art now the world's fresh ornament,\n"\
        "And only herald to the gaudy spring,\n"\
        "Within thine own bud buriest thy content,\n"\
        "And tender churl mak'st waste in niggarding:\n"\
        "Pity the world, or else this glutton be,\n"\
        "To eat the world's due, by the grave and to thee.\n"

# replace symbols with space
def replaceSymbol(myStr):
    symbols = ['\n','\r','\t',',',':',';','.','?','!']
    for s in symbols:
        myStr = myStr.replace(s,' ')
    return myStr

def strToList(myStr):
    return myStr.split()

myStr = replaceSymbol(myStr)
new_list = strToList(myStr)

new_dictionary = {}

# COUNT WORDS (single loop using if-else)
for mem in new_list:
    if mem not in new_dictionary:
        new_dictionary[mem] = 1
    else:
        new_dictionary[mem] += 1

# more efficient
# for mem in new_list:
#     new_dictionary[mem] = new_dictionary.get(mem, 0) + 1


# more more better
# from collections import Counter
# new_dictionary = Counter(new_list)


# SORT 1: Alphabetically
print('--------sort alphabetically--------')

for key in sorted(new_dictionary):
    print(f'{key} : {new_dictionary[key]}')


# SORT 2: Based on value
print('--------sort based on VALUE--------')

sorted_list = sorted(new_dictionary.items(), key=lambda x: x[1], reverse=True)

for key, value in sorted_list:
    print(f'{key} : {value}')
'''
Created on Jul 12, 2014

@author: tisma@linux.com
'''
import matplotlib.pyplot as plt

try:
    file2011 = open('2011.txt')
    file2012 = open('2012.txt')
    file2013 = open('2013.txt')
    file2014 = open('2014.txt')
except IOError:
    print "File cannot be opened!"
    exit()

text2011 = file2011.readlines()[:]
text2012 = file2012.readlines()[:]
text2013 = file2013.readlines()[:]
text2014 = file2014.readlines()[:]

# game is 7 of 39
LOTO_NUMBERS = 39

def statistics(text):
    array = [0] * LOTO_NUMBERS
    for i in range(1, len(text)):
        line = text[i]
        if line[2] != '.' and line[2] != ' ':
            line = line[10:]
        else:
            line = line[8:]
        line = line.replace("Download", "").strip()
        line = map(int, line.split(" "))
#       if i == len(text)-1:
        try:
            for x in line:
                array[x - 1] = array[x - 1] + 1
        except IndexError:
            print x, i
    return array

array2011 = [0] * LOTO_NUMBERS
array2012 = [0] * LOTO_NUMBERS
array2013 = [0] * LOTO_NUMBERS
array2014 = [0] * LOTO_NUMBERS

array2011 = statistics(text2011)
array2012 = statistics(text2012)
array2013 = statistics(text2013)
array2014 = statistics(text2014)

def draw(array, title):
    plt.plot(array, 'bs')
#     plt.hist(array,39)
    plt.title(title)
    plt.xlabel('numbers')
    plt.ylabel('appereance')
    plt.show()

draw(array2011, 'loto 2011')
draw(array2012, 'loto 2012')
draw(array2013, 'loto 2013')
draw(array2014, 'loto 2014')

print array2011
print array2012
print array2013
print array2014

file2011.close()
file2012.close()
file2013.close()
file2014.close()

'''
Created on Dec 2, 2017

@author: ITAUser
'''
def countingletters(filename, mychar):
    f = open(filename,'r')
    count = 0; 
    run = True
    while run:
        letter = f.read(1)
        letter = letter.lower()
        if letter == "":
            break
        else:
            if letter == mychar:
                count = count + 1
    print(count)
    return count
import string 
#make a list with the alphabet
letters = list(string.ascii_lowercase)
#make a list to store the count of each letters
letters_count = [0]*26
#print(letters_count)
#make a loop that counts how many of each letters there are
for i in range(len (letters)):
#    print("i=", i)
#    print("letter_counts[i] = " , letters_count[i])
#   print("letter[i] = ", letters[i])
    letters_count[i] = countingletters("constitution.txt", letters[i])
#define the maximum value 
print (letters_count)
pop = max(letters_count)
print (pop)
indexofletter = letters_count.index(pop)
large = letters[indexofletter]
print (large)
#find the letter at the maximum value
#print the answer 
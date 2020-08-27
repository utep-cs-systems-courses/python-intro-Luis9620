import re
import sys
words= []
words_dictionary = {}
#Open, read the file and store words in a list
with open(sys.argv[1], "r") as file: #Get file from the arguments
    for line in file:
        line = line.replace("-", " ") #Getting rid off "-"
        line = line.replace("'", " ") #Getting rid off "'"
        for word in line.split():
            word = re.sub(r'[^\w\s]', '', word) #Getting rid off all punctuatins
            words.append(word.lower())
    file.close()

words.sort();   #Sort the words in the word list
#store the words in the list into a dictionary to get rid off duplicates
for word in words:
    words_dictionary[word] = words.count(word)  #Store each word with their respective word count
#
#Print word in console
for word in words_dictionary:
    print(word, words_dictionary[word])

#Print the word dictionary in a file
with open(sys.argv[2], "w") as file:
	for word in words_dictionary:
		print(word, words_dictionary[word], file=file)
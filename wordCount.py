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

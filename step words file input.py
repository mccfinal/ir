import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# word tokenize accepts # a string as an input, not a file.
stop_words = set(stopwords.words('english'))
file1 = open("text.txt")
# Use this to read file content as a stream:
line=file1.read()
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile= open('filteredtext.txt','a')
        appendFile.write(" "+r)
        appendFile.close()

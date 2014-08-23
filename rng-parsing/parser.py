import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

from os import listdir
from os.path import isfile, join

from collections import Counter

def get_core_words( text ):

    #TOKENIZATION
    b = nltk.word_tokenize(text)

    #CONVERT INTO LOWER CASE
    looper = 0
    for token in b:
        b[looper] = token.lower()
        looper+=1

    #REMOVE THE STOPWORDS FROM THE FILE
    minlength = 2
    c = [token for token in b if (not token in stopwords.words('english')) and len(token) >= minlength]

    #STEMMING THE WORDS TO ITS BASE FORM
    stemmer = SnowballStemmer("english")
    looper1 = 0
    for token in c:
        c[looper1] = stemmer.stem(token.decode("utf8"))
        looper1 +=1
    return c

def load_text ( file_path ):
    return open(file_path, 'r').read()

def pre_process_text ( text ):
    text.decode("utf8")
    return text

root_path = "/home/dummey/global-hack-data/articles"
text_file_paths = [ join(root_path, f) for f in listdir(root_path) if isfile(join(root_path,f)) ]

aggregate = Counter();

for text_file_path in text_file_paths:
    raw_text = pre_process_text(load_text(text_file_path))
    core_words = get_core_words(raw_text)
    aggregate.update( Counter(core_words) )
    if len(list(aggregate.elements())) > 10000:
        break

print aggregate.most_common(100)
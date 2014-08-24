
import urllib2
import json
from nltk.corpus import wordnet
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords

url = 'http://api.redditanalytics.com/trending?subreddit=worldnews'

#get the current trends
data_source = urllib2.urlopen(url)
data = json.loads(data_source.read())

def get_core_words( text ):

    #TOKENIZATION
    b = word_tokenize(text)

    #KEEP ONLY NOUNS
    b = [noun for noun, pos in pos_tag(b) if pos.startswith('N')]

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

#mark previous transactions as invalid 
for entry in data['results']['trending']:
    core_words = get_core_words(entry['phrase'])

    for word in core_words:  
        try:
            word_synnet = wordnet.synset(word + '.n.01')
            lemma_names = word_synnet.lemma_names

            print zip(lemma_names, [entry['count'] * entry['count']] * len(lemma_names))
        except:
            pass

#add as transaction to db


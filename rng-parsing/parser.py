import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
 
nltk.download()

#TOKENIZATION
 
sentence = "Operating system is the heart of a computer"
b = nltk.word_tokenize(sentence)
print b
 
#CONVERT INTO LOWER CASE
 
looper = 0
for token in b:
 b[looper] = token.lower()
 looper+=1
print b
 
#REMOVE THE STOPWORDS FROM THE FILE
 
minlength = 2
c = [token for token in b if (not token in stopwords.words('english')) and len(token) >= minlength]
print c
 
#STEMMING THE WORDS TO ITS BASE FORM
stemmer = SnowballStemmer("english")
looper1 = 0
for token in c:
 c[looper1] = stemmer.stem(token)
 looper1 +=1
print c
import nltk
from nltk import word_tokenize, pos_tag
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk.corpus import wordnet

from os import listdir
from os.path import isfile, join, basename

from collections import Counter

import itertools

import math

import pprint as pp
import json

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

def load_text ( file_path ):
    return open(file_path, 'r').read()

def pre_process_text ( text ):
    text.decode("utf8")
    return text

def word_pair_weights( core_words ):
    word_counter = Counter(core_words)

    word_pairs = list(itertools.combinations(word_counter.keys(), 2))
    scores = []
    for word_pair in word_pairs:
        scores.append((word_pair, word_counter[word_pair[0]] * word_counter[word_pair[1]]))
    
    return Counter(dict(sorted(scores, key=lambda x: x[1])))

def get_parents( word ):
    try:
        word_synnet = wordnet.synset(word + '.n.01')
        word_parent = list(set([w for s in word_synnet.closure(lambda s:s.hypernyms()) for w in s.lemma_names]))
        return word_parent
    except:
        return []

def get_children( word ):
    try:
        word_synnet = wordnet.synset(word + '.n.01')
        word_children = list(set([w for s in word_synnet.closure(lambda s:s.hyponyms()) for w in s.lemma_names]))
        return word_children
    except:
        return []

def _associate_with_pair_and_weights(base, other, score, decay = 0.5):
    base_other_pair = zip(base, [other] * len(base))
    parent_pairs_with_weight = zip(base_other_pair, [int(round(score * decay))] * len(base))

    return Counter(dict(parent_pairs_with_weight))


root_path = "/home/dummey/global-hack-data/articles"
text_file_paths = [ join(root_path, f) for f in listdir(root_path) if isfile(join(root_path,f)) ]

counter = 0


for text_file_path in text_file_paths:
    print text_file_path

    #construct output path names
    source_name = basename(text_file_path).split('.')[0]
    sibling_output = join('dump', source_name + '-siblings.json')
    parent_output = join('dump', source_name + '-parent.json')
    children_output = join('dump', source_name + '-children.json')

    #if all of output files exist, skip
    if isfile(sibling_output) and isfile(parent_output) and isfile(children_output):
        print "\t Skipping"
        continue

    related_aggregate = Counter()
    parent_aggregate = Counter()
    children_aggregate = Counter()

    raw_text = pre_process_text(load_text(text_file_path))
    core_words = get_core_words(raw_text)
        
    #related word pairs
    related_word_pairs = word_pair_weights(core_words)

    #prune relate_word_pairs that only have 1 count
    related_word_pairs_cleaned = {}
    for pair in related_word_pairs:
        score = related_word_pairs[pair]
        if score > 10:
            related_word_pairs_cleaned[pair] = score
    related_word_pairs = Counter(related_word_pairs_cleaned)

    related_aggregate.update(Counter(related_word_pairs))

    for pairs in related_word_pairs:       
        score = related_word_pairs[pairs]

        parents = get_parents(pairs[0])
        parent_aggregate.update(_associate_with_pair_and_weights(parents, pairs[1], score))

        parents = get_parents(pairs[1])
        parent_aggregate.update(_associate_with_pair_and_weights(parents, pairs[0], score))

        children = get_children(pairs[0])
        children_aggregate.update(_associate_with_pair_and_weights(children, pairs[1], score))

        children = get_children(pairs[1])
        children_aggregate.update(_associate_with_pair_and_weights(children, pairs[0], score))

    with open(sibling_output, 'w') as outfile:
        json.dump(related_aggregate.most_common(), outfile)

    with open(parent_output, 'w') as outfile:
        json.dump(parent_aggregate.most_common(), outfile)

    with open(children_output, 'w') as outfile:
        json.dump(children_aggregate.most_common(), outfile)

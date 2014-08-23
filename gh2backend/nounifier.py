from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag




def find_nouns(blob):
    tokenized_blob = word_tokenize(blob)
    nouns = [noun for noun, pos in pos_tag(tokenized_blob) if pos.startswith('N')]
    return nouns


def get_noun_related_words(noun):
    synsets = wordnet.synsets(noun)
    data = {}
    for synset in synsets:
        hyponyms = [name.lemma_names[0] for name in synset.hyponyms() if synset.hyponyms() > 0]
        hypernyms = [name.lemma_names[0] for name in synset.hypernyms() if synset.hypernyms() > 0]
        data.setdefault('hyponyms', []).extend(hyponyms)
        data.setdefault('hypernyms', []).extend(hypernyms)

    return data


def build_data(flask_test_client):
    return 'ok'


if __name__ == "__main__":
    pass

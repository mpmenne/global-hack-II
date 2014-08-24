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

from subprocess import PIPE, Popen
import os

import re

#PLESE AXE MURDER, DON'T KILL ME

def load_text ( file_path ):
    return open(file_path, 'r').read()

# root_path = "/home/dummey/global-hack-data/articles"
# text_file_paths = [ join(root_path, f) for f in listdir(root_path) if isfile(join(root_path,f)) ]

# for path in text_file_paths:
#     text = load_text(text_file_paths)

#     

textteaser_path = '/home/dummey/sbt/textteaser'
sbt_path = '/home/dummey/sbt/bin/sbt'

root_path = "/home/dummey/global-hack-data/articles"
output_path = "/home/dummey/global-hack-data/articles/summary"

text_file_paths = [ join(root_path, f) for f in listdir(root_path) if isfile(join(root_path,f)) ]

os.chdir(textteaser_path)
p = Popen([sbt_path, 'run'], stdin=PIPE, stdout=PIPE)

cache = []
recording = 0
cur_file = ""
while True:
    last_line = p.stdout.readline()
    # if len(last_line) < 1:
    #     continue
    print last_line.rstrip("\n")

    if last_line.find('com.textteaser.summarizer.Main') > -1:
        p.stdin.write("1\r")
    elif last_line.find('Provide the article title:') > -1:
        p.stdin.write("\r")
    elif last_line.find('Provide the article text') > -1:
        cur_file = text_file_paths.pop()
        text = open(cur_file, 'r').read()
        p.stdin.write(text.replace('\n', ' ') + "\r")

    if recording == 1:
        cache.append(last_line.replace("\n", ''))

    if last_line.find('---- Summary ----') > -1:
        recording = 1
    elif last_line.find('-----------------') > -1:
        recording = 0
        del cache[-1]

        results = "\n".join(cache)
        source_name = basename(cur_file).split('.')[0]
        file_output_path = join(output_path, source_name + ".summary.txt")
        with open(file_output_path, 'w') as outfile:
            outfile.write(results)

        cache = []

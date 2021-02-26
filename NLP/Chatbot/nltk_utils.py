
"""This module takes in a list of words and return a 
    tokenized stemmed bag of words.
"""
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize( sentence ):
    return nltk.word_tokenize( sentence )

def stem( word ):
    word = word.lower()
    return stemmer.stem( word )

def convert_and_pad( all_words, sentence ):
    NO_W = 0.0 #Used to represent words not in all words
    INFREQ_W = 1.0 #Used to represent words not appearing frequent in all words

    bag = np.zeros( len(all_words), dtype=np.float32 )
    for idx, w in enumerate( all_words ):
        if w in sentence:
            bag[ idx ] = 1.0

    return np.array( bag )
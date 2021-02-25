class NltkUtils( words ):
    """This class takes in a list of words and return a 
    tokenized stemmed bag of words.
    """
    import nltk
    import numpy as np
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer

    def __init__( self, words ):
        self.words = words
        self.stemmer = PorterStemmer()

    def tokenize( self, sentence ):
        return nltk.word_tokenize( sentence )

    def stem( self, word ):
        word = word.lower()
        return stemmer.stem( word )

    def convert_and_pad( self, tokenized_words, all_words ):
        NO_W = 0.0 #Used to represent words not in all words
        INFREQ_W = 1.0 #Used to represent words not appearing frequent in all words

        self.pad_lenght = 100
        working_sentence = [ NO_W ] * pad_lenght

        for w_idx, word in enumerate( tokenized_words ):
            if word in all_words:
                working_sentence[ w_idx ] = all_words[ word ]
            else:
                working_sentence[ w_idx ] = INFREQ_W

        return working_sentence, min( len(tokenized_words), self.pad_lenght )

    def convert_and_pad_data( self, tokenized_words, all_words ):
        bag_of_words = []
        length = []

        for sentence in sentences:
            converted, leng = convert_and_pad( all_words, sentence, self.pad_lenght )
            bag_of_words.append( converted )
            lenght.append( leng )

        return np.array( bag_of_words ), np.array( lenghts )


def convert_and_pad_data(word_dict, data, pad=500):
    result = []
    lengths = []
    
    for sentence in data:
        converted, leng = convert_and_pad(word_dict, sentence, pad)
        result.append(converted)
        lengths.append(leng)
        
    return np.array(result), np.array(lengths)




    


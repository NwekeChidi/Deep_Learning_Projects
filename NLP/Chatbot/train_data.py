
def prepare_train_data(): 
    import numpy as np
    import json
    from nltk.corpus import stopwords
    from nltk_utils import tokenize, stem, convert_and_pad

    with open( "intents.json", "r" ) as f:
        data = json.load( f )

    all_words = [ ]
    tags = [ ]
    x_y = [ ]

    for d_point in data[ "intents" ]:
        tag = d_point[ 'tag' ]
        tags.append( tag )
        
        for pattern in d_point[ "patterns" ]:
            word = tokenize( pattern )
            word = [ s_w.lower() for s_w in word ]
            all_words.extend( word )
            x_y.append( (word, tag) )

    signs = [ '!', '?', ',', '.']
    all_words = [ stem( w ) for w in all_words if w not in signs ]
    all_words = sorted( set(all_words) )
    tags = sorted( set(tags) )

    X_train = []
    y_train = []

    for ( pattern_sentence, tag ) in x_y:
        bag_of_words = convert_and_pad( all_words, pattern_sentence )
        X_train.append( bag_of_words )

        label = tags.index( tag )
        y_train.append( float(label) )
    y_train = np.array( y_train )
    
    ## Testing fuction/
    # sents = ['hi', 'hello', 'i', 'you', 'bye', 'thank', 'cool']
    # ss = ['hello', 'how', 'are', 'you']
    # print(convert_and_pad(sents, ss))

    return X_train, y_train, [ all_words, tags, x_y ]


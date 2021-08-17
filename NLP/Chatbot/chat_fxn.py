import numpy as np
import torch
import json
import random
import torch.nn as nn
from model_architect import MNet
from nltk_utils import stem, tokenize, convert_and_pad

# Loading saved variables
with open( "intents.json", "r" ) as f:
    intents = json.load( f )

variables_pth = "variables.pt"
variables = torch.load( variables_pth )

# Initializing variables
input_size = variables[ "input" ]
output_size = variables[ "output" ]
hidden_size = variables[ "hidden" ]
all_words = variables[ "vocabulary" ]
tags = variables[ "tags" ]
model_state = variables[ "model_artefacts" ]


model = MNet( input_size, hidden_size, output_size )
model.load_state_dict( model_state )

model.eval()

bot_name = "Linden"

response_1 = ['Sorry, I do not understand.....',
             'I think it is better you chat with a live agent, please hold..']

def get_response( sentence ):

    sentence = tokenize( sentence )
    sentence = [ s_w.lower() for s_w in sentence ]
    sentence = convert_and_pad( all_words, sentence )
    sentence.reshape( 1, sentence.shape[0] )
    sentence = torch.from_numpy( sentence )

    output = model( sentence.float() )
    probs = torch.softmax( output, dim=0 )
    ps, idx = torch.sort( probs, descending=True )
    ps = ps.detach().numpy()
    idx = idx.detach().numpy()
    ps, idx = ps[ 0 ], idx[ 0 ]
    tag = tags[ idx ]

    # Getting output probabilities
    # probs = torch.softmax( output, dim=0 )
    # prob = probs[ 0 ][ prediction.item() ]

    if ps >= 0.75:
        for intent in intents[ "intents" ]:
            if tag == intent[ "tag" ]:
                return random.choice(intent['responses'])
                    
    else:
        return random.choice( response_1 )
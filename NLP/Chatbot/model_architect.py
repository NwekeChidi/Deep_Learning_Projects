import torch
import torch.nn as nn 

# Building Architecture

class MNet( nn.Module ):
    def __init__( self, input_size, hidden_size, output ):
        super( MNet, self ).__init__()
        self.fc1 = nn.Linear( input_size, hidden_size )
        self.fc2 = nn.Linear( hidden_size, hidden_size )
        self.fc3 = nn.Linear( hidden_size, output )
        self.relu = nn.ReLU()
        
    def forward( self, x ):
        x = self.relu( self.fc1( x ) )
        x = self.relu( self.fc2( x ) )
        x = self.fc3( x )
        return x
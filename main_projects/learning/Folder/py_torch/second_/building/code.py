#!/usr/bin/env python3

from torch import nn
from torch import optim
import torch.nn.functional as F

class Network(nn.Module):
    def __init__(self):
        super().__init__()
        # Defining the layers, 128, 64, 10 units each
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 64)
        # Output layer, 10 units - one for each digit
        self.fc3 = nn.Linear(64, 10)
        
    def forward(self, x):
        ''' Forward pass through the network, returns the output logits '''
        
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        x = F.softmax(x, dim=1)
        
        return x

model = Network()

#print(model.fc1.bias, '\n')

print(model.fc1.bias.data, '\n')
#print(model.fc1.weight, '\n')
#print(model.fc1.bias, '\n')
#print(model.fc1.weight + 1)
#print(); print((model.fc1.bias.data.size)); print()

# Set biases to all zeros
print(model.fc1.bias.data.fill_(1), '\n\n\n\n\n')

# sample from random normal with standard dev = 0.01
print(model.fc1.weight.data.normal_(2))

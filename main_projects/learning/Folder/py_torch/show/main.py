#!/usr/bin/env python3

from torchvision import datasets, transforms
import torch
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

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)
#print(criteration, '\n')
#print(optimizer)

###########print('Initial weight - ', model.fc1.weight)#.data)

transform = transforms.Compose([transforms.ToTensor(),
transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),])

trainset = datasets.MNIST(
      'MNIST_data/',
      download=True,
      train=True,
      transform=transform)

trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
images, labels = next(iter(trainloader))
images.resize_(64,784)

output = model.forward(images)
loss = criterion(output, labels)
loss.backward()
############print('Gradient -', model.fc1.weight.grad)
optimizer.step()

##############print('Updated weights - ', model.fc1.weight)





#!/usr/bin/env python3

import torch
#from some_shit.code import trainloader, criterion
from torchvision import datasets, transforms
from torch import optim
from torch import nn
#from some_shit.code import Network
import torch.nn.functional as F
from helper import view_classify

transform = transforms.Compose([transforms.ToTensor(),
transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),])
trainset = datasets.MNIST(
	'MNIST_data/',
	download=True,
	train=True,
	transform=transform)


criterion = nn.CrossEntropyLoss()
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

class Network(nn.Module):
	def __init__(self):
		super().__init__()
# Defining the layers, 128, 64, 10 units each
		self.fc1 = nn.Linear(784, 128)
		self.fc2 = nn.Linear(128, 64)
# Output layer, 10 units - one for each digit
		self.fc3 = nn.Linear(64, 10)

	def forward(self, x):

		x = self.fc1(x)
		x = F.relu(x)
		x = self.fc2(x)
		x = F.relu(x)
		x = self.fc3(x)
		x = F.softmax(x, dim=1)

		return x


model = Network()


optimizer = optim.SGD(model.parameters(), lr=0.003)
epochs = 1
print_every = 40
steps = 0
step = 0
for e in range(epochs):
  running_loss = 0
  for images, labels in iter(trainloader):
    steps += 1
    images.resize_(images.size()[0], 784)

    optimizer.zero_grad()

    output= model.forward(images)
    loss = criterion(output, labels)
    loss.backward()
    optimizer.step()

    running_loss += loss.item()

    if steps % print_every ==0:
      #print('\n', "steps is - {}".format(steps))
      step += 1
      print(step, ') EPoch : {}/{}...'. format(e+1, epochs),
            ' Loss: {:.4f}'.format(running_loss/print_every))

       
      #как число с плавающей точкой(f - float), c округлением 
      #до 4-х знаков после запяой 
      running_loss = 0

#images, labels = next(iter(trainloader))

#img = images[0].view(1, 784)
### Turn off gradients to speed up this part
#with torch.no_grad():
#  logits = model.forward(img)

#ps = F.softmax(logits, dim=1)
#view_classify(img.view(1, 28, 28), ps)

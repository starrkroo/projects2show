#!/usr/bin/env python3

import torch
from some_shit.code import trainloader, criterion
from torch import optim
from some_shit.code import Network
import torch.nn.functional as F
from helper import view_classify

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
    #optimizer.step()

    running_loss += loss.item()

    if steps % print_every ==0:
      print('\n', "steps is - {}".format(steps))
      #print('print_every is - {}'.format(print_every))
      #print("Result of sharing: {:.4f}".format(running_loss/print_every), '\n')
      step += 1
      print(step, ') EPoch : {}/{}...'. format(e+1, epochs),
            ' Loss: {:.4f}'.format(running_loss/print_every))

       
      #как число с плавающей точкой(f - float), c округлением 
      #до 4-х знаков после запяой 
      running_loss = 0

images, labels = next(iter(trainloader))

img = images[0].view(1, 784)
## Turn off gradients to speed up this part
with torch.no_grad():
  logits = model.forward(img)

## Output of the network are logits, need to take softmax for probabilities
ps = F.softmax(logits, dim=1)
view_classify(img.view(1, 28, 28), ps)

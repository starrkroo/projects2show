#!/usr/bin/env python3


# Neseccery packages
import matplotlib.pyplot as plt
import torch
from torch import nn, optim
import torch.nn.functional as F
import time
import numpy as nmp
from torchvision import datasets, transforms
import helper
from main import Network
model = Network()

# Define a trannsform to normalize the data
transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
)

# Load the training data
trainset = datasets.FashionMNIST('F_MNIST_data/', download=False, train=True, transform
=transform)


# Download and load the test data
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
testset = datasets.FashionMNIST('F_MNIST_data/', download=False, train=False, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=True)


image, label = next(iter(trainloader))
print(helper.imshow(image[0,:]))



dataiter = iter(testloader)
images, labels = dataiter.next()
img = images[0]
#print(images)
#time.sleep(1)
#print(img)

img = img.resize_(1, 784)
#print(img)
#ps = model.forward(images[0,:])
#helper.view_classify(img.resize_(1, 28, 28), ps, version='Fashion')


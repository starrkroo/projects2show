#!/usr/bin/env python3
import torch

def MyNetworkForward(weights, bias, x):
    h1 = weights @ x + bias
    a1 = torch.tanh(h1)

    return a1

weights = weights.cuda()
bias = bias.cuda()
x = x.cuda()

y = MyNetworkForward(weights, bias, x)
loss = torch.mean((y - y_hat) ** 2)

loss.backward()

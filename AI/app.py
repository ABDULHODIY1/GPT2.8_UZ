from numpy import *
from torch import nn, optim

from sheryozuvchi import model

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

def train(input_tensor, target_tensor):
    target_tensor.unsqueeze_(-1)
    hidden = model.init_hidden()

    model.zero_grad()
    loss = 0

    for i in range(input_tensor.size(0)):
        output, hidden = model(input_tensor[i], hidden)
        loss += criterion(output, target_tensor[i])

    loss.backward()
    optimizer.step()

    return loss.item() / input_tensor.size(0)

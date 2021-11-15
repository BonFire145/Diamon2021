import os
import torch
from torch.autograd import Variable
import numpy as np
#import getAPIbloodinfo


def path():
    return os.path.dirname(os.path.abspath(__file__))


def modelFile():
    return os.path.join(path(), "model/model_static.pt")


def LoadModel(model):
    model.load_state_dict(torch.load(modelFile()))
    model.eval()

    return model


def Prediction(xy):
    torch.manual_seed(777)  # for reproducibility
    xy = np.array(xy, dtype=np.float32)
    x_data = xy
    y_data = xy[[-1]]

    X = Variable(torch.from_numpy(x_data))
    Y = Variable(torch.from_numpy(y_data))

    linear = torch.nn.Linear(8, 1, bias=True)
    tanh = torch.nn.Tanh()
    model = torch.nn.Sequential(linear, tanh)
    model = LoadModel(model)

    return displayLearning(model, X, Y)


def displayLearning(model, X, Y):
    predicted = (model(X).data > 0.5).float()

    return int(predicted.numpy()[0].tolist())

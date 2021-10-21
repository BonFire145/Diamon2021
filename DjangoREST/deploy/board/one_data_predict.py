import os
import torch
from torch.autograd import Variable
import numpy as np
#import getAPIbloodinfo


def path():
    return os.path.dirname(os.path.abspath(__file__))


def modelFile():
    return os.path.join(path(), "model/model_static.pt")


def csvFile():
    return os.path.join(path(), "data-03-diabetes.csv")


def CheckingcsvFile():
    return os.path.join(path(), "TempCSV/getAPIbloodinfo.csv")


def saveModel(model):
    torch.save(model.state_dict(), modelFile())


def LoadModel(model):
    model.load_state_dict(torch.load(modelFile()))
    model.eval()

    return model


def Prediction(xy):
    torch.manual_seed(777)  # for reproducibility
    xy = np.array(xy, dtype=np.float32)
    x_data = xy
    print("패러미터: \n{}".format(x_data))
    y_data = xy[[-1]]

    X = Variable(torch.from_numpy(x_data))
    Y = Variable(torch.from_numpy(y_data))

    # Hypothesis using sigmoid
    linear = torch.nn.Linear(8, 1, bias=True)
    sigmoid = torch.nn.Sigmoid()
    model = torch.nn.Sequential(linear, sigmoid)

    model = LoadModel(model)
    return displayLearning(model, X, Y)


def displayLearning(model, X, Y):
    hypothesis = model(X)
    
   # Accuracy computation
    predicted = (model(X).data > 0.5).float()
    accuracy = (predicted == Y.data).float().mean()

    return int(predicted.numpy()[0].tolist())

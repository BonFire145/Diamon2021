import os
import torch
from torch.autograd import Variable
import numpy as np
import getAPIbloodinfo


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


def Prediction():
    torch.manual_seed(777)  # for reproducibility

    #xy = np.loadtxt(csvFile(), delimiter=',', dtype=np.float32)
    xy = np.loadtxt(CheckingcsvFile(), delimiter=',', dtype=np.float32)[1:]
    x_data = xy[:-1]
    print("패러미터: \n{}".format(x_data))
    y_data = xy[[-1]]

    global X
    global Y
    X = Variable(torch.from_numpy(x_data))
    Y = Variable(torch.from_numpy(y_data))

    # Hypothesis using sigmoid
    linear = torch.nn.Linear(8, 1, bias=True)
    sigmoid = torch.nn.Sigmoid()
    model = torch.nn.Sequential(linear, sigmoid)

    model = LoadModel(model)

    return model


def displayLearning(model):
    hypothesis = model(X)

#    global correct_count
#    global dismiss_count

    # Accuracy computation
    predicted = (model(X).data > 0.5).float()
    accuracy = (predicted == Y.data).float().mean()
    print("\n예측값(Y): ", predicted.numpy()[0])
    print("\n신뢰도: {:.2f}%".format(accuracy*100))
#    if accuracy == 1:
#        correct_count = correct_count + 1
#    else:
#        dismiss_count = dismiss_count + 1
#   print("\n=========================================================================\n")


if __name__ == '__main__':
#    global correct_count
#    global dismiss_count
#    correct_count = 0
#    dismiss_count = 0
#    for i in range(1, 760):
        #print("i = {}".format(i))
    getAPIbloodinfo.getAPIinfo(str(2))
    displayLearning(Prediction())
#        print("예측 성공 수: {}".format(correct_count))
#        print("예측 실패 수: {}".format(dismiss_count))

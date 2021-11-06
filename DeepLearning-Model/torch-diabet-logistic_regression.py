import os
import torch
from torch.autograd import Variable
import numpy as np


def path():
    return os.path.dirname(os.path.abspath(__file__))


def modelFile():
    return os.path.join(path(), "model/model_static.pt")


def csvFile():
    return os.path.join(path(), "data-03-diabetes.csv")


def saveModel(model):
    torch.save(model.state_dict(), modelFile())


def LoadModel(model):
    model.load_state_dict(torch.load(modelFile()))
    model.eval()

    return model


def setting_DeepLearning():
    torch.manual_seed(777)  # for reproducibility

    xy = np.loadtxt(csvFile(), delimiter=',', dtype=np.float32)
    x_data = xy[:, 0:-1]
    y_data = xy[:, [-1]]

    # Make sure the shape and data are OK
    print(x_data.shape, y_data.shape)

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


def start_learning(learning_model):
    optimizer = torch.optim.SGD(learning_model.parameters(), lr=0.01)

    for step in range(10001):
        optimizer.zero_grad()
        hypothesis = learning_model(X)
        # cost/loss function
        cost = -(Y * torch.log(hypothesis) + (1 - Y)
                 * torch.log(1 - hypothesis)).mean()
        cost.backward()
        optimizer.step()

        if step % 200 == 0:
            print(step, cost.data.numpy())

    saveModel(learning_model)

    return (learning_model, hypothesis)


def displayLearning(infoTuple):
    model, hypothesis = infoTuple

    # Accuracy computation
    predicted = (model(X).data > 0.5).float()
    accuracy = (predicted == Y.data).float().mean()
    print("\nHypothesis: ", hypothesis.data.reshape(11, 3, 23).numpy())
    print("\nCorrect (Y): ", predicted.reshape(11, 3, 23).numpy())
    print("\nAccuracy: ", accuracy)
    print("\n신뢰도: {:.2f}%".format(accuracy*100))


if __name__ == '__main__':
    displayLearning(
        start_learning(
            setting_DeepLearning()
        )
    )

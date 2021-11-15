import os
import torch
from torch.autograd import Variable
import numpy as np


def path():
    return os.path.dirname(os.path.abspath(__file__))


def modelFile():
    return os.path.join(path(), "model/model_static.pt")


def csvFile():
    return os.path.join(path(), "pima-diabetes-data.csv")


def saveModel(model):
    torch.save(model.state_dict(), modelFile())


def LoadModel(model):
    model.load_state_dict(torch.load(modelFile()))
    model.eval()

    return model


def setting_DeepLearning():
    torch.manual_seed(777)  # for reproducibility

    xy = np.loadtxt(csvFile(), delimiter=',', dtype=np.float32)
    x_train_data = xy[:388, 0:-1]
    y_train_data = xy[:388, [-1]]

    x_test_data = xy[389:, 0:-1]
    y_test_data = xy[389:, [-1]]

    global X_train
    global Y_train

    X_train = Variable(torch.from_numpy(x_train_data))
    Y_train = Variable(torch.from_numpy(y_train_data))

    global X_Test
    global Y_Test

    X_Test = Variable(torch.from_numpy(x_test_data))
    Y_Test = Variable(torch.from_numpy(y_test_data))

    # Hypothesis using sigmoid
    linear = torch.nn.Linear(8, 1, bias=True)
    #sigmoid = torch.nn.Sigmoid()
    tanh = torch.nn.Tanh()
    model = torch.nn.Sequential(linear, tanh)

    # model = LoadModel(model)

    return model


def start_learning(learning_model):
    #optimizer = torch.optim.SGD(learning_model.parameters(), lr=0.01)
    optimizer = torch.optim.Adam(learning_model.parameters(), lr=0.01, betas=(
        0.9, 0.999), amsgrad=False)

    for step in range(601):
        optimizer.zero_grad()
        hypothesis = learning_model(X_train)
        # cost/loss function
        cost = -(Y_train * torch.log(hypothesis) + (1 - Y_train)
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
    predicted = (model(X_Test).data > 0.5).float()
    accuracy = (predicted == Y_Test.data).float().mean()

    #print("\nHypothesis: ", hypothesis.data.reshape(11, 3, 23).numpy())
    #print("\nCorrect (Y): ", predicted.reshape(11, 3, 23).numpy())
    print("\nAccuracy: ", accuracy)


if __name__ == '__main__':
    displayLearning(
        start_learning(
            setting_DeepLearning()
        )
    )

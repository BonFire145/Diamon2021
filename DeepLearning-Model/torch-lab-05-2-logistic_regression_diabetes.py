import os
import torch
from torch.autograd import Variable
import numpy as np

path = os.path.dirname(os.path.abspath(__file__))
modelFile = os.path.join(path, "model/model_static.pt")
csvFile = os.path.join(path, "data-03-diabetes.csv")

torch.manual_seed(777)  # for reproducibility

xy = np.loadtxt(csvFile, delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

# Make sure the shape and data are OK
print(x_data.shape, y_data.shape)

X = Variable(torch.from_numpy(x_data))
Y = Variable(torch.from_numpy(y_data))

# Hypothesis using sigmoid
linear = torch.nn.Linear(8, 1, bias=True)
sigmoid = torch.nn.Sigmoid()
model = torch.nn.Sequential(linear, sigmoid)

# Load Model
model.load_state_dict(torch.load(modelFile))
model.eval()

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for step in range(10001):
    optimizer.zero_grad()
    hypothesis = model(X)
    # cost/loss function
    cost = -(Y * torch.log(hypothesis) + (1 - Y)
             * torch.log(1 - hypothesis)).mean()
    cost.backward()
    optimizer.step()

    if step % 200 == 0:
        print(step, cost.data.numpy())

# Accuracy computation
predicted = (model(X).data > 0.5).float()
accuracy = (predicted == Y.data).float().mean()
print("\nHypothesis: ", hypothesis.data.numpy(), "\nCorrect (Y): ",
      predicted.numpy(), "\nAccuracy: ", accuracy)
print("신뢰도: {:.2f}%".format(accuracy*100))

# Save Model
torch.save(model.state_dict(), modelFile)

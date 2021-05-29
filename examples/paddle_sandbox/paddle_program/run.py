import paddle
from PyQt5 import QtCore

layer = paddle.nn.Linear(in_features=1, out_features=1)

loss_func = paddle.nn.MSELoss()
opt = paddle.optimizer.SGD(learning_rate=0.001, parameters=layer.parameters())

for i in range(5):
    loss = None
    for data in range(10):
        y_predict = layer(paddle.to_tensor([data], dtype="float32"))
        loss = loss_func(y_predict, paddle.to_tensor([data * 3], dtype="float32"))
        loss.backward()
        opt.step()
        opt.clear_grad()
    print("Epoch:", i, "loss:", loss.numpy())

input("测试成功！")
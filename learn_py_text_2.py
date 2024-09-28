# 模拟生成accuracy逐步上升、loss逐步下降的日志

import random

epoch = 100
accuracy = 0.5
loss = 0.9

with open("resources/training_log.txt", "w") as f:
    f.write("Epoch\tAccuracy\tLoss\n")

    for epoch_i in range(1, epoch + 1):
        accuracy += random.uniform(
            0, 0.005
        )  # random.uniform(a, b) 生成一个[a, b)范围的浮点数
        loss -= random.uniform(0, 0.005)

        accuracy = min(1, accuracy)
        loss = max(0, loss)

        f.write(f"{epoch_i}\t{accuracy:.3f}\t{loss:.3f}\n")
        print(f"Epoch: {epoch_i}, Accuracy: {accuracy}, Loss: {loss}")

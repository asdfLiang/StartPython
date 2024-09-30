# # 读取文件
# with open("resources/training_log.txt", "r") as file:
#     print(file.read())

# print("==========================================================")
# # 按行读取文件
# with open("resources/training_log.txt", "r") as file:
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())

# # 写入，多次执行不会追加内容，而是覆盖
# with open("resources/example_1.txt", "w") as file:
#     file.write("Hello World!")

# # 写入多行，多次写入不会追加内容，而是覆盖
# lines = ["Hello World!", "Welcome to Python programming"]
# with open("resources/example_2.txt", "w") as file:
#     file.writelines(line + "\n" for line in lines)


##############################################################################
import random

""" 
    模拟生成accuracy逐步上升、loss逐步下降的日志
"""

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

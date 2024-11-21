import numpy as np

# 向量（一维）
vector = np.array([1, 2, 3, 4, 5])
vector_norm = np.linalg.norm(vector)
print("Vector: \n", vector)
print("Vector L2 Norm：", vector_norm)

# 矩阵（二维）
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_norm = np.linalg.norm(matrix)
print("matrix：\n", matrix)
print("Matrix L2 Norm：", matrix_norm)

# 张量（多维）
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
tensor_norm = np.linalg.norm(tensor)
print("Tensor：\n", tensor)
print("Tensor L2 Norm：", tensor_norm)

import math

import numpy as np


def four_dot_one():
    array1 = np.array([10, 100, 1000.])
    array2 = np.array([[1., 2., 3.], [4., 5., 6.]])
    # print(array1.dtype)  # float64
    # print(array1[0]) # 10.0
    # print(array2 + 1)
    # print(array2 * array2)
    # print(array2 * array1)

    # 嵌套循环来计算每个元素的平方根，然后再把结果构造成一个NumPy数组
    # print(np.array([[math.sqrt(i) for i in row] for row in array2]))
    #
    # print(np.sqrt(array2))
    print(array2.sum(axis=0))  # [5. 7. 9.] 返回一维数组
    print(array2.sum())  # 21.0 数组之和


def four_dot_two():
    array1 = np.array([10, 100, 1000.])
    array2 = np.array([[1., 2., 3.], [4., 5., 6.]])
    # print(array1[2]) # 1000.0 返回标量
    # print(array2[0, 0]) # 1.0 返回标量
    # print(array2[:, 1:])
    # print(array2[:, 1])
    # print(array2[1, :2])
    # print(np.arange(2 * 5).reshape(2, 5))  # np.arange(10).reshape(2, 5)
    # print(np.random.randn(2, 3))
    print(array2, '\n')
    subset = array2[:, :2].copy()
    print(subset, '\n')

    subset[0, 0] = 1000
    print(subset, '\n')
    print(array2)


def main():
    # four_dot_one()
    four_dot_two()


if __name__ == '__main__':
    main()

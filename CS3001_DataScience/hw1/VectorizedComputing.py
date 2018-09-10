import numpy

x = numpy.array([[1,  2,  3,  4],
                 [5,  6,  7,  8],
                 [9,  10, 11, 12],
                 [13, 14, 15, 16]])

if __name__=="__main__":
    # a
    y = x[:, 2] 
    print("a")
    print(y)

    # b
    y = x[-1, :2]
    print("b")
    print(y)

    # c
    y = x[:, [True, False, False, True]]
    print("c")
    print(y)

    # d
    y = x[0:2, 0:2]
    print("d")
    print(y)

    # e
    y = x[[0, 1, 2], [0, 1, 2]]
    print("e")
    print(y)

    # f
    y = x[0]**2
    print("f")
    print(y)

    # g
    y = x.max(axis=1)
    print("g")
    print(y)

    # h
    y = x[:2, :2] + x[:2, 2:]
    print("h")
    print(y)

    # i
    y = x[:2, :3].T
    print("i")
    print(y)

    # j
    y = x[:2, :3].reshape((3,2))
    print("j")
    print(y)

    # k
    y = x[:, :2].dot([1, 1])
    print("k")
    print(y)

    # l
    y = x[:, :2].dot([[3, 0], [0, 2]])
    print("l")
    print(y)
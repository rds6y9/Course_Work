import matplotlib.pyplot as plt
from SummaryStats import generateResults

def VisualA():
    ssA, ssB, ssC = generateResults()
    
    print(ssA)
    print(ssB)
    print(ssC)

    # Our standard categorical x-axis
    x_axis = ['Data 1', 'Data 2', 'Data 3']
    
    plt.scatter(x_axis, [ssA[0], ssB[0], ssC[0]], marker="v", c="k")
    plt.scatter(x_axis, [ssA[1], ssB[1], ssC[1]], marker="^", c="k")
    plt.scatter(x_axis, [ssA[2], ssB[2], ssC[2]], marker="+", c="b")
    plt.scatter(x_axis, [ssA[2] + ssA[3], ssB[2] + ssB[3], ssC[2] + ssC[3]], marker="v", c="g")
    plt.scatter(x_axis, [ssA[2] - ssA[3], ssB[2] - ssB[3], ssC[2] - ssC[3]], marker="^", c="g")
    plt.scatter(x_axis, [ssA[4], ssB[4], ssC[4]], marker="x", c="b")
    plt.scatter(x_axis, [ssA[5], ssB[5], ssC[5]], marker="^", c="r")
    plt.scatter(x_axis, [ssA[6], ssB[6], ssC[6]], marker="v", c="r")
    plt.show()


if __name__=='__main__':
    VisualA()
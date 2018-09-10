import matplotlib.pyplot as plt
from SummaryStats import generateResults
from Normalize import generateNormalizedData, countOccurences

def VisualA():
    ssA, ssB, ssC = generateResults()
    
    print(ssA)
    print(ssB)
    print(ssC)

    # Our standard categorical x-axis
    x_axis = ['Data 1', 'Data 2', 'Data 3']

    plt.scatter(x_axis, [ssA[0], ssB[0], ssC[0]], marker="v", c="k", label="max")
    plt.scatter(x_axis, [ssA[1], ssB[1], ssC[1]], marker="^", c="k", label="min")
    plt.scatter(x_axis, [ssA[2], ssB[2], ssC[2]], marker="+", c="b", label="mean")
    plt.scatter(x_axis, [ssA[2] + ssA[3], ssB[2] + ssB[3], ssC[2] + ssC[3]], marker="v", c="g", label="mean+std")
    plt.scatter(x_axis, [ssA[2] - ssA[3], ssB[2] - ssB[3], ssC[2] - ssC[3]], marker="^", c="g", label="mean-std")
    plt.scatter(x_axis, [ssA[4], ssB[4], ssC[4]], marker="x", c="b", label="median")
    plt.scatter(x_axis, [ssA[5], ssB[5], ssC[5]], marker="^", c="r", label="25 perc")
    plt.scatter(x_axis, [ssA[6], ssB[6], ssC[6]], marker="v", c="r", label="75 perc")

    plt.legend()

    plt.show()

def VisualB():
    listA, listB, listC = generateNormalizedData()
    freqA, freqB, freqC = countOccurences(listA), countOccurences(listB), countOccurences(listC)

    print(freqA)
    print(freqB)
    print(freqC)

    plt.plot(freqA.keys(), freqA.values(), marker='.', linestyle="-", c="r", label="Rescaled Data 1")
    plt.plot(freqB.keys(), freqB.values(), marker='+', linestyle="-.", c="g", label="Rescaled Data 2")
    plt.plot(freqC.keys(), freqC.values(), marker='x', linestyle=":", c="b", label="Rescaled Data 3")

    plt.legend()
    plt.show()

if __name__=='__main__':
    VisualA()
    VisualB()
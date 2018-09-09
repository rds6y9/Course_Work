import matplotlib
from SummaryStats import generateResults

def VisualA():
    ssA, ssB, ssC = generateResults()
    
    print(ssA[0])
    print(ssB[0])
    print(ssC[0])

if __name__=='__main__':
    VisualA()
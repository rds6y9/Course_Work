from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier

import pandas as pd
import pickle

def testModel(data):
    # Testing CART Decision Tree
    with open('decisionTree.txt', 'rb') as f:
        loadedModel = pickle.load(f)
    
    print("Decision Tree Results: ")
    print(loadedModel.predict(data))

    # Testing kNN Classifier
    with open('classifier.txt', 'rb') as f:
        loadedModel = pickle.load(f)
    
    print("kNN Classifier Results: ")
    print(loadedModel.predict(data))

if __name__ == "__main__":
    testModel()
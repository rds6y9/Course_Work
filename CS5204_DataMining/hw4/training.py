from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier

import pandas as pd
import pickle

def trainModel(data, target):
    # Getting Iris Data
    trainData = pd.read_csv("iris.txt")

    features = list(trainData.columns[0:4])
    label = list(trainData.columns[4:5])

    data = trainData[features]
    target = trainData[label]
    
    # CART Decision Tree
    model = tree.DecisionTreeClassifier()
    model.fit(data, target)

    # Save model to file
    with open('decisionTree.txt', 'wb') as f:
        pickle.dump(model, f)

    # kNN Classifier Trainer
    neigh = KNeighborsClassifier()
    neigh.fit(data, target['class'])

    with open('classifier.txt', 'wb') as f:
        pickle.dump(neigh, f)

if __name__ == "__main__":
    trainModel()



    # Open file
    # with open('decisionTree.txt', 'rb') as f:
    #     loadedModel = pickle.load(f)
from sklearn import tree
from sklearn.naive_bayes import GaussianNB

import pandas as pd

def Question1():
    gnb = GaussianNB()

    trainData = pd.read_csv("traindata.txt")
    testData = pd.read_csv("testdata.txt")

    features = list(trainData.columns[2:5])
    label = list(trainData.columns[5:6])

    testFeatures = list(testData.columns[2:5])
    actualResults = list(testData['Label'])

    # Removing Unnecessary Columns
    trainData = trainData.drop('Date', axis=1)
    testData = testData.drop('Date', axis=1)

    # Mapping Categorical Columns to Continuous for Scikit-learn
    trainData['Media'] = trainData['Media'].map({'1-NBC':0, '2-ESPN':1,'3-FOX':2, '4-ABC':3, '5-CBS':4})
    trainData['Is_Home_or_Away'] = trainData['Is_Home_or_Away'].map({'Home':0, 'Away':1})
    trainData['Is_Opponent_in_AP25_Preseason'] = trainData['Is_Opponent_in_AP25_Preseason'].map({'In':0, 'Out':1})

    testData['Media'] = testData['Media'].map({'1-NBC':0, '2-ESPN':1,'3-FOX':2, '4-ABC':3, '5-CBS':4})
    testData['Is_Home_or_Away'] = testData['Is_Home_or_Away'].map({'Home':0, 'Away':1})
    testData['Is_Opponent_in_AP25_Preseason'] = testData['Is_Opponent_in_AP25_Preseason'].map({'In':0, 'Out':1})

    data = trainData[features]
    target = trainData['Label']

    testData = testData[testFeatures]

    # Generate Naive Bayes Results 
    
    testResults = gnb.fit(data, target).predict(testData)
    
    accuracy_result = calculate_accuracy(actualResults, testResults)
    precision_result = calculate_precision(actualResults, testResults)
    recall_result = calculate_recall(actualResults, testResults)

    print(testResults)
    print(actualResults)

    print("----------- Performance of Naive Baysian ------------")
    print(str(accuracy_result) + "% Accuracy")
    print(str(precision_result) + "% Precision")
    print(str(recall_result) + "% Recall")
    print(str(2 * ((precision_result * recall_result) / (precision_result + recall_result))) + " f1 score")

    # ID3 Comparison

    model = tree.DecisionTreeClassifier(criterion='entropy')
    model.fit(data, target)
    testResults = model.predict(testData)

    accuracy_result = calculate_accuracy(actualResults, testResults)
    precision_result = calculate_precision(actualResults, testResults)
    recall_result = calculate_recall(actualResults, testResults)

    print(testResults)
    print(actualResults)

    print("----------- Performance of ID3 Decision Tree ------------")
    print(str(accuracy_result) + "% Accuracy")
    print(str(precision_result) + "% Precision")
    print(str(recall_result) + "% Recall")
    print(str(2 * ((precision_result * recall_result) / (precision_result + recall_result))) + " f1 score")

    # CART Comparison

    model = tree.DecisionTreeClassifier()
    model.fit(data, target)
    testResults = model.predict(testData)

    accuracy_result = calculate_accuracy(actualResults, testResults)
    precision_result = calculate_precision(actualResults, testResults)
    recall_result = calculate_recall(actualResults, testResults)

    print(testResults)
    print(actualResults)

    print("----------- Performance of CART Decision Tree ------------")
    print(str(accuracy_result) + "% Accuracy")
    print(str(precision_result) + "% Precision")
    print(str(recall_result) + "% Recall")
    print(str(2 * ((precision_result * recall_result) / (precision_result + recall_result))) + " f1 score")


    
def calculate_accuracy(list_1, list_2):
    matches = 0
    for _ in range(len(list_1)):
        if list_1[_] == list_2[_]:
            matches += 1
    return (matches / len(list_1)) * 100

def calculate_precision(list_1, list_2):
    matches = 0
    for _ in range(len(list_1)):
        if list_1[_] == list_2[_]:
            matches += 1
    
    false_pos = 0
    for _ in range(len(list_1)):
        if list_1[_] == 'Lose' and list_2[_] == 'Win':
            false_pos += 1
    return (matches / (matches + false_pos)) * 100

def calculate_recall(list_1, list_2):
    matches = 0
    for _ in range(len(list_1)):
        if list_1[_] == list_2[_]:
            matches += 1
    
    false_neg = 0
    for _ in range(len(list_1)):
        if list_1[_] == 'Win' and list_2[_] == 'Lose':
            false_neg += 1
    return (matches / (matches + false_neg)) * 100
    
if __name__ == "__main__":
    Question1()
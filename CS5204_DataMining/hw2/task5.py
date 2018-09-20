from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer, OneHotEncoder
from subprocess import call

import pandas as pd
import pydot

# Question 1

def Question1():
    # Importing data into acceptable format
    dataset = pd.read_csv("t5q1.txt")
    test_dataset = pd.read_csv("t5q1test.txt")

    features = list(dataset.columns[2:5])
    label = list(dataset.columns[5:6])

    # Store final results before dropping
    test_results = list(test_dataset['Label'])
    print(test_results)

    # Removing Unnecessary Columns
    dataset = dataset.drop('Opponent', axis=1)
    dataset = dataset.drop('Date', axis=1)
    test_dataset = test_dataset.drop('Opponent', axis=1)
    test_dataset = test_dataset.drop('Date', axis=1)
    test_dataset = test_dataset.drop('Label', axis=1)

    # Mapping Categorical Columns to Continuous for Scikit-learn
    dataset['Is_Home_or_Away'] = dataset['Is_Home_or_Away'].map({'Home':0, 'Away':1})
    dataset['Is_Opponent_in_AP25_Preseason'] = dataset['Is_Opponent_in_AP25_Preseason'].map({'Out':0, 'In':1})
    dataset['Media'] = dataset['Media'].map({'1-NBC':0, '2-ESPN':1, '3-FOX':2, '4-ABC':3, '5-CBS':4})

    test_dataset['Is_Home_or_Away'] = test_dataset['Is_Home_or_Away'].map({'Home':0, 'Away':1})
    test_dataset['Is_Opponent_in_AP25_Preseason'] = test_dataset['Is_Opponent_in_AP25_Preseason'].map({'Out':0, 'In':1})
    test_dataset['Media'] = test_dataset['Media'].map({'1-NBC':0, '2-ESPN':1, '3-FOX':2, '4-ABC':3, '5-CBS':4})

    data = dataset[features]
    target = dataset['Label']

    x_train, x_test, y_train, y_test = train_test_split(data, target, random_state=1)

    # ### ID3 Decision Tree Generation
    model = tree.DecisionTreeClassifier(criterion='entropy')
    model.fit(data, target)

    tree.export_graphviz(model, out_file='q1_5ID3tree.dot', feature_names=features)
    call(["dot", "-Tpng", "q1_5ID3tree.dot", "-o", "q1_5ID3tree.png"])

    predict = list(model.predict(test_dataset))
    print(predict)

    accuracy_result = calculate_accuracy(test_results, predict)
    precision_result = calculate_precision(test_results, predict)
    recall_result = calculate_recall(test_results, predict)
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
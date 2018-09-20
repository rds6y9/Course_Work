from sklearn import tree
from sklearn.preprocessing import LabelBinarizer, OneHotEncoder
from subprocess import call

import pandas as pd
import pydot

# Question 1

def Question1():
    # Importing data into acceptable format
    dataset = pd.read_csv("t4q1.txt")

    features = list(dataset.columns[2:5])
    label = list(dataset.columns[5:6])

    # Removing Unnecessary Columns
    dataset = dataset.drop('University', axis=1)
    dataset = dataset.drop('Date', axis=1)

    # Mapping Categorical Columns to Continuous for Scikit-learn
    dataset['Media'] = dataset['Media'].map({'1-NBC':0, '2-ESPN':1,'3-FOX':2, '4-ABC':3})
    dataset['Is Home/Away?'] = dataset['Is Home/Away?'].map({'Home':0, 'Away':1})
    dataset['Is Opponent in AP Top 25 at Preseason?'] = dataset['Is Opponent in AP Top 25 at Preseason?'].map({'In':0, 'Out':2})

    data = dataset[features]
    target = dataset['Label: Win/Lose']

    ### CART Decision Tree Generation 
    model = tree.DecisionTreeClassifier()
    model.fit(data, target)

    tree.export_graphviz(model, out_file='q1CARTtree.dot', feature_names=features)
    call(["dot", "-Tpng", "q1CARTtree.dot", "-o", "q1CARTtree.png"])

    ### ID3 Decision Tree Generation
    model = tree.DecisionTreeClassifier(criterion='entropy')
    model.fit(data, target)

    tree.export_graphviz(model, out_file='q1ID3tree.dot', feature_names=features)
    call(["dot", "-Tpng", "q1ID3tree.dot", "-o", "q1ID3tree.png"])


def Question2():
    # Importing data into acceptable format
    dataset = pd.read_csv("t4q2.txt")

    features = list(dataset.columns[1:5])
    label = list(dataset.columns[5:6])

    print(features)
    print(label)

    # Removing Unnecessary Columns
    dataset = dataset.drop('Date', axis=1)

    # Mapping Categorical Columns to Continuous for Scikit-learn
    dataset['Outlook'] = dataset['Outlook'].map({'Sunny':0, 'Overcast':1, 'Rainy':2})
    dataset['Temperature'] = dataset['Temperature'].map({'Hot':0, 'Mild':1, 'Cool':2})
    dataset['Humidity'] = dataset['Humidity'].map({'High':0, 'Normal':1})

    print(dataset['Windy'])
    dataset['Windy'] = dataset['Windy'].map({False:0, True:1})
    print(dataset['Windy'])

    data = dataset[features]
    target = dataset['Label: Play?']

    ### CART Decision Tree Generation 
    model = tree.DecisionTreeClassifier()
    model.fit(data, target)

    tree.export_graphviz(model, out_file='q2CARTtree.dot', feature_names=features)
    call(["dot", "-Tpng", "q2CARTtree.dot", "-o", "q2CARTtree.png"])

    ### ID3 Decision Tree Generation
    model = tree.DecisionTreeClassifier(criterion='entropy')
    model.fit(data, target)

    tree.export_graphviz(model, out_file='q2ID3tree.dot', feature_names=features)
    call(["dot", "-Tpng", "q2ID3tree.dot", "-o", "q2ID3tree.png"])

if __name__ == "__main__":
    Question1()
    Question2()

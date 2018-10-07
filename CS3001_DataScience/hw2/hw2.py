# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 21:40:59 2018

@author: Ryan Stoughton
@assignment: Homework 1 Problem 3
@course: CS5204 Data Mining w/ Dr. Fu

All code was run in the Spyder IDE
"""

from collections import Counter

import matplotlib.pyplot as plt
import numpy
import pandas as pd
import statistics as stats

train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
all_data = pd.concat([train_df, test_df], sort=True)

# Question 1 - Features available in the dataset
# This can simply be achieved by looking at the column names of the data frame.

print("\n~ Q1 ~")
print("The features available in the dataset are: ")
for feature in list(all_data.columns):
    print(feature)
    
# Question 2 - Which features are categorical?
# Categorical can't be purely checked by code. Hard coded values for columns
# that contain categorical data.
    
print("\n~ Q2 ~")
print("The features that are categorical in the dataset are: ")
print("PassengerId")
print("Survived")
print("Pclass")
print("Name")
print("Sex")
print("Cabin")
print("Embarked")

# Question 3 - Which features are numerical?
# Numerical can't be purely checked by code. Hard coded values for columns
# that contain numerical data.

print("\n~ Q3 ~")
print("The features that are numerical in the dataset are: ")
print("Age")
print("SibSp")
print("Parch")
print("Fare")

    
# Question 4 - Which features are mixed data types?

print("\n~ Q4 ~")
print("The features that are mixed in the dataset are: ")
print("Ticket")

# Question 5 - Which features contain blank, null, or empty values?
 
print("\n~ Q5 ~")
print("The features with blank, null, or empty values.")
for feature in list(all_data.columns):
    if all_data.isnull().get(feature).any():
        print(feature)

# Question 6 - What are the data types?
        
print("\n~ Q6 ~")
print("The datatypes of each feature: ")
for feature in list(all_data.columns):
    print(feature + " : " + type(train_df.get(feature)[0]).__name__)
    
# Question 7 - Stats of numerical values
print("\n~ Q7 ~")
print("The summary statistics of each numerical feature: ")
for feature in ["Age", 
                "SibSp", 
                "Parch", 
                "Fare"]:
    cleaned_col = list(filter(lambda a: str(a) != 'nan', all_data.get(feature)))
    print("Count of " + feature + ": " + str(len(cleaned_col)))
    print("Mean of " + feature + ": " + str((sum(cleaned_col) / len(cleaned_col))))
    print("Standard Deviation of " + feature + ": " + str(stats.pstdev(cleaned_col)))
    print("Min of " + feature + ": " + str(min(cleaned_col)))
    print("25th Percentile of " + feature + ": " 
          + str(numpy.percentile(numpy.array(cleaned_col), 25)))
    print("50th Percentile of " + feature + ": " 
          + str(numpy.percentile(numpy.array(cleaned_col), 50)))
    print("75th Percentile of " + feature + ": " 
          + str(numpy.percentile(numpy.array(cleaned_col), 75)))
    print("Max of " + feature + ": " + str(max(cleaned_col)))
    print("")

# Question 8 - Distribution of categorical features
print("\n~ Q8 ~")
print("The distribution of categorical features: ")
for feature in ["PassengerId", 
                "Survived", 
                "Pclass", 
                "Name", 
                "Sex", 
                "Cabin", 
                "Embarked"]:
    cleaned_col = list(filter(lambda a: str(a) != 'nan', all_data.get(feature)))
    print("Count of " + feature + ": " + str(len(cleaned_col)))
    print("Unique values of " + feature + ": " + str(len(set(cleaned_col))))
    most_common_value = Counter(cleaned_col).most_common(1)
    print("Top value of " + feature + ": " + str(most_common_value[0][0]))
    print("Frequency of top value of " + feature + ": " + str(most_common_value[0][1]))
    print("")
    
# Question 9 - Significant correlation (>0.5) among Pclass=1 and Survived?
print("\n~ Q9 ~")
print("Significant correlation among Pclass=1 and Survived")

relevant_data = train_df.loc[pd.notnull(train_df['Survived'])]
relevant_data = relevant_data[['Survived', 'Pclass']]

print(relevant_data.corr(method='pearson'))
print("\n\nBased on an r value of roughly -0.33848, significant correlation cannot be " +
      "observed and therefore Pclass will not be included in the predictive model.")

# Question 10 - Are women more likely to have survived?
print("\n~ Q10 ~")
print("Are women more likely to have survived?")

relevant_data = train_df[['Sex', 'Survived']]

women_data = relevant_data.loc[relevant_data['Sex'] == 'female']
men_data = relevant_data.loc[relevant_data['Sex'] == 'male']

women_surv = len(list(filter(lambda a: a == 1, women_data.get('Survived'))))
men_surv = len(list(filter(lambda a: a == 1, men_data.get('Survived'))))

print("Percentage of women survived: " + str(100 * (women_surv / len(women_data.index))) + "%")
print("Percentage of men survived: " + str(100* (men_surv / len(men_data.index))) + "%")
print("\nWomen were more likely to survive.")

# Question 11 - Age / Survived Graphs
print("\n~ Q11 ~")
print("Age / Survived Graphs")

relevant_data = train_df[['Age', 'Survived']]
relevant_data = relevant_data.dropna(how='any', axis=0)

age_surv = relevant_data[relevant_data['Survived'] == 1].get('Age')
age_no_surv = relevant_data[relevant_data['Survived'] == 0].get('Age')

n, bins, patches = plt.hist(age_surv, 25, density=True)

plt.title("Survived = 1")
plt.xlabel("Age")
plt.ylabel("Number Survived")
plt.show()

n, bins, patches = plt.hist(age_no_surv, 25, density=True)

plt.title("Survived = 0")
plt.xlabel("Age")
plt.ylabel("Number Survived")
plt.show()

# Question 12 - Age / Pclass / Survived Graphs
print("\n~ Q12 ~")
print("Age / Pclass / Survived Graphs")

relevant_data = train_df[['Age', 'Pclass', 'Survived']]
relevant_data = relevant_data.dropna(how='any', axis=0)

age_surv_pclass1 = relevant_data[relevant_data['Survived'] == 1]
age_surv_pclass1 = age_surv_pclass1[age_surv_pclass1['Pclass'] == 1].get('Age')

n, bins, patches = plt.hist(age_surv_pclass1, 20, density=True)

plt.title("Pclass = 1 | Survived = 1")
plt.xlabel("Age")
plt.ylabel("Number Survived")

age_surv_pclass1.hist(bins=20)
plt.show()

age_nosurv_pclass1 = relevant_data[relevant_data['Survived'] == 0]
age_nosurv_pclass1 = age_nosurv_pclass1[age_nosurv_pclass1['Pclass'] == 1].get('Age')

n, bins, patches = plt.hist(age_nosurv_pclass1, 20, density=True)

plt.title("Pclass = 1 | Survived = 0")
plt.xlabel("Age")
plt.ylabel("Number Survived")

age_nosurv_pclass1.hist(bins=20)
plt.show()

age_surv_pclass2 = relevant_data[relevant_data['Survived'] == 1]
age_surv_pclass2 = age_surv_pclass2[age_surv_pclass2['Pclass'] == 2].get('Age')

n, bins, patches = plt.hist(age_surv_pclass2, 20, density=True)

plt.title("Pclass = 2 | Survived = 1")
plt.xlabel("Age")
plt.ylabel("Number Survived")

age_surv_pclass2.hist(bins=20)
plt.show()

age_nosurv_pclass2 = relevant_data[relevant_data['Survived'] == 0]
age_nosurv_pclass2 = age_nosurv_pclass2[age_nosurv_pclass2['Pclass'] == 2].get('Age')

n, bins, patches = plt.hist(age_nosurv_pclass2, 20, density=True)

plt.title("Pclass = 2 | Survived = 0")
plt.xlabel("Age")
plt.ylabel("Number Survived")

age_nosurv_pclass2.hist(bins=20)
plt.show()

age_surv_pclass3 = relevant_data[relevant_data['Survived'] == 1]
age_surv_pclass3 = age_surv_pclass3[age_surv_pclass3['Pclass'] == 3].get('Age')

n, bins, patches = plt.hist(age_surv_pclass3, 20, density=True)

plt.title("Pclass = 3 | Survived = 1")
plt.xlabel("Age")
plt.ylabel("Number Survived")

age_surv_pclass3.hist(bins=20)
plt.show()

age_nosurv_pclass3 = relevant_data[relevant_data['Survived'] == 0]
age_nosurv_pclass3 = age_nosurv_pclass3[age_nosurv_pclass3['Pclass'] == 3].get('Age')

n, bins, patches = plt.hist(age_nosurv_pclass3, 20, density=True)

plt.title("Pclass = 3 | Survived = 0")
plt.xlabel("Age")
plt.ylabel("Number Survived")

age_nosurv_pclass3.hist(bins=20)
plt.show()

# Question 13
print("\n~ Q13 ~")

# Question 14
print("\n~ Q14 ~")
print("Drop Tickets from model?")

ticket_col = list(all_data.get('Ticket'))
ticket_count = Counter(ticket_col).most_common()
print("Percent unique tickets: " + str(100 * len(ticket_count) / len(ticket_col)) + "%")

# Question 15
print("\n~ Q15 ~")
print("How many nulls in Cabin?")

cabin_col = all_data.get('Cabin')
num_null_vals = cabin_col.isnull().sum()
print(str(num_null_vals) + " null values in Cabin column out of " + str(len(list(cabin_col))) + ".")

# Question 16
print("\n~ Q16 ~")
sex_col = all_data.get('Sex')
print("\nColumn Before: \n\n" + str(sex_col))

sex_col = sex_col.replace('male', 0)
sex_col = sex_col.replace('female', 1)

all_data['Gender'] = sex_col
print("\nColumn Before: \n\n" + str(sex_col))

# Question 17
print("\n~ Q17 ~")

# Question 18 - Fill in missing embarked values
print("\n~ Q18 ~")
print("Filling in missing Embarked values")

most_common_embark = Counter(train_df.get('Embarked')).most_common(1)[0][0]
print("Most Common Embarking point: " + str(most_common_embark))

train_df['Embarked'] = train_df['Embarked'].fillna(most_common_embark)

# Question 19 - Fill in missing Fare value
print("\n~ Q19 ~")
print("Filling in missing Fare value")

fare_col = list(test_df.get('Fare'))
mode_fare_val = Counter(fare_col).most_common(1)[0][0]
print("Missing Fare Value: " + str(mode_fare_val))

test_df['Fare'] = test_df['Fare'].fillna(mode_fare_val)

# Question 20
print("\n~ Q20 ~")
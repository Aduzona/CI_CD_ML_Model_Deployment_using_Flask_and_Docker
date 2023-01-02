import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
import joblib # to save the model

df = pd.read_csv("breast_cancer.csv")
df['target']=df['target'].astype(int)

y=df['target']
X=df.drop('target',axis=1)

from sklearn.model_selection import train_test_split
# Splitting the dataset in train and test data with 80:20 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# Importing the SVC model from sklearn
from sklearn.svm import SVC

# Importing confusion matrix and classification report to get accuarcy of our model
#from sklearn.metrics import classification_report, confusion_matrix

svc_model = SVC()
# fitting the model to the training dataset
svc_model.fit(X_train, y_train)

# Predicting the model using the Test dataset
#y_pred = svc_model.predict(X_test)

# Creating the confusion matrix
#cm = confusion_matrix(y_test,y_pred)

#from sklearn.metrics import accuracy_score
#print(accuracy_score(y_test,y_pred))

model_filename='model.pkl'
joblib.dump(svc_model,model_filename)
import joblib

model=joblib.load('model.pkl')
import pandas as pd
new_df = pd.read_csv("breast_cancer.csv")

new_df['target']=new_df['target'].astype(int)
data=new_df.drop('target',axis=1)#remove target column
data=data.iloc[-1:,:]# get last row and all columns
pred = model.predict(data)
print(pred)
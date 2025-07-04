import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


df = pd.read_csv(r'D:\AIML_python\ML_project\introvertextrovert\personality_dataset.csv')

df = df.dropna()
# print(df.isnull().sum())
# print(df.info())
# print(df.head())
# print(df.columns)

def repl(x):
    if (x == 'Yes'):
        return 1
    else:
        return 0

df['Stage_fear'] = df['Stage_fear'].apply(repl)
df['Drained_after_socializing'] = df['Drained_after_socializing'].apply(repl)
df['Personality'] = df['Personality'].apply(lambda x: 1 if x=="Introvert" else 0)


x_train,x_test,y_train,y_test = train_test_split(df.drop(['Personality'],axis=1),df['Personality'],test_size=0.3,random_state=10)

transformer = ColumnTransformer(transformers=[('scaling',MinMaxScaler(),['Time_spent_Alone',  'Social_event_attendance',
       'Going_outside',  'Friends_circle_size',
       'Post_frequency'])],remainder='passthrough')

x_train_transformed = transformer.fit_transform(x_train)
x_test_transformed = transformer.transform(x_test)

logr = LogisticRegression()
logr.fit(x_train_transformed,y_train)

# y_pred = logr.predict(x_test_transformed)
# print("Accuracy - ", accuracy_score(y_test, y_pred))

# ['Time_spent_Alone', 'Stage_fear', 'Social_event_attendance',
#        'Going_outside', 'Drained_after_socializing', 'Friends_circle_size',
#        'Post_frequency', 'Personality']

tsa = int(input("Hours spent alone daily (0–11) "))
sf = int(input("Fear of public speaking (Yes = 1/No = 0) "))
sea = int(input("Frequency of social events (0–10) "))
go = int(input('Frequency of going outside (0–7) '))
das = int(input("Feeling drained after socializing (Yes = 1/No = 0) "))
fcs =int(input('Number of close friends (0–15) '))
pf = int(input("Social media post frequency (0–10) "))

new_d = pd.DataFrame({
    'Time_spent_Alone' : [tsa],
    'Stage_fear' : [sf],
    'Social_event_attendance' : [sea],
    'Going_outside' : [go],
    'Drained_after_socializing' : [das],
    'Friends_circle_size' : [fcs],
    'Post_frequency' : [pf]
})

new_d_trnf = transformer.transform(new_d)
custm_predict = logr.predict(new_d_trnf)
custm_proba = logr.predict_proba(new_d_trnf)

print("Predicted Personality:", "Introvert" if custm_predict[0] == 1 else "Extrovert")
print(f"Confidence: Introvert: {custm_proba[0][1]*100:.2f}%, Extrovert: {custm_proba[0][0]*100:.2f}%")


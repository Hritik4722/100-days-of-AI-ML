import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

df = pd.read_csv(r'D:\AIML_python\ML_project\Life-Expectancy-Data-Updated.csv', usecols=['Country','Year','BMI','Life_expectancy'])
important_countries = ['India','China','Russia','Spain']
df['Country'] = df['Country'].apply(lambda x: x if x in important_countries else 'Other')
# print(df['Country'].value_counts())

###train test split
x_train,x_test,y_train,y_test = train_test_split(df.drop(['Life_expectancy'],axis=1) ,df['Life_expectancy'] , test_size= 0.3,random_state=0)

transformer = ColumnTransformer(transformers=[('trf1',StandardScaler(),['Year','BMI']),
                                              ('trf2',OneHotEncoder(drop='first',sparse_output=False),['Country'])],
                                              remainder='passthrough')
x_train_transformed = transformer.fit_transform(x_train)
x_test_transformed = transformer.transform(x_test)

lr = LinearRegression()
lr.fit(x_train_transformed,y_train)

# y_pred = lr.predict(x_test_transformed)

# print("MAE:", mean_absolute_error(y_test, y_pred))
# print("MSE:", mean_squared_error(y_test, y_pred))
# print("R2 Score:", r2_score(y_test, y_pred))

country = input('India or China or Russia or Spain = ')
year = int(input('Enter year = '))
bmi = int(input('Enter BMI = '))


new_data = pd.DataFrame({
    'Country' : [country],
    'Year': [year],
    'BMI': [bmi]
})
custom_input_transformed = transformer.transform(new_data)
custom_prediction = lr.predict(custom_input_transformed)
print("Predicted Life Expectancy:", round(custom_prediction[0], 2))

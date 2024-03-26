# -*- coding: utf-8 -*-
"""DSMP_2023_WebbApp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oUx2TEjs3maWqEeO01UkqVrUNTGkGnBM

## **1 - Importing Libraries & Utilities**
"""

#!pip install streamlit
#from IPython.display import clear_output
#clear_output()
#import streamlit as st
import pandas as pd
import numpy as np
#from google.colab import files, drive
#from sklearn.preprocessing import LabelEncoder
#import matplotlib.pyplot as plt
#import seaborn as sns
#!pip install prediction
#!pip install joblib
clear_output()
import joblib
#from prediction import predict

#drive.mount('/content/drive')
#path_files = "/content/drive/MyDrive/2023_DSMP_Project/WebApp - StreamLit"

"""## **2 - Setup and Loading Information**"""

data = pd.read_csv('df_.csv')
# Get column names
column_names = list(data.columns)[1:-1]
for col in column_names:
  print(col)

"""## **3 - Building Web App on StreamLit**"""

st.title('Predicting Electricity Prices at the Alberta Region')
st.markdown('This app allows predicting Electricty prices for the Alberta region considering the "Residential", "Commercial" and the "Industrial" Sectors.')

# input for Feature Values
st.sidebar.markdown('<h2 style="color: blue;"> Select the values of input variables to predict the target variable</h2>', unsafe_allow_html=True)
user_input_prediction = {}
for column in column_names:
  #print(column)
  if data[column].dtype != 'O':
    user_input_prediction[column] = st.sidebar.slider(f'Select {column}', float(data[column].min()), float(data[column].max()), float(data[column].mean()))
  else:
    #le = LabelEncoder()
    #data[col] = le.fit_transform(data[col])
    user_input_prediction[column] = ''                 #st.sidebar.selectbox('Select Sector', data[col].unique().tolist())

df = pd.DataFrame()
list_ = sorted(data['Sector'].unique().tolist())
#
for sector_ in list_:
  #print(sector_)
  user_input_prediction['Sector'] = list_.index(sector_)
  df = pd.concat([df, pd.DataFrame([user_input_prediction])], axis = 0, ignore_index=True)
df['Sector'] = df['Sector'].astype('float')

# Load the ML Model
model = joblib.load('lgbm_model.sav')
model.set_params(n_classes=1)
clear_output()

# Predict and display the results
#prediction = model.predict(temp.values.reshape(1, -1))
preds = model.predict(df.values)
st.subheader('Prediction')
st.write(f'The predicted Electricity Price is: {np.round(preds,2)}')

# Predict Button
st.button("Predict Electricity Prices")
#
if st.button("Predict Electricity Prices"):
  result = model.predict(df.values)
  st.text(np.round(preds,2))

# Generate Plot
df_output = pd.DataFrame(np.round(preds,2)).T
df_output.columns = list_
#df_output
#
#

"""fig, ax=plt.subplots(figsize=(8,5))
colors_ = sns.color_palette("deep")
ax = sns.barplot(df_output, palette=colors_)
for i in range(len(list_)):
  ax.bar_label(ax.containers[i], fontsize=10);
#ax.grid(axis='y')
plt.ylabel('Electricity Price - (CAD Cents/KWh)')
plt.show()
st.pyplot(fig)
"""

st.bar_chart(df_output)

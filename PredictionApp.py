# imports
import pickle
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression


# Loading model
model = pickle.load(open('firstbasicmodel.pkl','rb'))

# Loading features
features = pickle.load(open('features.pkl','rb'))

# Caching the model for faster loading
@st.cache

# Application Body
st.title('Salary Prediction')
st.image("""https://github.com/lifepopkay/Tech-Monies/blob/206b25db1766925f3717142bd0f5091b1981240f/jp-valery-lVFoIi3SJq8-unsplash.jpg""")
st.header('Provide your inputs for predicting Salry:')

# selections
jobTitle = st.selectbox('Select Job Title:', list(feature_dict['title scraped for'].keys()))
country = st.selectbox('Select Country:', list(feature_dict['Country'].keys()))
position = st.selectbox('Select Seniority:', list(feature_dict['Position'].keys()))
yearExp = st.number_input('Enter Total Experience (Years):', min_value=1, max_value=25, value=1)
contract = st.selectbox('Select Job Type', list(feature_dict['contract_type'].keys()))
eligibility = st.selectbox('Select Seniority:', list(feature_dict['eligibility'].keys()))

# Prediction & output
if st.button('Predict Salary'):
  dataset = [
    feature_dict['title scraped for'][jobTitle],
    feature_dict['Country'][country],
    feature_dict['Position'][position],
    yearExp
    feature_dict['contract_type'][contract],
    feature_dict['eligibility'][eligibility]
    ]
  df = pd.DataFrame(dataset, columns=[list(features.keys())]
  salary = model.predict(df)
  st.success(f'The predicted ranges from ${salary[0]:.0f} to ${salary[1]:.0f} USD')
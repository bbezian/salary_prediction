import streamlit as st
import pickle
import joblib
import numpy as np 

def load_model():
    with open('saved_steps', 'rb') as file:
        data = joblib.load(file)
    return data


data = load_model()


regressor = data['model']
le_country = data['le_country']
le_education = data['le_education']


def show_predict_page():
    st.title('Software Developer Salary prediction')

    st.write('''We need some information to predict the salary''')


    countries = (
    'United States of America',
    'United Kingdom of Great Britain and Northern Ireland',
    'Other',
    'Australia',
    'Netherlands',
    'Germany',
    'Sweden',
    'France',
    'Spain',
    'Brazil',
    'Italy',
    'Canada',
    'Switzerland',
    'India',
    'Norway',
    'Denmark',
    'Israel',
    'Poland'
    )

    education = (
        'Bachelor’s degree', 
        'Less than a Bachelors', 
        'Master’s degree',
        'Post grad'
    )


    country = st.selectbox('country', countries)
    education = st.selectbox('education Level', education)

    experience = st.slider('Years of Experience', 0, 50, 2)

    ok = st.button('Calculate Salary')
    if ok:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)


        salary = regressor.predict(X)
        st.subheader(f'The estimated salary is ${salary[0]:.2f}')




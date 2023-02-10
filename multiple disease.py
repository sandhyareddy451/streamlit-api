# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 21:28:54 2023

@author: ell
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


loading_diabetes = pickle.load(open('save_diabetes.sav','rb'))
loading_heart = pickle.load(open('saved_heart.sav','rb'))

with st.sidebar:
    
    selected = option_menu('Multiple Diabetes Data',
                       
                       ['Diabetes Result',
                        'Heart Diseas'],
                       
                         icons = ['heart','person'],
                         
                         default_index = 0)
            

if selected == 'Diabetes Result':
    
        st.title('Diabetes Prediction')
           
            
        Pregnancies = st.text_input('No of Pregnancies')
        Glucose = st.text_input('Glucose')
        BloodPressure = st.text_input('BP')
        SkinThickness = st.text_input('SkinThickness')
        Insulin = st.text_input('Insulin')
        BMI = st.text_input('BMI')
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
        Age = st.text_input('Age')
        
        diagnosis = ""
        if st.button('Submit'):
            diagnosis = loading_diabetes.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction,Age]])
             
            if (diagnosis[0]==0):
                print('Non diabetic')
            else:
                print('diabetic')
            
        st.success(diagnosis)
            
if selected == 'Heart Diseas':
    
    st.title('Heart Diseas Prediction')
    age = st.text_input('Age of Person')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain')
    trestbps = st.text_input('trestbps')
    chol = st.text_input('chol')
    fbs = st.text_input('fbs')
    restecg = st.text_input('restecg')
    thalach = st.text_input('thalach')
    exang = st.text_input('exang')
    oldpeak = st.text_input('oldpeak')
    slope = st.text_input('slope')
    ca = st.text_input('ca')
    thal = st.text_input('thal')
    
    diagnosis = ""
    if st.button('Submit'):
        diagnosis = loading_heart.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (diagnosis[0]==0):
           
           print(' no heart dieses')
        else:
           print('having heartdiseas')
           
    st.success(diagnosis)              
             
         
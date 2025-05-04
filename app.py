#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 10:39:12 2025

@author: Pierre
"""

import streamlit as st
import pandas as pd
import joblib

# Chargement du pipeline
pipeline = joblib.load("pipeline_3var_definitif.pkl")

# Titre
st.title("Lymph Node Involvement Prediction – Ovarian Cancer")

# Formulaire d'entrée utilisateur
menopause = st.selectbox("Menopause", [0, 1])
taille_tumorale = st.number_input("Tumor size (cm)", min_value=0.0, max_value=60.0, value=10.0)
atteinte_bilaterale = st.selectbox("Bilateral ovarian involvement", [0, 1])

if st.button("Predict"):
    X_input = pd.DataFrame([{
        "menopause": menopause,
        "taille_tumorale": taille_tumorale,
        "atteinte_ovarienne_bilaterale": atteinte_bilaterale
    }])
    proba = pipeline.predict_proba(X_input)[0, 1]
    st.write(f"Predicted probability of lymph node involvement: **{proba:.3f}**")
    if proba < 0.02:
        st.success("Low-risk profile – lymph node staging could be omitted.")
    else:
        st.error("At-risk profile – lymph node staging recommended.")

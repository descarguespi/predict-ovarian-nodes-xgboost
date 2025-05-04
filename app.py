#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 10:39:12 2025

@author: Pierre
"""

import streamlit as st
import pandas as pd
import joblib
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_vzK9E2dAuj7RQqbqRKhIzJz81a6wO_YI9A&s", width=200)
st.title("Node Risk Prediction for Presumed Early Stage Ovarian Cancer")
st.markdown("A clinical decision-support tool based on a 3-variable XGBoost model.")
st.markdown("---")

# Chargement du pipeline
pipeline = joblib.load("pipeline_3var_definitif.pkl")

# Formulaire d'entrée utilisateur
menopause_str = st.selectbox("Menopause", ["No", "Yes"])
taille_tumorale = st.number_input("Tumor size (cm)", min_value=0.0, max_value=60.0, value=10.0)
atteinte_str = st.selectbox("Bilateral ovarian involvement", ["No", "Yes"])

# Convertir en 0/1 pour le modèle
menopause = 1 if menopause_str == "Yes" else 0
atteinte_bilaterale = 1 if atteinte_str == "Yes" else 0

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

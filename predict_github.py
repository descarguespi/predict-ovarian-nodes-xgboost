#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 10:39:12 2025

@author: Pierre
"""

import pandas as pd
import joblib

# Charger le modèle pipeline entraîné
pipeline = joblib.load("pipeline_3var_definitif.pkl")

# Charger les données d'entrée (à adapter selon ton fichier)
df_input = pd.read_excel("example_input.xlsx")  # ⚠️ Assure-toi que ce fichier a les bonnes colonnes

# Vérification des colonnes attendues
required_columns = ["menopause", "taille_tumorale", "atteinte_ovarienne_bilaterale"]
if not all(col in df_input.columns for col in required_columns):
    raise ValueError(f"Le fichier doit contenir les colonnes suivantes : {required_columns}")

# Prédiction
proba = pipeline.predict_proba(df_input)[:, 1]
df_input["Predicted Risk"] = proba
df_input["Low Risk (<0.02)"] = (proba < 0.02).astype(int)

# Affichage
print(df_input)

# Sauvegarde éventuelle
df_input.to_excel("prediction_results.xlsx", index=False)
print("✅ Résultats sauvegardés dans prediction_results.xlsx")

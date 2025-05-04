#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 10:37:06 2025

@author: Pierre
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
import joblib

# Charger les données
df = pd.read_excel("Données.xlsx")

# Nettoyage de la variable ca_125
df["ca_125"] = df["ca_125"].astype(str).str.replace(" ", "", regex=False).str.replace(",", ".", regex=False)
df["ca_125"] = pd.to_numeric(df["ca_125"], errors="coerce")
df["ca_125"] = df["ca_125"].fillna(df["ca_125"].median())

# Imputation des variables catégorielles
df["menopause"] = df["menopause"].fillna(df["menopause"].mode()[0])
df["traitement_entretien"] = df["traitement_entretien"].fillna(df["traitement_entretien"].mode()[0])

# Variables du modèle
features = ["menopause", "taille_tumorale", "atteinte_ovarienne_bilaterale"]
target = "envahissement_ganglionnaire"

# Nettoyage
df = df[features + [target]].dropna()
X = df[features]
y = df[target].astype(int)

# Prétraitement
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), ["taille_tumorale"])
], remainder="passthrough")

# Pipeline XGBoost
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", XGBClassifier(n_estimators=30, eval_metric="logloss", use_label_encoder=False, random_state=42))
])

# Entraînement
pipeline.fit(X, y)

# Sauvegarde
joblib.dump(pipeline, "pipeline_3var_definitif.pkl")
print("✅ Modèle enregistré dans pipeline_3var_definitif.pkl")

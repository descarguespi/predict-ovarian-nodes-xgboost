# Modèle de prédiction de l’envahissement ganglionnaire dans le cancer de l’ovaire (stade précoce)

Ce dépôt contient un script Python permettant d’entraîner et d’évaluer un modèle XGBoost pour prédire l’envahissement ganglionnaire à partir de variables préopératoires simples.  
Il vise à identifier une sous-population de patientes à très faible risque (<2%), potentiellement dispensables d’un curage ganglionnaire.

---

## 📂 Contenu

- `pipeline_3var_definitif.py` : script principal
- `pipeline_3var_definitif.pkl` : pipeline entraîné, sauvegardé avec joblib
- `Données.xlsx` : (non inclus) fichier Excel attendu en entrée
- `requirements.txt` : dépendances nécessaires

---

## 📊 Variables utilisées

- `menopause` (1 = oui)
- `taille_tumorale` (cm)
- `atteinte_ovarienne_bilaterale` (1 = oui)

---

## ⚙️ Installation

1. Cloner le dépôt :
```bash
git clone https://github.com/toncompte/pipeline-ovaire.git
cd pipeline-ovaire
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

---

## ▶️ Exécution

Placer un fichier Excel appelé `Données.xlsx` dans le dossier attendu, avec les colonnes mentionnées ci-dessus.

Puis exécuter :
```bash
python pipeline_3var_definitif.py
```

---

## ✅ Résultats produits

- **Validation croisée 5×5** sans calibration pour identifier les patientes à faible risque (seuil 0.02)
- **Calibration finale** avec méthodes sigmoïde et isotonique
- **Courbes de calibration** + scores de Brier
- **Pipeline sauvegardé** (`pipeline_3var_definitif.pkl`)

---

## 🧠 Auteur

Projet développé dans le cadre d'une thèse en onco-gynécologie.  
Contact : pierre.descargues@chu-lyon.fr

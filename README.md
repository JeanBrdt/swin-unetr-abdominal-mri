# Swin UNETR pour la segmentation multi-organes en IRM abdominale

Projet TAF Health (UE cœur « Analyse d'images médicales ») : IMT Atlantique, 2A, 2026.
Sujet E : Transformers, Swin UNETR pour la segmentation sémantique.

**Équipe :** [Nom 1], [Nom 2], [Nom 3]
**Encadrants :** P.-H. Conze, F. Rousseau

## Objectif

Segmenter automatiquement quatre organes (foie, rein droit, rein gauche, rate) sur des IRM T2 abdominales (jeu de données CHAOS, T2-SPIR), et **étudier l'apport d'un Transformer pour capturer des dépendances à longue distance** par rapport à un U-Net convolutif.

Nous comparons, à armes égales (mêmes données, même loss, même entraînement) :

1. un **U-Net** de référence ;
2. **Swin UNETR** entraîné depuis zéro ;
3. **Swin UNETR** initialisé avec des poids pré-entraînés.

Métrique : **score Dice**, par organe, sur les 4 examens de test.

## Données

12 examens IRM T2 (fournis sur Moodle, **non versionnés dans ce dépôt**) :

| Rôle | Examens |
|---|---|
| Apprentissage (masques fournis) | 1, 2, 3, 5, 8, 10, 13, 19 |
| Test (masques fournis en fin de projet) | 21, 22, 32, 39 |

Étiquettes : 1 = foie, 2 = rein droit, 3 = rein gauche, 4 = rate.

Placer les fichiers `*-T2SPIR-src.nii.gz` et `*-T2SPIR-mask.nii.gz` dans `chaos-data/` (ce dossier est ignoré par git).

## Structure du dépôt

```
.
├── README.md
├── requirements.txt
├── project.ipynb        # notebook fourni (baseline random forest, calcul du Dice)
├── notebooks/           # nos expériences (exploration, U-Net, Swin UNETR)
├── src/                 # code réutilisable
│   ├── config.py        # chemins, découpage train/val/test, étiquettes
│   ├── data.py          # chargement et transformations MONAI
│   ├── models.py        # U-Net, Swin UNETR
│   ├── train.py         # boucle d'entraînement commune
│   └── evaluate.py      # inférence fenêtre glissante, Dice, visualisations
├── docs/                # restitution bibliographique
│   └── figures/
├── chaos-data/          # données (non versionnées)
└── outputs/             # poids, prédictions, logs (non versionnés)
```

## Installation

```bash
git clone <url-du-depot>
cd swin-unetr-abdominal-mri
pip install -r requirements.txt
```

Un GPU est nécessaire pour entraîner les réseaux (Google Colab convient).

## Méthode

- **Prétraitement :** normalisation d'intensité, recadrage du fond, padding en z (tailles multiples de 32), crops 3D guidés par les étiquettes (`RandCropByPosNegLabeld`) pour compenser le fort déséquilibre (fond ≈ 70 % du volume, reins et rate < 1 % chacun).
- **Perte :** Dice + entropie croisée.
- **Inférence :** fenêtre glissante (`sliding_window_inference`) sur le volume entier.
- **Validation :** examens 13 et 19 mis de côté pendant les expériences. Les examens de test ne servent qu'à l'évaluation finale.

## Résultats

*À compléter : tableau des Dice par organe et par modèle.*

| Modèle | Foie | Rein D | Rein G | Rate | Moyenne |
|---|---|---|---|---|---|
| Random forest (baseline) | | | | | |
| U-Net | | | | | |
| Swin UNETR (depuis zéro) | | | | | |
| Swin UNETR (pré-entraîné) | | | | | |

## Planning

| Date | Étape |
|---|---|
| 18/11 | Mise en place, pipeline de données |
| 01/12 | U-Net de référence, début Swin UNETR |
| 09/12 | Swin UNETR (avec et sans pré-entraînement), analyse |
| 16/12 | Restitution finale et challenge |

## Références

- A. Hatamizadeh et al., *Swin UNETR: Swin Transformers for semantic segmentation of brain tumors in MR images*, 2021.
- MONAI : [SwinUNETR](https://docs.monai.io/en/stable/networks.html#swinunetr) et [tutoriel BTCV](https://github.com/Project-MONAI/tutorials/blob/main/3d_segmentation/swin_unetr_btcv_segmentation_3d.ipynb).
- A. E. Kavur et al., *CHAOS Challenge: Combined (CT-MR) Healthy Abdominal Organ Segmentation*, 2021.

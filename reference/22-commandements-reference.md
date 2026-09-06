# Référence canonique — 22 commandements de Gabriel

La référence textuelle exacte du projet est désormais :

- `data/commandements.json`

Ce fichier contient, pour chacune des 22 cartes :

1. le **commandement intégral**, exactement dans la formulation fournie par l’utilisateur ;
2. le **mantra exact** associé ;
3. le **mouvement / Arcana exact** fourni par l’utilisateur ;
4. la référence numérotée indiquée par l’utilisateur.

> **Règle absolue du projet : ne jamais reformuler, corriger, compléter, résumer ou raccourcir ces trois textes sans instruction explicite de l’utilisateur.**

Cette page ne duplique volontairement plus les textes afin d’éviter qu’une deuxième copie diverge de la source canonique JSON. Le générateur de cartes lit directement `data/commandements.json`.

## Éléments de production

- Format d’une carte : **80 × 125 mm**.
- 4 cartes sur une feuille A4.
- Fond blanc et graphisme bleu minimal.
- Recto : chiffre romain, commandement, mantra, mouvement, cadre et quatre gouttes.
- Verso : image finale validée par l’utilisateur.
- Filet gris très fin de découpe : verso uniquement.
- Impression : taille réelle / 100 %, sans ajustement à la page.

Voir `docs/REPRODUCTION-PDF.md` et `scripts/generate_cards.py` pour reproduire le PDF.

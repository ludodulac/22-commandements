# Reproduire le PDF des 22 cartes

## Source canonique

`data/commandements.json` est la seule source textuelle à utiliser. Les formulations des commandements, mantras et mouvements ont été fournies explicitement par l’utilisateur et ne doivent jamais être reformulées, corrigées, complétées, résumées ou raccourcies automatiquement.

## Mise en page validée

- Carte : **80 × 125 mm** exactement.
- Papier : A4.
- Imposition : 2 × 2, donc 4 cartes par feuille.
- Écart entre cartes : 4 mm.
- Pages : recto puis verso, répétées pour chaque groupe de 4 cartes.
- Recto : fond blanc, bleu minimal, chiffre romain, commandement complet, mantra, mouvement.
- Typographie : serif élégante type tarot pour numéro/titre/mantra ; sans-serif lisible pour le mouvement.
- Cadre : double filet bleu arrondi.
- Quatre gouttes : **toutes pointent vers le bas**.
- Verso : utiliser **exactement l’image finale validée par l’utilisateur**, sans la réinterpréter, la redessiner ni la recadrer créativement.
- Guide de découpe : filet gris très fin **au verso uniquement** afin qu’un léger décalage duplex ne soit pas visible sur le recto.

## Image du verso

Nom canonique attendu par le générateur : `assets/verso-final.png`.

Le fichier source validé dans la conversation est `1000035408.png`. Il doit être conservé sans modification. Le générateur accepte également `assets/verso-final.png.base64` et le décode automatiquement si le PNG n’est pas présent.

## Génération

Dépendances : Python 3, ReportLab, Pillow.

```bash
python scripts/generate_cards.py
```

Sortie :

`output/22-commandements-80x125-duplex.pdf`

## Impression

- imprimer à **100 % / taille réelle** ;
- désactiver « ajuster à la page » ;
- commencer par un test sur papier ordinaire ;
- duplex : tester d’abord le retournement sur le bord long ;
- mesurer une carte imprimée : elle doit faire 80 × 125 mm ;
- seulement après validation, imprimer sur papier épais puis plastifier et découper.

## Principe de sécurité éditoriale

Le code peut adapter uniquement la taille typographique pour faire tenir les textes. Il ne doit **jamais modifier le contenu textuel** pour gagner de la place.

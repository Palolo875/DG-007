# Parcours — index.html

Mesures et captures en une passe ; rien n'est jugé ici. Chaque signal pose une question : la décision reste au run.

## 1. Défauts bloquants
- **Contraste du texte sur fond uni** : span #a9a59d sur #a9a59d = 1:1 (seuil 3:1, 297.303 px, « ESTU ») ; span #a9a59d sur #a9a59d = 1:1 (seuil 3:1, 162.432 px, « ESTU ») ; 1440 px : 5 texte(s) évalué(s), 34 candidat(s), 8 exclu(s) ; 390 px : 5 texte(s) évalué(s), 37 candidat(s), 15 exclu(s) … (suite dans `recette.json`) → SAVOIR/CRAFT/CFT-05 ; SAVOIR/CRAFT/CFT-03

## 2. Réserves à vérifier
- Chevauchement et troncature de texte : texte décoratif superposé, à juger : 1440 px : « ESTUÁRIO » et « ESTUÁRIO », 1440 px : « ESTUÁRIO » et « ESTUÁRIO », 1440 px : « ESTUÁRIO » et « ESTU », 390 px : « ESTU » et « ESTU », 390 px : « ESTU … (suite dans `recette.json`)
- Nom accessible des contrôles (candidats DOM) : 10 contrôle(s) DOM inspecté(s) ; nom accessible calculé non vérifié ; candidat hors couverture : button.burger
- Objet de preuve au premier écran (#nome) : 1440 px : intersection verticale 297.296875 px sur 297.296875, horizontale 1331.625 px sur 1331.625; limites : découpe par un ancêtre non évaluée; 390 px : intersection verticale 318.375 px sur … (suite dans `recette.json`)

## 3. Signaux et questions
- Aucun signal mesurable. Un relevé vide ne prouve ni la singularité ni la finition.
- À regarder, non mesuré : **Partie ordinaire** — navigation, bouton, onglets et pied, logo et titre masqués, appartiennent-ils encore à cette page ? Geste (`SAVOIR/STATE`) : Emprunter à la direction une seule propriété qui ne change pas le comportement : voix typographique, bord dans la logique de l’objet de preuve, couleur par rôle, alignement sur la grille.

## 4. Images à regarder
- **D'abord, seule : l'image sans le texte** `parcours-final/regard/sans-texte-1440.png`. Avant d'ouvrir une autre capture et de relire la direction déclarée, écris dans la trace l'idée qui s'y lit en une seconde ; compare ensuite ce nom à la direction. S'ils ne concordent pas, c'est l'idée qui se reprend.
- Ensuite :
  - 1440 px : écran `parcours-final/ecran-1440@2x.png` ; réduite `parcours-final/regard/reduite-1440.png`
  - 390 px : écran `parcours-final/ecran-390@2x.png` ; réduite `parcours-final/regard/reduite-390.png` ; sans le texte `parcours-final/regard/sans-texte-390.png`
- Foyer agrandi : `parcours-final/foyer-1440@2x.png`
- Mouvement : `parcours-final/mouvement-1440.png` : l'entrée image par image, le défilement et le survol ; le mouvement déclaré se juge ici, pas sur une capture fixe.
- Rendu contre références : `parcours-final/contre-references.png` : le niveau visé se juge ici, à la même hauteur.

## 5. Prochaine commande
- Pendant la boucle, une version à la fois : `python3 scripts/parcours.py captures site/index.html --version v2` (premier écran seul, aux mêmes largeurs).
- Regard séparé, si un second agent est possible : `python3 scripts/parcours.py critique site/index.html --brief "…"` (images seules et consigne).
- Garder un signal ou un marqueur : construis la variante qui le retire, puis `python3 scripts/planche.py atelier.png site/index.html retiree.html --bureau-seul` et compare à la vue.
- Après correction : `python3 scripts/parcours.py verifier site/index.html --foyer '#nome' --action '#cta' --refs refs`

## 6. Lignes mesurables de la trace légère
- Recette : 1 défaut(s) bloquant(s), 3 réserve(s), largeurs 1440, 390 px, action dans le premier écran vérifiée (`#cta`).
- Marqueurs relevés : aucun.
- Signaux de finition : 0 ; captures : 8 fichiers dans `parcours-final`.
- Mouvement : 26 animation(s) à l'entrée sur 1150 ms, 0 au défilement, 0 liée(s) au défilement, survol de cartes : aucun.

# Fiche de regard : index.html

Signaux, pas verdicts. L'œil de la personne tranche.

Attention : approximation classique (contraste couleur et résidu spectral), signal faible ; brancher un modèle de saillance appris avec `--attention onnx:` pour un signal plus fiable.

## Largeur 1440 px

**Attention au premier écran** (zones par part de la masse d'attention) :

1. 13 % : `div.mar` «  »
2. 9 % : `div.mar` «  »
3. 2 % : `div.mar` «  »
4. 1 % : `a.btn.p` « Passe do festival »

Foyer déclaré `#nome` : 24 % de l'attention pour 31 % de l'écran (levier 0.8) ; le foyer déclaré n'attire pas plus que sa surface.

**Contraste sur le fond réel** : 20 textes mesurés, 0 sous le seuil, 0 sur fond hétérogène au-dessus du seuil, 3 non évalués.

- Non évalué : « ESTUÁRIO » (texte rempli par un dégradé, une image ou sans remplissage)
- Non évalué : « ESTU » (texte rempli par un dégradé, une image ou sans remplissage)
- Non évalué : « ÁRIO » (texte rempli par un dégradé, une image ou sans remplissage)

Captures : `attention-1440.png`, `contraste-1440.png` (rouge : sous le seuil ; orange : fond hétérogène), `reduite-1440.png` (page entière réduite), `sans-texte-1440.png` (test de support).

## Largeur 390 px

**Attention au premier écran** (zones par part de la masse d'attention) :

1. 14 % : `div.mar` «  »
2. 12 % : `div.mar` «  »
3. 8 % : `a.btn.p` « Passe do festival »
4. 1 % : `div.mar` «  »

Signal : **foyer disputé** (zones 1 et 2 à 14 % et 12 %).

Foyer déclaré `#nome` : 24 % de l'attention pour 35 % de l'écran (levier 0.7) ; le foyer déclaré n'attire pas plus que sa surface.

**Contraste sur le fond réel** : 13 textes mesurés, 0 sous le seuil, 0 sur fond hétérogène au-dessus du seuil, 4 non évalués.

- Non évalué : « ESTU » (texte rempli par un dégradé, une image ou sans remplissage)
- Non évalué : « ÁRIO » (texte rempli par un dégradé, une image ou sans remplissage)
- Non évalué : « ESTU » (texte rempli par un dégradé, une image ou sans remplissage)

Captures : `attention-390.png`, `contraste-390.png` (rouge : sous le seuil ; orange : fond hétérogène), `reduite-390.png` (page entière réduite), `sans-texte-390.png` (test de support).

## Marqueurs de vague (1440 px, premier écran)

Liste [VEILLE 2026-10] de `SAVOIR/TOOLS/CONVERGENCE`, pour nommer `MODAL`, jamais pour interdire : un marqueur gardé par décision reste valide s'il tient (dose, limite, lien, exécution exacte).

- Aucun marqueur mesurable relevé.

Non relevés : violet, police Inter, halos et gradient décoratif, hero SaaS à cartes répétées, fond beige ou crème, brun, serif de caractère ou serif italique, orange rouille, bandeau défilant, ASCII, bleu Klein, libellés mono en capitales.
Non mesurés, à regarder : illustration peinte, tramage, dithering, logos pixel, hachures de plan, gravures, repères de recadrage, paysage peint en fond.

## Limites

- Attention : prédiction moyenne d'une population, pas une mesure ; un modèle appris hérite des interfaces et de la résolution de son corpus d'entraînement. L'approximation classique ne sait pas lire.
- Contraste : mesuré au pire décile du fond sous chaque ligne (5e et 95e centiles ; quartiles pour le texte tourné, dont la boîte droite déborde de son fond) ; le texte rogné par son conteneur et le texte rempli par un dégradé ne sont pas évalués ; les états non rendus (survol, focus) ne sont pas couverts.
- Marqueurs : relevés au premier écran de la première largeur, par teintes de pixels et styles calculés, avec des seuils `[À ADAPTER]` ; une police déclarée n'est pas forcément celle qui s'affiche. Un marqueur relevé n'est pas une faute, un relevé vide ne prouve pas la singularité, et les marqueurs non mesurés restent à regarder.

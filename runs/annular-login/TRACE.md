# Annular — page de connexion · trace de run (Design Governance V1, trace légère)

> Run fait avec la skill `design-governance-practice` (R2026-11-05d), sans personne pour répondre et sans agent critique (les questions de critique de la réponse en tiennent lieu).
> Produit et marque **fictifs** : nom, chiffres, liens et le circuit montré sont des **exemples** (TRUTH/ILLUSTRATIVE). Les faits de domaine (circuits imprimés, cartouche) sont réels.

## Cadrage

**RUN** — mode `DIRECTION` (premier contact d'une marque ouverte), avec **protection de niveau** : c'est un flux d'authentification, donc jamais `LITE`. Contrôles du profil « application, formulaire » (`ACTION/GATE-A`), y compris l'*authentification accessible*. · Décision : la direction de la page de connexion. · Risque principal : convergence (carte centrée ou écran partagé sombre à dégradé), puis la sécurité et la récupération (erreurs, mot de passe oublié, sans mot de passe). · Preuve minimale : planche des esquisses, parcours à 1440 et 390, états critiques capturés, atelier. · Arrêt : la direction tient, les états critiques sont observés et le défaut dominant est nommé.

**Produit (exemple)** : *Annular*, plateforme de revue de conception électronique, où des équipes revoient et approuvent les révisions de leurs circuits imprimés avant fabrication. Nom vérifié sans collision dans le domaine (recherche web, 2026-11-05).

**Public et tâche** : ingénieurs électroniciens, responsables hardware, sous-traitants. JTBD : entrer vite et sûrement dans son espace pour signer une révision. **La page n'affiche aucune donnée de compte avant l'authentification** (confidentialité) : le circuit montré est un exemple générique.

**Inventaire du domaine** (réel) :
1. L'*annular ring* : la couronne de cuivre autour d'un trou percé.
2. Les pistes de cuivre, les pastilles, les vias.
3. Le vernis épargne (*solder mask*), souvent vert, et la sérigraphie blanche (*silkscreen*).
4. Les mires (*fiducials*), cercles de cuivre qui calent la machine de pose.
5. L'empilement des couches (*stack-up*) et les fichiers de fabrication (Gerber RS-274X, perçage Excellon).
6. Le cartouche du plan de fabrication : titre, numéro, révision, date, feuille, « dessiné par », « approuvé par » (champs normalisés par l'ISO 7200).
7. Le cadre de plan à repères de zones (lettres et chiffres sur les bords).
8. La revue : annotations en rouge (*redline*), DRC, ordre de modification.
9. Les révisions lettrées : Rév. A, B, C.
10. Les cotes en millimètres et en mils.
11. Le rituel : la **signature** (*sign-off*) avant l'envoi en fabrication.

**Phrase d'idée** : « Sur cette page, se connecter devient signer le cartouche : le formulaire est le bloc de titre du plan de fabrication. » Test du concurrent : elle tiendrait aussi pour un outil de CAO mécanique, qui a lui aussi des cartouches. Il faut donc ancrer le plan dans le circuit lui-même (couronnes, mires, couches) pour qu'elle reste propre au domaine.

## Divergence

| # | Direction | p | Piste | Registre |
|---|---|---|---|---|
| M | **Écran partagé** : formulaire à gauche en Inter, panneau sombre à droite avec lueur verte et citation client | 0,40 | — (`MODAL`) | split screen ; dégradé ; grotesque neutre |
| 2 | Fond sombre de pistes lumineuses animées | 0,20 | cliché du domaine | néon, motif |
| A | **Cartouche** : la page est un plan de fabrication, et la connexion se fait dans le cartouche | 0,10 | l'objet imprimé de son monde + son rituel | dessin technique au trait ; papier et encre ; rouge de revue |
| B | **Sérigraphie** : la page est la carte elle-même ; on écrit dans les cases blanches que la sérigraphie réserve au marquage | 0,08 | ce qu'il produit, montré tel quel | matière (vernis, cuivre, sérigraphie) ; densité |
| C | **Couches** : vue éclatée de l'empilement, avec le formulaire sur la couche du dessus | 0,06 | sa structure | axonométrie ; couches translucides |

Gardées pour esquisse : A, B, C. Modale M esquissée comme référence. Direction 2 écartée (cliché du domaine).

**Références observées** (`refs/`, 2026-11-05) :
- Vercel : e-mail d'abord, puis fournisseurs, SSO SAML et clé d'accès. *Change* : l'ordre des options. *Ne se transfère pas* : le vide total.
- Stripe : carte centrée sur un ruban en dégradé ; « Mot de passe oublié ? » à côté du libellé. *Change* : la place du lien de récupération. *Ne se transfère pas* : le dégradé, marqueur de vague 1.
- Figma : Google d'abord, puis SSO et réinitialisation en liens. *Change* : rien de plus.
- Linear : non rendue (application vide à la capture).

## Choix sur la planche (`esquisses/planche-1.png`)

- **B · Sérigraphie** : écartée. Les pistes aléatoires se lisent comme le cliché « fond de circuit » (la direction 2 écartée).
- **C · Couches** : écartée. Elle se lit comme une carte à ombres colorées, un effet plutôt qu'une idée.
- **A · Cartouche** : **gardée**. C'est la seule qui bat la modale : un vrai plan (cotes, couronnes, mires, pas de 2,54 mm, cadre à repères, nuage de revue), et la connexion se fait dans le cartouche. *Ce que la retenue perd* : la matière de B (cuivre, vernis).

**Voix** (`esquisses/planche-voix.png`, sur le vrai titre, dans le cartouche) :
- Barlow : **retenue**, de la lignée DIN du lettrage technique.
- IBM Plex Sans : écartée, elle évoque la marque IBM.
- Overpass : écartée, plus large et plus molle.

## Direction déclarée

```text
DIRECTION — Cartouche
VISION — Se connecter, c'est signer le plan : la page est la feuille de fabrication d'une carte, et le formulaire en est le cartouche ; l'ingénieur reconnaît son monde avant de lire un mot.
REGISTRE — base : dessin technique au trait (plan, cadre à repères ISO 5457) ; modificateur : annotation de revue (rouge, nuage). Marqueurs visibles : les repères de zones 1–8 / A–F ; le nuage rouge autour du boîtier U3.
NIVEAU — qu'un électronicien la prenne pour un vrai plan de fabrication, sans faute de convention.
ASSET — plan de carte dessiné en SVG dans la page ; aucune image.
COMPOSANT — libellés au-dessus des champs ; « Mot de passe oublié ? » à droite du libellé, mais après le champ dans l'ordre de tabulation ; « Afficher » dans le champ ; bouton principal plein ; clé d'accès et SSO en contour ; autocomplete username/current-password.
FINITION — angles vifs ; traits de 1 et 2 px (rapport 1:2 des épaisseurs normalisées) ; une seule famille (Barlow) ; six tailles de texte ; le rouge réservé à ce qui demande une action (annotation, erreur).
MOUVEMENT — un seul moment : le nuage de revue se trace une fois à l'entrée (0,9 s), puis sa note apparaît ; ce qui répond au geste : l'e-mail saisi s'inscrit dans « Approuvé par » ; en mouvement réduit, rien ne s'anime.
MOBILE — le plan passe en tête, en bande, et le cartouche devient l'écran ; l'action reste dans le premier écran.
```

**Trame modale d'une page de connexion** : logo, « Bon retour », fournisseurs, « ou », e-mail, mot de passe, bouton, liens, avec un panneau décoratif en option. **Gardée à l'intérieur du formulaire** : l'ordre des champs est une convention de tâche, et la rompre nuirait à la connexion. **Rompue autour** : il n'y a pas de panneau décoratif ; la page entière est le document que l'on vient signer, et le succès s'écrit « Signé ✓ ».

## Boucle (capture → défaut dominant → correction)

| Version | Défaut dominant observé | Modification |
|---|---|---|
| v1 | cartouche trop haut, débordement de 19 px à 900 ; « Conne / xion » en mobile | resserrement ; alternatives côte à côte ; trois colonnes en mobile |
| v2 | le cartouche est poussé sous les notes (rangée 1) | le cartouche couvre les deux rangées et se cale en bas |
| v3 | à 1280×720, le cartouche chevauche les révisions | table des révisions masquée sur écran bas |
| parcours | 11 tailles de texte qui se concurrencent | échelle à 6 paliers : 11, 13, 15, 17, 24, 30 |
| états | ordre de tabulation e-mail → « oublié » → mot de passe ; en erreur, la page grandit de 96 px ; le cartouche chevaucherait les révisions | lien placé après le champ dans le DOM, à côté du libellé par la grille ; message sur deux lignes ; démo déplacée en note 4 ; colonne de droite en pile |
| v5–v7 | note 4 disloquée (les `<b>` devenaient des cellules) ; cartouche 16 px hors cadre ; plan mal calé à 1024×768 | contenu enveloppé ; colonnes `minmax(0, …)` ; cartouche calé en bas |
| finition | dates incohérentes (12.09.26 contre 05.11.2026) ; **sans script, envoi en GET : mot de passe dans l'URL** | dates harmonisées ; `method="post"` |
| mobile final | « 05.11.20 / 26 », « Prototy / pe » | cartouche en deux colonnes, cases du bas sur deux rangées |

## Atelier (`esquisses/planche-atelier.png`, vue normale et vue réduite floue)

**Décision éprouvée : la page est un plan** (dessin à gauche, cartouche en coin). Les règles ont été écrites avant de construire les variantes.
- *Retirer* (ni carte ni révisions) gagnait si la connexion prenait plus de foyer et que la page restait reconnaissable comme un outil d'électronique. → **Perd** : on obtient un formulaire encadré quelconque.
- *Intensifier* (carte plus grande, trois nuages de revue) gagnait si le domaine se lisait plus fort et que le cartouche restait le foyer en vue floue. → **Perd** : les masses rouges tirent l'œil loin du cartouche, et une note chevauche des composants.
- **Issue : original confirmé par comparaison.** En vue floue, le foyer est le bouton noir, et le nuage reste un second plan.

## Contrôles (profil « application, formulaire », `ACTION/GATE-A`, AUTOMATED + MANUAL, Chromium 153)

- **Recette** (`parcours-final/`) : 0 défaut bloquant ; contraste conforme sur 74 textes à 1440 et 49 à 390 ; action dans le premier écran à 1440 et à 390 ; 0 signal de finition ; aucun marqueur de vague relevé.
- **Contraste calculé** : encre sur papier 15,9:1 ; gris 6,7:1 ; rouge 5,6:1.
- **États observés** (`captures/etat-*`, `captures/etats-planche.png`) :
  - nominal, avec la signature en direct ;
  - champs vides : messages près des champs, `aria-invalid`, focus sur le premier champ en erreur ;
  - e-mail incomplet : message qui dit comment corriger ;
  - chargement : bouton désactivé, `aria-busy`, pas de double envoi ;
  - refus : message générique qui ne dit pas lequel des deux est faux, focus sur le message, e-mail conservé, mot de passe vidé ;
  - mot de passe affiché (`aria-pressed`) ;
  - réinitialisation : message qui ne révèle pas si le compte existe ;
  - clé d'accès, SSO, succès.
- **Authentification accessible** : collage autorisé, gestionnaires de mots de passe (autocomplete `username webauthn` et `current-password`), aucune énigme ni CAPTCHA, possibilité d'afficher le mot de passe, clé d'accès proposée.
- **Clavier** : ordre e-mail → mot de passe → Afficher → oublié → Se connecter → clé d'accès → SSO → Demander un accès ; focus visible de 3 px.
- **Replis** : sans script, le formulaire reste lisible et s'envoie en POST (aucun identifiant dans l'URL) ; mouvement réduit, 0 animation ; contraste forcé, lisible ; zoom 200 % (720 px CSS), sans défilement horizontal.
- **Largeurs observées** : 1920×1080, 1440×900, 1280×720, 1024×768, 390×844, 360×740.
- **Confidentialité** : aucune donnée de compte affichée avant authentification ; le plan montré est un exemple générique.
- **NOT-VERIFIED** :
  - lecteur d'écran réel (le nom accessible calculé n'est pas vérifié par la recette) ;
  - vraie cérémonie WebAuthn et vrai SSO, faute de serveur ;
  - état de compte bloqué ou de limitation de débit ;
  - double authentification ;
  - Safari et Firefox ;
  - traduction anglaise.

## Trace légère (six lignes)

1. **RUN** `DIRECTION` avec protection de niveau (authentification) ; risque de convergence, puis sécurité et récupération ; preuves : planche, parcours, états, atelier.
2. **Direction déclarée** : *Cartouche*, « dessin technique × annotation de revue ». Mouvement : le nuage se trace une fois, et l'e-mail s'inscrit dans « Approuvé par ». Thèse : la promesse (des révisions revues et signées) passe par un objet de preuve (un plan de carte annoté, à signer) et un geste (signer = se connecter).
3. **Modal, trame et parti** : modale = écran partagé à dégradé (p ≈ 0,40) ; esquissées : Cartouche 0,10, Sérigraphie 0,08, Couches 0,06 ; planche → Cartouche ; trame gardée dans le formulaire, rompue autour ; aucun marqueur relevé.
4. **Plafond atteint** : tout en code natif, au plafond (plan SVG, typographie Barlow OFL). Pas d'image, aucune n'étant nécessaire. Contenu d'exemple : Annular, ANN-2041, les révisions et le compte de démonstration.
5. **Défaut dominant restant** : sur grand écran (1920 px), le cartouche de 500 px paraît petit face au plan ; une échelle du cartouche liée à la hauteur serait à essayer.
6. **Prochaine preuve** : un test avec un lecteur d'écran réel ; la branche au vrai serveur d'authentification (WebAuthn, SSO, blocage) ; la version anglaise ; l'avis d'ingénieurs électroniciens sur la justesse du plan.

**Statut** : proposition `EXPLORATORY` ; ni acceptation ni `RUN_CARD`.

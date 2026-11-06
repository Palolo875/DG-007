# Plan de route — Design Governance V1

> Établi le 6 novembre 2026 à partir de nos échanges, de deux runs réels (Estuário, Annular), de la relecture du paquet `R2026-11-05d` et de recherches vérifiées en double (Exa et recherche web).
> Chaque constat porte son niveau de certitude : **établi** (vérifié dans le paquet, dans un rendu ou dans une source primaire), **probable** (déduit, ou source secondaire), **à vérifier**.
> Rien ici n'est encore mesuré par un test comparatif : ce plan propose des hypothèses et dit comment les éprouver.

---

## 1. Le cap

**Ce que le système dit vouloir** (`maintenance/versions.md`, « Cap ») : obtenir un niveau élevé **plus régulièrement**, avec moins d'oublis, de tâtonnements et de reprises, et dire honnêtement ce qui a été vérifié.

**Ce que nous visons, précisé dans nos échanges :**

1. **Un visuel fini au niveau d'un produit**, pas une démo générique, y compris quand le travail est une démo.
2. **Moins de coût et de temps**, pas plus : faire mieux avec moins, sans alourdir ni compliquer le système.
3. **Une démo toujours signalée, visiblement**, sans jamais baisser la qualité visuelle pour autant.

**Critère de réussite global :** sur des briefs vagues comparables, le système allégé gagne à l'aveugle, au jugement d'un humain, contre le système actuel **et** contre l'absence de système, tout en coûtant moins que le système actuel.

---

## 2. Ce que nous avons obtenu de concret

| Acquis | Où | Statut |
|---|---|---|
| Run « Estuário » : héro de festival, direction *Mar Largo*, calçada générée en code | `runs/estuario-hero/` | fait |
| Run « Annular » : page de connexion, direction *Cartouche*, états critiques et replis vérifiés | `runs/annular-login/` | fait |
| Traces des deux runs, avec le registre corrigé et contrôlé après coup | `runs/*/TRACE.md` | fait |
| Planches réutilisables (divergence, voix, atelier, états) | `runs/*/esquisses/`, `runs/*/captures/` | fait |
| Générateur de calçada (rangs qui suivent la vague, lettres taillées dans la pierre) | `runs/estuario-hero/calcada.py`, `site/index.html` | fait |
| Diagnostic du système, sourcé (section 3) | ce document | fait |
| Revue de la recherche, vérifiée en double (section 7) | ce document | fait |

---

## 3. Le diagnostic

### Ce qui marche (établi dans les runs)

- **La planche** (esquisses comparées côte à côte) a écarté de mauvaises directions dans les deux runs : la cage pombaline lue comme des cases vides, le « fond de circuit » cliché.
- **La boucle capture → correction** a trouvé la plupart des vrais défauts :
  - le nom absent au chargement ;
  - le mot de passe envoyé dans l'URL sans script ;
  - l'ordre de tabulation, le débordement en erreur ;
  - onze tailles de texte, un cartouche hors cadre de 16 px.
- **Le parcours automatique** (`scripts/parcours.py verifier`) a relevé des signaux utiles sans effort de l'agent.
- **L'honnêteté** : plafond déclaré, contenus d'exemple marqués, limites écrites.

### Ce qui coûte sans améliorer le visuel

**Établi :**
- **Le noyau fait 42 352 octets** et se lit à chaque run (budget : 46 000). Le tronc du mode `DIRECTION` fait 34 506 caractères, à 98 % de son budget.
- **Le guide officiel d'Anthropic** (`frontend-design`) obtient l'étape équivalente (plan, puis relecture contre le brief) en quelques lignes.
- **L'atelier retirer/intensifier** a confirmé l'original dans les deux runs. Le système prévoit lui-même que, dans ce cas, la façon de construire les variantes se revoit.

**Établi aussi :** le registre et la gouvernance n'ont eu **aucun effet sur l'image**. Le registre a été écrit sans piloter le build, et une règle fausse est passée sans être détectée.

**Probable :** la fiche de version mesure un run avec le système à environ 1,7 fois plus de jetons et 3 à 4 fois plus de temps qu'un run sans lui.

### Ce qui se contredit ou n'est pas contrôlé (établi dans le paquet)

| Problème | Preuve |
|---|---|
| **La modale part perdante.** Le texte défend la convention (« Ne remplace pas un biais de conformité par une obligation de nouveauté »), mais la procédure oppose trois esquisses finies à « une esquisse rapide de la modale ». | `SKILL.md`, §4 étape 2 ; mes deux modales faisaient environ 20 lignes |
| **Le signalement de démo est facultatif** : « Quand le public doit savoir ». Estuário est sorti sans aucun signal visible que le festival est fictif. | `SKILL.md`, §7 « Audience » ; `runs/estuario-hero/site/index.html` |
| **Les règles se satisfont sans contrôle.** Deux registres faux, test de style non fait, relecture « contre n'importe quel brief » non tracée : rien ne l'a vu. | `runs/*/TRACE.md`, section « Registre : contrôle a posteriori » |
| **La finition est une passe, pas une boucle** (« Une passe, pas une boucle »). Le défaut restant d'Annular a été noté, jamais repris. | `SKILL.md`, §8 |
| **Les outils de capture n'attendent pas la fin des animations d'entrée** : planche et critique ont photographié des états transitoires. | captures des deux runs |
| **Les marqueurs de convergence vieillissent vite et en ignorent certains**, que nos rendus portent : noir teinté (`#17181A`, `#1B1D1F`), mise en page « journal » à filets et rayon zéro, libellés en capitales. | `design/savoir/gout-et-tendances.md` ; guide Anthropic ; `regard.py` n'a rien relevé |

---

## 4. Les principes du chantier

1. **Retirer avant d'ajouter.** Une règle sans effet visible part (le système le demande déjà : « qu'est-ce qui change si cette ligne est vraie, fausse ou absente ? »).
2. **Du code plutôt que de la prose.** Ce qui se vérifie se vérifie par un outil, pas par la lecture de l'agent.
3. **Garder les deux leviers prouvés** : la planche et la boucle capture → correction.
4. **Aucun style maison.** Le socle de finition porte des relations (rayons imbriqués, chiffres tabulaires, focus), jamais des couleurs, des polices ou des valeurs, pour ne pas fabriquer une nouvelle convergence.
5. **Mesurer avant d'intégrer.** Seul ce qui gagne au test comparatif entre dans le paquet.
6. **Démo visible, qualité intacte.**

---

## 5. Les chantiers

Effort : **petit** (moins d'une heure), **moyen** (une demi-journée), **gros** (plus d'une journée).

### Phase 0 — Préparer le terrain

| # | Action | Fichiers | Effort | Réussi quand |
|---|---|---|---|---|
| 0.1 | Décompresser le paquet dans le dépôt, pour que chaque modification soit lisible en diff (aujourd'hui, DG-007 ne contient qu'un zip). Garder le zip d'origine comme référence. | `Design_Governance_V1_GITHUB_R2026-11-05d.zip` → `package/` | petit | `python3 scripts/validate_all.py` passe depuis le dossier décompressé |
| 0.2 | Mesurer la ligne de base : taille du noyau et du tronc, durée et volume lu d'un run type. | `scripts/test_core_budget.py`, journal de mobilisation | petit | chiffres consignés ici |
| 0.3 | Corriger les deux rendus livrés : signal « démonstration, festival fictif » visible et soigné sur Estuário ; bouton d'Annular qui garde son libellé pendant le chargement. | `runs/estuario-hero/site/index.html`, `runs/annular-login/build_site.py` | petit | captures refaites |
| 0.4 | Documenter l'installation de la liaison Python de Playwright, à la même version que le Chromium présent, sans `playwright install`. | `maintenance/README.md` | petit | un agent neuf lance le parcours sans tâtonner |

### Phase 1 — Alléger sans perte visuelle

| # | Action | Fichiers | Effort | Réussi quand |
|---|---|---|---|---|
| 1.1 | **Un noyau visuel d'environ 8 Ko** : gestes de fabrication et de finition, planche, boucle de capture, signal de démo. Le reste reste dans les sections propriétaires, lu au signal. | `SKILL.md`, blocs « noyau » des sources, `scripts/build_core.py` | gros | noyau ≤ 10 Ko ; validation du paquet verte |
| 1.2 | **La gouvernance en module** : gates, `RUN_CARD`, trace complète chargés seulement pour un travail audité ou une acceptation demandée. | `gouvernance/`, `agent/chemins.md` | moyen | un run de proposition ne les lit pas |
| 1.3 | **L'atelier devient conditionnel** : seulement si une décision principale est réellement en doute après la capture. | `design/produit/finition.md` (`ACTION/ATELIER-EDITION`) | petit | règle réécrite, sans quota |
| 1.4 | **La trace se limite à ses six lignes** hors travail audité ; pas de longue trace par défaut. | `SKILL.md` §9 | petit | — |
| 1.5 | **Le regard séparé (second agent) devient optionnel**, remplacé par défaut par les contrôles de la phase 2. | `SKILL.md` §8 | petit | — |

### Phase 2 — Confier au code ce que l'agent refait à chaque run

| # | Action | Fichiers | Effort | Réussi quand |
|---|---|---|---|---|
| 2.1 | **Un socle de finition CSS**, relations seulement : focus visible, chiffres tabulaires pour les données, titres équilibrés (`text-wrap`), rayon intérieur = rayon extérieur − marge, cibles tactiles (24 px, 44 px en mobile), mouvement réduit, styles d'état (chargement, erreur, désactivé, vide). Ni couleur, ni police, ni valeur imposée. | nouveau `design/produit/socle.css` + une ligne au noyau | moyen | appliqué à Annular et Estuário sans changer leur direction |
| 2.2 | **Capture à l'ouverture** : le parcours photographie aussi la page à l'instant zéro et signale un contenu principal absent. | `scripts/parcours.py`, `scripts/check_render.py` | petit | le défaut « nom absent » d'Estuário v4 est relevé automatiquement |
| 2.3 | **Planche et critique attendent la fin des animations d'entrée** (`document.getAnimations()`), ou une durée fournie. | `scripts/planche.py`, `scripts/parcours.py` | petit | les planches des deux runs se refont sans état transitoire |
| 2.4 | **Signaux de finition mesurés** : nombre de rayons distincts, espacements hors échelle, traits d'icônes mêlés, chiffres non tabulaires dans une colonne, lignes de base décalées. | `scripts/regard.py`, `scripts/parcours.py` | moyen | chaque signal a un test dans `scripts/test_regard.py` |
| 2.5 | **Présence d'un signal de démo** : le parcours vérifie qu'un artefact déclaré fictif porte une mention visible. | `scripts/parcours.py` | petit | Estuário actuel échoue, Estuário corrigé passe |
| 2.6 | **Mise à jour des marqueurs**, sourcée et datée : les cinq familles du guide Anthropic (crème/serif/terre cuite, noir et accent acide, mise en page « journal », kit de cartes SaaS, habillage de gabarit dont le noir teinté et les libellés en capitales) et les tendances 2026 devenues des défauts (filets fins avec une seule famille, bento, imperfection simulée). Échéance de revue raccourcie. Mesurer ceux qui se mesurent. | `design/savoir/gout-et-tendances.md`, `scripts/regard.py` | moyen | `regard.py` relève le noir teinté et les libellés en capitales sur nos deux runs |

### Phase 3 — Corriger les règles qui se contredisent

| # | Action | Fichiers | Effort | Réussi quand |
|---|---|---|---|---|
| 3.1 | **Modale finie** : remplacer « une esquisse rapide de la modale » par « la modale, au même niveau de finition que les autres ». | `SKILL.md` §4, `design/direction/diriger.md` | petit | la convention peut gagner sur la planche |
| 3.2 | **La convention comme parti valide pour un écran de produit**, avec une cible de fidélité : comparer au zoom les composants (bouton, champ, carte, ligne de tableau) à 2 ou 3 interfaces réelles. La divergence reste réservée au premier contact de marque. Appuis : Tuch 2012, loi de Jakob, Material 3 Expressive. | `agent/chemins.md` (`STANDARD`), `SKILL.md` §4 | moyen | règle courte, sans nouvelle étape obligatoire |
| 3.3 | **Démo toujours visible** : « tout artefact fictif ou de démonstration qui sort de l'atelier signale son statut, visiblement et proportionnellement au risque, en langage produit ; la qualité visuelle n'est jamais réduite pour autant ». Mention « Image générée » près de toute image réaliste générée (AI Act, article 50, en vigueur depuis le 2 août 2026). | `SKILL.md` §7, `design/direction/diriger.md` | petit | remplace « quand le public doit savoir » |
| 3.4 | **Direction cochée sur capture**, contre le « Design Theater » : chaque ligne de la direction déclarée est notée *vue* ou *non vue* sur l'image ; une ligne non vue se corrige ou se retire, jamais ne se garde par une phrase. | `SKILL.md` §4 et §8 | petit | une ligne de trace, pas un formulaire |
| 3.5 | **La finition devient une boucle courte** sur le premier écran et l'objet de preuve, jusqu'à ce que l'écart avec la référence ne se voie plus. Elle remplace la « passe unique » ; l'atelier allégé (1.3) compense le temps. | `SKILL.md` §8 | petit | — |

### Phase 4 — Mesurer

| # | Action | Effort | Réussi quand |
|---|---|---|---|
| 4.1 | **Protocole comparatif** : 3 briefs vagues (tableau de bord, inscription d'une app de fitness, portfolio à voix joueuse) × 3 conditions (sans système, système actuel, système allégé). Paires mélangées au hasard, fichier de correspondance scellé jusqu'après la notation. | moyen à préparer, gros à exécuter | protocole écrit dans `maintenance/evolution.md` |
| 4.2 | **Ce qu'on mesure** : note visuelle à l'aveugle (fini « produit », beauté, adéquation), honnêteté du signal de démo, durée, volume lu et écrit. | — | — |
| 4.3 | **Règle d'intégration** : un changement n'entre dans le paquet que s'il gagne ou ne perd pas visuellement **et** réduit le coût. On peut commencer par un seul brief pour décider si la suite vaut l'effort. | — | décision consignée ici |

### Phase 5 — Plus tard, ou à décider

| # | Piste | Pourquoi plus tard |
|---|---|---|
| 5.1 | **Méthode de registre illustré** codable : vue du dessus ou axonométrique, primitives géométriques, palette restreinte, personnages en vue plongeante (tête, épaules, ombre portée). | utile pour la famille « golf, ping-pong », à éprouver d'abord |
| 5.2 | **Route de génération d'images**, avec signal « Image générée » : tester les connecteurs disponibles dans l'environnement. | jamais testée ; plafond réel pour les rendus portés par la photo |
| 5.3 | **Mise en scène de présentation** (appareil, ombre, cadrage), distincte de la page livrée. | une partie du niveau des références vient de là |
| 5.4 | **Règles de Vercel absentes du système** : états clairsemés et denses, durée minimale de chargement, `…` et guillemets typographiques, espaces insécables, contenu très long. | à verser dans le socle 2.1 si le test le justifie |

---

## 6. Ce que nous n'affirmons pas

- Que le système allégé sera meilleur : c'est l'hypothèse de la phase 4.
- Que la convergence mesurée sur des modèles en 2026 vaut pour tous les outils : les études sont des prépublications, dont une écrite par une entreprise du secteur.
- Que les rendus très finis prouvent l'usage. La recherche montre qu'une maquette pauvre trompe sur l'esthétique, mais aussi qu'une basse fidélité trouve autant de problèmes d'usage, et qu'un beau rendu peut masquer de petits défauts en test.
- Les mentions de « 22 runs », « Brindille », « Soleil noir » ou « COTA » : absentes du paquet et de la session, non vérifiées.
- Une lecture juridique : l'AI Act et la règle de la FTC sont cités comme contexte, pas comme avis.

---

## 7. Sources principales (vérifiées)

**Recherche sur la perception :**
- Lindgaard et al. 2006, *Behaviour & Information Technology* 25(2) : jugement d'attrait en 50 ms. https://www.tandfonline.com/doi/abs/10.1080/01449290500330448
- Tuch et al. 2012, *IJHCS* 70(11) : faible complexité et forte prototypicité préférées, dès 17 ms. https://www.sciencedirect.com/science/article/abs/pii/S1071581912001127
- NN/g, *The Aesthetic-Usability Effect* (Moran 2024). https://www.nngroup.com/articles/aesthetic-usability-effect/
- NN/g, *Jakob's Law*. https://www.nngroup.com/videos/jakobs-law-internet-ux/
- NN/g, *State of UX in 2026*. https://www.nngroup.com/articles/state-of-ux-2026/
- Sauer et Sonderegger 2009 (fidélité et esthétique des prototypes). https://www.sciencedirect.com/science/article/abs/pii/S0003687008001129
- Walker, Takayama et Landay 2002 (basse et haute fidélité). https://doi.org/10.1177/154193120204600513

**Convergence des sorties d'IA :**
- Doshi et Hauser 2024, *Science Advances* (homogénéisation collective). https://www.science.org/doi/10.1126/sciadv.adn5290
- *Design Creativity Bench*, arXiv 2610.11539 (oct. 2026). https://arxiv.org/abs/2610.11539
- *Design Theater*, arXiv 2607.22928 (juil. 2026). https://arxiv.org/abs/2607.22928
- *Interrogating Design Homogenization in Web Vibe Coding*, arXiv 2603.13036. https://arxiv.org/abs/2603.13036

**Guides de pratique :**
- Anthropic, `frontend-design` SKILL.md. https://github.com/anthropics/claude-code/blob/main/plugins%2Ffrontend-design%2Fskills%2Ffrontend-design%2FSKILL.md
- Vercel, *Web Interface Guidelines*. https://vercel.com/design/guidelines

**Cadre réglementaire et conventions :**
- Commission européenne, transparence de l'IA (article 50, 2 août 2026). https://commission.europa.eu/news-and-media/news/safer-and-more-transparent-ai-2026-08-02_en
- FTC, règle sur les avis et témoignages (16 CFR 465). https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465
- Stripe, mode test et sandboxes. https://docs.stripe.com/testing-use-cases

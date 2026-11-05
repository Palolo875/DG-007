"""Construit site/index.html : page de connexion Annular, direction « Cartouche »."""
from pathlib import Path
import build_sketches as B

HERE = Path(__file__).parent
K = 10                       # px par mm dans le viewBox du plan
OX, OY = 70, 70              # origine de la carte dans le viewBox (marges pour les cotes et la note)
VW, VH = OX + 62 * K + 40, OY + 38 * K + 70

art, _ = B.board_drawing(OX, OY, K, ink="#1B1D1F", red="#C8322A")
# note de revue : au-dessus de la carte, reliée au nuage du boîtier U3
qx, qy, qs = OX + 24 * K, OY + 12 * K, 10 * K
nx, ny = qx + qs + 30, OY - 26
note = (f'<g class="redline"><path class="nuage-lien" d="M{qx+qs+qs*.55:.0f},{qy-qs*.1:.0f}L{nx-6},{ny+8}" />'
        f'<text x="{nx}" y="{ny}">Rév. C · U3 déplacé, à signer</text></g>')
PLAN = (f'<svg class="plan-svg" viewBox="0 0 {VW} {VH}" role="img" aria-label="Exemple de plan de fabrication : carte de 62 × 38 mm, '
        f'avec une annotation de revue sur le boîtier U3">{art}{note}'
        f'<text x="{OX}" y="{OY-26}" class="legende">ANN-2041 · Carte capteur · 4 couches</text></svg>')

HTML = r"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Se connecter · Annular</title>
<meta name="description" content="Connexion à Annular, la revue de conception électronique.">
<!--
  Produit fictif : Annular, le circuit ANN-2041, ses révisions et le compte de démonstration sont des EXEMPLES.
  Prototype sans serveur : aucune donnée n'est envoyée ; les états (erreur, chargement, succès) sont simulés localement.
  Trace du run : ../TRACE.md
-->
<link rel="stylesheet" href="polices.css">
<style>
:root{
  --papier:#F7F7F4;   /* papier de plan, gris neutre (pas crème) */
  --encre:#1B1D1F;    /* encre : texte, traits, action */
  --gris:#575A5E;     /* texte secondaire, 6,7:1 sur le papier */
  --rouge:#C8322A;    /* rouge de revue : seulement ce qui demande une action (5,6:1) */
  --champ:#FFFFFF;
  --m:24px;           /* marge du cadre */
  --b:18px;           /* bande des repères de zones */
}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%}
body{background:var(--papier);color:var(--encre);font-family:Barlow,system-ui,sans-serif;font-size:16px;line-height:1.4}
a{color:inherit;text-underline-offset:3px;text-decoration-thickness:1px}
a:hover{text-decoration-thickness:2px}
:focus-visible{outline:3px solid var(--encre);outline-offset:2px}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

/* ---------- la feuille et son cadre à repères (ISO 5457) ---------- */
.feuille{position:relative;min-height:100svh;padding:calc(var(--m) + var(--b))}
.cadre{position:absolute;inset:var(--m);border:2px solid var(--encre);pointer-events:none}
.cadre:after{content:"";position:absolute;inset:calc(var(--b) - 2px);border:1px solid var(--encre)}
.zones{position:absolute;display:flex;font-size:11px;font-weight:500;line-height:1}
.zones span{flex:1;display:flex;align-items:center;justify-content:center}
.zones span + span{border-left:1px solid var(--encre)}
.zones.h{left:calc(var(--b) - 2px);right:calc(var(--b) - 2px);height:calc(var(--b) - 2px)}
.zones.h.t{top:0}.zones.h.b{bottom:0}
.zones.v{top:calc(var(--b) - 2px);bottom:calc(var(--b) - 2px);width:calc(var(--b) - 2px);flex-direction:column}
.zones.v span + span{border-left:0;border-top:1px solid var(--encre)}
.zones.v.l{left:0}.zones.v.r{right:0}

/* ---------- composition : plan à gauche, révisions et cartouche à droite ---------- */
.dessin{position:relative;display:grid;grid-template-columns:minmax(0,1fr) 500px;grid-template-rows:auto minmax(0,1fr);
  min-height:calc(100svh - 2 * (var(--m) + var(--b)))}
.notes{grid-column:1;grid-row:1;padding:30px 40px 0 36px;max-width:640px}
.notes h2{font-size:13px;font-weight:600;letter-spacing:.08em;margin-bottom:10px}
.notes ol{list-style:none;counter-reset:n;font-size:17px;line-height:1.4}
.notes li{counter-increment:n;display:grid;grid-template-columns:28px 1fr;margin-bottom:6px}
.notes li:before{content:counter(n) ".";font-weight:600}
.notes li:first-child{font-size:24px;font-weight:600;line-height:1.2;margin-bottom:12px}
.notes li.demo{color:var(--gris);font-size:15px;margin-top:4px}.notes li.demo b{color:var(--encre);font-weight:600}
.notes li:first-child:before{font-size:17px;padding-top:4px}
.plan{grid-column:1;grid-row:2;display:flex;align-items:center;justify-content:center;padding:12px 40px 28px 16px;min-height:0}
.plan-svg{width:100%;max-width:820px;height:100%}
@media (min-width:861px) and (min-height:700px){.dessin{height:calc(100svh - 2 * (var(--m) + var(--b)));min-height:0}}
.plan-svg .cote{font:500 15px Barlow,sans-serif;fill:var(--encre)}
.plan-svg .legende{font:600 15px Barlow,sans-serif;fill:var(--encre);letter-spacing:.02em}
.redline text{font:italic 500 15px Barlow,sans-serif;fill:var(--rouge)}
.redline path{stroke:var(--rouge);stroke-width:1.4;fill:none}

.droite{grid-column:2;grid-row:1 / 3;display:flex;flex-direction:column;justify-content:flex-end;gap:16px}
.revs{margin-bottom:auto;border-left:1px solid var(--encre);border-bottom:1px solid var(--encre);border-collapse:collapse;width:100%;font-size:13px}
.revs caption{text-align:left;font-weight:600;font-size:13px;letter-spacing:.08em;padding:8px 12px;border-left:1px solid var(--encre);border-bottom:1px solid var(--encre);caption-side:top}
.revs th,.revs td{border-bottom:1px solid var(--encre);padding:5px 12px;text-align:left;font-weight:500}
.revs th{font-weight:600;color:var(--gris);font-size:13px}
.revs td + td,.revs th + th{border-left:1px solid var(--encre)}
.revs tr:last-child td{border-bottom:0}
.revs .c{color:var(--rouge)}

/* ---------- le cartouche : c'est ici qu'on signe ---------- */
.cartouche{background:var(--papier);border-left:2px solid var(--encre);border-top:2px solid var(--encre);
  display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr) minmax(0,.8fr) minmax(0,1fr)}
.cartouche > *{border-bottom:1px solid var(--encre);padding:9px 14px}
.cartouche > * + *{border-left:1px solid var(--encre)}
.cartouche .plein{grid-column:1 / -1;border-left:0}
.cartouche .k{display:block;font-size:13px;color:var(--gris);line-height:1.2;margin-bottom:3px}
.cartouche .v{font-size:15px;font-weight:600;overflow-wrap:anywhere}
.marque{grid-column:1 / 4;display:flex;align-items:center;gap:10px;font-size:24px;font-weight:700;letter-spacing:.005em}
.marque svg{width:24px;height:24px}
.titre{padding:12px 18px 10px}
.titre h1{font-size:30px;font-weight:600;line-height:1.1;letter-spacing:-.005em}
.corps{padding:16px 18px 14px}
.cartouche .bas > *{border-bottom:0}

/* ---------- formulaire ---------- */
.f{display:flex;flex-direction:column}
.f label,.f .lbl{font-size:15px;font-weight:500;margin-bottom:6px}
.lr{display:grid;grid-template-columns:1fr auto;align-items:baseline;column-gap:12px}
.lr label{grid-row:1;grid-column:1}.lr #oubli{grid-row:1;grid-column:2}.lr .mdp,.lr .err{grid-column:1 / -1}
.lr a{font-size:15px}
.f input{width:100%;height:46px;border:1.5px solid var(--encre);background:var(--champ);padding:0 14px;font:inherit;font-size:17px;color:var(--encre);border-radius:0}
.f input:focus-visible{outline:3px solid var(--encre);outline-offset:0}
.f input[aria-invalid=true]{border-color:var(--rouge);box-shadow:inset 3px 0 0 var(--rouge)}
.champ{margin-bottom:12px}
.mdp{position:relative}
.mdp input{padding-right:92px}
.voir{position:absolute;right:6px;top:6px;height:36px;padding:0 10px;border:0;background:transparent;font:inherit;font-size:15px;font-weight:600;color:var(--encre);cursor:pointer;text-decoration:underline;text-underline-offset:3px}
.err{color:var(--rouge);font-size:15px;font-weight:500;margin-top:6px}
.btn{height:50px;border:2px solid var(--encre);font:inherit;font-size:17px;font-weight:600;cursor:pointer;border-radius:0;display:flex;align-items:center;justify-content:center;gap:10px;width:100%}
.btn.p{background:var(--encre);color:var(--papier)}
.btn.p:hover{background:#000}
.btn.p[aria-busy=true]{cursor:progress;background:#3A3D40;border-color:#3A3D40}
.btn.s{background:transparent;color:var(--encre);height:46px;font-size:17px;font-weight:500}
.alts{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.btn.s:hover{background:var(--encre);color:var(--papier)}
.btn svg{width:18px;height:18px;flex:none}
.ou{display:flex;align-items:center;gap:12px;margin:12px 0 10px;font-size:13px;color:var(--gris)}
.ou:before,.ou:after{content:"";flex:1;border-top:1px solid var(--encre)}
.nouveau{margin-top:12px;font-size:15px;color:var(--gris)}.nouveau a{color:var(--encre);font-weight:500}
.msg{border-left:3px solid var(--rouge);padding:2px 0 2px 12px;margin-bottom:16px;font-size:15px}
.msg strong{color:var(--rouge);font-weight:600}
.msg strong:after{content:" "}
.msg.info{border-left-color:var(--encre)}.msg.info strong{color:var(--encre)}
.msg:focus{outline:none}
.signe{color:var(--encre)}
.signe.vide{color:var(--gris);font-weight:500}
.ok .titre h1:after{content:"";display:inline-block;width:.5em;height:.28em;border-left:3px solid currentColor;border-bottom:3px solid currentColor;transform:rotate(-45deg) translate(.08em,-.18em);margin-left:.35em}

@media (prefers-reduced-motion:no-preference){
  .nuage{stroke-dasharray:var(--len);stroke-dashoffset:var(--len);animation:trace .9s .25s cubic-bezier(.4,0,.2,1) forwards}
  .redline{opacity:0;animation:apparait .3s 1.05s forwards}
  @keyframes trace{to{stroke-dashoffset:0}}
  @keyframes apparait{to{opacity:1}}
}

/* ---------- entre bureau et téléphone ---------- */
@media (max-width:1180px){.dessin{grid-template-columns:minmax(0,1fr) 440px}}
@media (max-height:820px) and (min-width:861px){.revs{display:none}.notes ol li:nth-child(2),.notes ol li:nth-child(3){display:none}.corps{padding-top:14px}.champ{margin-bottom:12px}}

/* ---------- téléphone : le cartouche devient l'écran ---------- */
@media (max-width:860px){
  :root{--m:8px;--b:14px}
  .zones{font-size:11px}
  .zones .z5,.zones .z6,.zones .z7,.zones .z8{display:none}
  .dessin{display:flex;flex-direction:column;min-height:0}
  .revs{display:none}
  .droite{order:2;display:block}
  .plan{order:1;padding:4px 0 0;height:auto}
  .plan-svg{max-width:none;height:auto}
  .cartouche{margin-top:6px;border-left:0;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr)}
  .cartouche > *{border-left:0}
  .cartouche > :nth-child(2n):not(.plein){border-left:1px solid var(--encre)}
  .marque{grid-column:1}
  .cartouche .bas:nth-child(5),.cartouche .bas:nth-child(6){border-bottom:1px solid var(--encre)}
  .marque{font-size:17px}
  .titre{padding:12px 14px 10px}.titre h1{font-size:24px}
  .corps{padding:14px}
  .btn.s{font-size:15px}
  .notes{order:3;padding:22px 6px 18px;max-width:none}
  .notes li:first-child{font-size:17px}
  .notes ol{font-size:15px}
}
</style>
</head>
<body>
<main class="feuille">
  <div class="cadre" aria-hidden="true">
    <div class="zones h t">__ZH__</div><div class="zones h b">__ZH__</div>
    <div class="zones v l">__ZV__</div><div class="zones v r">__ZV__</div>
  </div>

  <div class="dessin">
    <section class="notes" aria-labelledby="notes-t">
      <h2 id="notes-t">NOTES</h2>
      <ol>
        <li><span>La revue de conception électronique, de la première pastille à la mise en fabrication.</span></li>
        <li><span>Chaque révision de carte est annotée, discutée, puis signée.</span></li>
        <li><span>Fichiers Gerber, perçage et nomenclature au même endroit.</span></li>
        <li class="demo"><span>Prototype : rien n'est envoyé. Compte de démonstration : <b>demo@example.com</b>, mot de passe <b>revision-c</b>.</span></li>
      </ol>
    </section>

    <div class="plan">__PLAN__</div>

    <div class="droite">
    <table class="revs" aria-hidden="true">
      <caption>RÉVISIONS</caption>
      <tr><th>Rév.</th><th>Description</th><th>Date</th><th>Approuvé</th></tr>
      <tr><td>A</td><td>Création</td><td>12.09.2026</td><td>oui</td></tr>
      <tr><td>B</td><td>Alimentation 3V3</td><td>03.10.2026</td><td>oui</td></tr>
      <tr><td class="c">C</td><td class="c">U3 déplacé, routage</td><td>—</td><td class="c">à signer</td></tr>
    </table>

    <section class="cartouche" id="cartouche" aria-labelledby="titre">
      <div class="marque"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.2" fill="none" stroke="currentColor" stroke-width="5.2"/></svg>Annular</div>
      <div><span class="k">Document</span><span class="v">Connexion</span></div>
      <div class="titre plein"><h1 id="titre">Se connecter</h1></div>
      <div class="corps plein">
        <form class="f" id="connexion" method="post" action="#connexion" novalidate>
          <div class="msg" id="msg" role="alert" tabindex="-1" hidden></div>
          <div class="champ">
            <label for="email">E-mail professionnel</label>
            <input id="email" name="email" type="email" autocomplete="username webauthn" inputmode="email" autocapitalize="none" spellcheck="false" required aria-describedby="email-err">
            <p class="err" id="email-err" hidden></p>
          </div>
          <div class="champ lr">
            <label for="mdp">Mot de passe</label>
            <div class="mdp">
              <input id="mdp" name="password" type="password" autocomplete="current-password" required aria-describedby="mdp-err">
              <button class="voir" type="button" id="voir" aria-controls="mdp" aria-pressed="false">Afficher</button>
            </div>
            <a href="#reinitialiser" id="oubli">Mot de passe oublié ?</a>
            <p class="err" id="mdp-err" hidden></p>
          </div>
          <button class="btn p" type="submit" id="go">Se connecter</button>
          <div class="ou" aria-hidden="true">ou</div>
          <div class="alts">
            <button class="btn s" type="button" id="cle"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="8" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 12h9m-3 0v3.5m-3-3.5v2.5" fill="none" stroke="currentColor" stroke-width="2"/></svg>Clé d'accès</button>
            <button class="btn s" type="button" id="sso">SSO de l'organisation</button>
          </div>
          <p class="nouveau">Pas encore de compte ? <a href="#acces">Demander un accès</a></p>
        </form>
      </div>
      <div class="bas"><span class="k">Approuvé par</span><output class="v signe vide" id="signe" for="email">à signer</output></div>
      <div class="bas"><span class="k">Date</span><span class="v" id="date">05.11.2026</span></div>
      <div class="bas"><span class="k">Feuille</span><span class="v">1 / 1</span></div>
      <div class="bas"><span class="k">Statut</span><span class="v">Prototype</span></div>
    </section>
    </div>
  </div>
</main>

<script>
(function(){
  var f=document.getElementById('connexion'), em=document.getElementById('email'), pw=document.getElementById('mdp');
  var go=document.getElementById('go'), msg=document.getElementById('msg'), signe=document.getElementById('signe');
  var eErr=document.getElementById('email-err'), pErr=document.getElementById('mdp-err'), cart=document.getElementById('cartouche');
  var d=new Date(); document.getElementById('date').textContent=('0'+d.getDate()).slice(-2)+'.'+('0'+(d.getMonth()+1)).slice(-2)+'.'+d.getFullYear();

  // le nuage de revue se trace une fois : sa longueur est mesurée sur le dessin réel
  var n=document.querySelector('.plan-svg path[stroke="#C8322A"]');
  if(n){n.classList.add('nuage'); n.style.setProperty('--len', Math.ceil(n.getTotalLength()));}

  // la signature : ce que l'on tape s'inscrit dans la case « Approuvé par »
  function sig(){var v=em.value.trim(); signe.textContent=v||'à signer'; signe.classList.toggle('vide',!v);}
  em.addEventListener('input',sig);

  function say(kind,title,text){msg.className='msg'+(kind==='info'?' info':''); msg.innerHTML='<strong></strong><span></span>';
    msg.firstChild.textContent=title; msg.lastChild.textContent=text; msg.hidden=false; msg.focus();}
  function field(input,err,text){input.setAttribute('aria-invalid',text?'true':'false'); err.textContent=text||''; err.hidden=!text;}

  document.getElementById('voir').addEventListener('click',function(){
    var on=pw.type==='password'; pw.type=on?'text':'password'; this.setAttribute('aria-pressed',on); this.textContent=on?'Masquer':'Afficher'; pw.focus();});

  f.addEventListener('submit',function(e){
    e.preventDefault(); msg.hidden=true;
    var v=em.value.trim(), ok=true;
    if(!v){field(em,eErr,'Saisissez votre e-mail professionnel.');ok=false;}
    else if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)){field(em,eErr,'Cette adresse ne semble pas complète : il manque peut-être le domaine (nom@entreprise.com).');ok=false;}
    else field(em,eErr,'');
    if(!pw.value){field(pw,pErr,'Saisissez votre mot de passe.');ok=false;} else field(pw,pErr,'');
    if(!ok){(em.getAttribute('aria-invalid')==='true'?em:pw).focus();return;}
    go.setAttribute('aria-busy','true'); go.disabled=true; go.textContent='Vérification…';
    setTimeout(function(){
      go.removeAttribute('aria-busy'); go.disabled=false;
      if(v.toLowerCase()==='demo@example.com'&&pw.value==='revision-c'){
        cart.classList.add('ok'); document.getElementById('titre').textContent='Signé';
        go.textContent='Ouverture de votre espace…'; go.disabled=true;
        say('info','Connexion réussie.','Prototype : l’espace de travail s’ouvrirait ici.');
      }else{
        go.textContent='Se connecter'; pw.value='';
        say('err','Connexion refusée :','e-mail ou mot de passe incorrect. Vérifiez la saisie ou réinitialisez le mot de passe.');
      }
    },900);
  });

  document.getElementById('oubli').addEventListener('click',function(e){e.preventDefault();
    var v=em.value.trim();
    say('info','Réinitialisation.', v ? 'Si un compte existe pour '+v+', un lien de réinitialisation vient d’être envoyé. (Prototype : rien n’est envoyé.)'
      : 'Saisissez d’abord votre e-mail professionnel, puis choisissez « Mot de passe oublié ? ».');
    if(!v) em.focus();});
  document.getElementById('cle').addEventListener('click',function(){
    say('info','Clé d’accès.','Votre appareil vous demanderait votre empreinte, votre visage ou le code de l’appareil. (Prototype : non relié à un serveur.)');});
  document.getElementById('sso').addEventListener('click',function(){
    say('info','Connexion unique (SSO).','Vous seriez redirigé vers le fournisseur d’identité de votre organisation. (Prototype : non relié.)');});
})();
</script>
</body>
</html>
"""

zh = "".join(f'<span class="z{i}">{i}</span>' for i in range(1, 9))
zv = "".join(f"<span>{c}</span>" for c in "ABCDEF")
out = HTML.replace("__ZH__", zh).replace("__ZV__", zv).replace("__PLAN__", PLAN)
(HERE / "site" / "index.html").write_text(out)
print("site/index.html", len(out))

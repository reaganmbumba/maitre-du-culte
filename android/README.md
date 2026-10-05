# Maître du Culte — Android

Application Android du maître du culte (EBNM) : rapport du culte, chrono,
règlement intérieur complet, rappels et notifications.

## Obtenir l'APK sans rien installer
1. Envoyer ce dossier dans un dépôt GitHub.
2. Onglet « Actions » : « Construire l'APK Android » démarre tout seul.
3. Télécharger `maitre-du-culte-apk`, puis l'installer sur le téléphone
   (autoriser « sources inconnues »).

## Construire sur un ordinateur (Windows, Mac ou Linux)
Prérequis : Node.js 20+ et Android Studio.

    npm install
    npx cap sync android
    npx cap open android    # puis Build > Build APK

## Google Play
Compte développeur Google (25 $ une seule fois), puis envoyer un AAB signé
(Android Studio : Build > Generate Signed Bundle).

## Espace administrateur
Réglages › Espace administrateur, protégé par le mot de passe administrateur
(communiqué par l'administration ; il n'est pas écrit en clair dans le code). L'administrateur y règle le numéro WhatsApp et l'e-mail
qui reçoivent les rapports, l'en-tête de la paroisse et le programme du culte.

## Rapport PDF
Rapport › « Envoyer le rapport (PDF) » : le PDF (logo KCC, tableau du
déroulement, vérifications, effectif, anomalies avec articles du règlement,
synthèse, signature) s'ouvre dans le menu de partage du téléphone. Choisir
WhatsApp ou la messagerie, puis le destinataire indiqué.

## Icône et écran de démarrage
Générés depuis `assets/` (logo KCC) avec `npx capacitor-assets generate`.

## Plusieurs paroisses
Au premier lancement, l'application demande le nom de la paroisse, la ville et le
nom du maître du culte. Ensuite, seul l'administrateur (code) peut changer la paroisse.

## Numéro WhatsApp et e-mail communs (configuration centrale)
`config-centrale.json` contient le numéro WhatsApp et l'e-mail qui reçoivent les
rapports. Publiez ce fichier en ligne (par exemple sur GitHub), puis indiquez son
adresse dans Réglages › Espace administrateur › Configuration centrale (ou dans
`CENTRAL_URL` de `www/index.html` avant de construire l'application).
Chaque téléphone relit ce fichier à l'ouverture : modifier le numéro dans ce
fichier le change pour toutes les paroisses. Sans Internet, le dernier numéro connu
est utilisé.

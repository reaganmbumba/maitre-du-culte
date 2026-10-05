# Maître du Culte — iPhone (iOS)

Application iPhone du maître du culte (EBNM) : rapport du culte, chrono,
règlement intérieur complet, rappels et notifications.

## Prérequis
- Un Mac avec Xcode (gratuit sur l'App Store).
- Node.js 20+.
- Pour installer sur un iPhone : un identifiant Apple (gratuit, 7 jours)
  ou un compte Apple Developer (99 $ par an) pour l'App Store et TestFlight.

## Construire
    npm install
    npx cap sync ios
    npx cap open ios        # Xcode s'ouvre

Dans Xcode : choisir l'équipe (Signing & Capabilities), brancher l'iPhone,
puis Run ▶. Pour l'App Store : Product > Archive, puis Distribute App.

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

# Maître du Culte

Application du maître du culte pour les paroisses de l'Église Bon Nouveau Message (KCC) : rapport du culte en PDF, rappels du règlement intérieur, envoi par WhatsApp ou e-mail.

## Contenu

| Dossier | Rôle |
|---|---|
| `android/` | Projet Android (Capacitor). L'APK est construit automatiquement par GitHub Actions. |
| `ios/` | Projet iOS (Capacitor). Se compile sur un Mac avec Xcode, voir `ios/README.md`. |
| `source/` | Source de l'application (`app.src.html`), règlement intérieur (`reglement.json`), logo et bibliothèques PDF. |
| `config.json` | Numéro WhatsApp et e-mail qui reçoivent les rapports de toutes les paroisses. |

## Activer le téléphone d'une paroisse

Chaque téléphone doit être approuvé par l'administration. Un téléphone non approuvé reste bloqué, même si on lui donne le nom d'une paroisse déjà active.

1. Le maître du culte installe l'application, choisit sa paroisse et indique son nom. L'application affiche « En attente d'activation » avec l'identifiant du téléphone (ex. `A7K2-9QX4`) et envoie la demande sur WhatsApp au numéro de `config.json`.
2. L'administrateur approuve le téléphone :
   - en transférant la demande à Claude dans le projet ;
   - ou avec `python3 tools/approuver.py "Paroisse de Pika" A7K2-9QX4 --ville Kikwit` ;
   - ou dans l'application : Réglages → Espace administrateur → Paroisses et téléphones, puis coller le texte produit dans `config.json`.
3. Dès qu'il a Internet, le téléphone se déverrouille tout seul.

Retirer un téléphone : `--retirer`. Suspendre toute une paroisse : `--suspendre` (et `--reactiver`). Liste : `--liste`.

Sur place, l'administrateur peut aussi activer un téléphone avec son mot de passe (bouton « Administrateur » de l'écran d'attente).

`config.json` ne contient pas les identifiants eux-mêmes, seulement leur empreinte. Avec `"activation": false`, l'application s'ouvre sans approbation.

## Changer le numéro ou l'e-mail de réception

Modifiez `config.json` directement sur GitHub (icône crayon), puis « Commit changes ». Toutes les applications le lisent au démarrage. Un champ laissé vide garde la valeur saisie dans l'espace administrateur du téléphone.

Le dépôt doit être **public** pour que les téléphones puissent lire ce fichier.

## Télécharger l'APK Android

Onglet **Actions** → dernière exécution « Construire l'APK Android » → section **Artifacts** → `maitre-du-culte-apk`. Pour relancer une construction : **Run workflow**.

## Modifier l'application

```
cd source
python3 build.py ../android/www
python3 build.py ../ios/www
```

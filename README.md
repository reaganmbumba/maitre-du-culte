# Maître du Culte

Application du maître du culte pour les paroisses de l'Église Bon Nouveau Message (KCC) : rapport du culte en PDF, rappels du règlement intérieur, envoi par WhatsApp ou e-mail.

## Contenu

| Dossier | Rôle |
|---|---|
| `android/` | Projet Android (Capacitor). L'APK est construit automatiquement par GitHub Actions. |
| `ios/` | Projet iOS (Capacitor). Se compile sur un Mac avec Xcode, voir `ios/README.md`. |
| `source/` | Source de l'application (`app.src.html`), règlement intérieur (`reglement.json`), logo et bibliothèques PDF. |
| `config.json` | Numéro WhatsApp et e-mail qui reçoivent les rapports de toutes les paroisses. |

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

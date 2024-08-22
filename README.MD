# CIS Bdpm Conversion and Processing

Ce projet contient deux scripts Python pour traiter un fichier texte contenant des informations sur les médicaments. Le projet inclut les étapes de conversion de l'encodage du fichier texte en UTF-8, suivie de son traitement pour générer un fichier JSON structuré.

## Structure du Projet

- **CIS_bdpm.txt** : Le fichier texte original contenant les données brutes sur les médicaments.
- **conversion.py** : Un script Python pour convertir le fichier texte d'origine en encodage UTF-8.
- **main.py** : Un script Python qui traite le fichier texte UTF-8 et le transforme en un fichier JSON structuré.
- **output.json** : Le fichier JSON généré contenant les données structurées.
- **README.md** : Ce fichier qui explique le projet et les scripts.

## Prérequis

- Python 3.x doit être installé sur votre système.
- Vous devez disposer des permissions pour lire et écrire des fichiers sur le système de fichiers.

## Utilisation

### Étape 1 : Conversion du fichier texte en UTF-8

Le fichier texte original (`CIS_bdpm.txt`) peut ne pas être encodé en UTF-8. Pour éviter les erreurs de décodage, utilisez le script `conversion.py` pour convertir le fichier en UTF-8.

```bash
python conversion.py

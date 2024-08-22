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
```
Cela créera un nouveau fichier nommé CIS_bdpm_utf8.txt.

### Étape 2 : Traitement du fichier UTF-8

Une fois le fichier converti en UTF-8, utilisez le script main.py pour traiter le fichier et générer un fichier JSON structuré.

```bash
python main.py
```
Cela générera un fichier output.json contenant les données des médicaments sous un format JSON structuré.

## Scripts
### conversion.py
Ce script lit le fichier texte d'origine et le réécrit en UTF-8. Il utilise latin-1 comme encodage de lecture, car il est couramment utilisé pour les textes en français.
Usage :
Lit : CIS_bdpm.txt
Écrit : CIS_bdpm_utf8.txt

### main.py
Ce script lit le fichier texte UTF-8 converti, extrait les données des médicaments, et les sauvegarde dans un fichier JSON structuré.
Usage :
Lit : CIS_bdpm_utf8.txt
Écrit : output.json
Exemple de Données
Les lignes de données dans CIS_bdpm.txt ont le format suivant :

```bash
CodeCIS  DénominationDuMédicament  FormePharmaceutique  VoiesDAdministration  StatutAMM  TypeDeProcédureAMM  ÉtatDeCommercialisation  DateD’AMM  StatutBdm  NuméroDeLAutorisationEuropéenne  Titulaire(s)  SurveillanceRenforcée
```
Le fichier output.json aura le format suivant :

json```
[
    {
        "Code CIS": "66864885",
        "Dénomination du médicament": "RISEDRONATE ARROW 35 mg, comprimé pelliculé",
        "Forme pharmaceutique": "comprimé pelliculé",
        "Voies d'administration": "orale",
        "Statut administratif de l’AMM": "Autorisation active",
        "Type de procédure AMM": "Procédure de reconnaissance mutuelle",
        "Etat de commercialisation": "Commercialisée",
        "Date d’AMM": "21/10/2011",
        "StatutBdm": "",
        "Numéro de l’autorisation européenne": "",
        "Titulaire(s)": "ARROW GENERIQUES",
        "Surveillance renforcée": "Non"
    },
    ...
]
```
Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

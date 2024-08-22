import json

# Fonction pour nettoyer et normaliser les données d'une ligne
def normalize_line(line):
    parts = line.split('\t')
    data = {
        "Code CIS": parts[0].strip(),
        "Dénomination du médicament": parts[1].strip(),
        "Forme pharmaceutique": parts[2].strip(),
        "Voies d'administration": parts[3].strip(),
        "Statut administratif de l’AMM": parts[4].strip(),
        "Type de procédure AMM": parts[5].strip(),
        "Etat de commercialisation": parts[6].strip(),
        "Date d’AMM": parts[7].strip(),
        "StatutBdm": parts[8].strip() if len(parts) > 8 else "",
        "Numéro de l’autorisation européenne": parts[9].strip() if len(parts) > 9 else "",
        "Titulaire(s)": parts[10].strip() if len(parts) > 10 else "",
        "Surveillance renforcée": parts[11].strip() if len(parts) > 11 else ""
    }
    return data

# Lecture du fichier texte
input_file = 'CIS_bdpm.txt'
output_file = 'output.json'

# Liste pour stocker les données transformées
medicaments = []

with open(input_file, 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():  # Ignorer les lignes vides
            medicament = normalize_line(line)
            medicaments.append(medicament)

# Écriture des données dans un fichier JSON
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(medicaments, json_file, ensure_ascii=False, indent=4)

print(f"Le fichier JSON a été généré sous le nom '{output_file}'.")

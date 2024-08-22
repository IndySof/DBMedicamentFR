# Chemins des fichiers
input_file = 'votre_fichier.txt'
converted_file = 'votre_fichier_utf8.txt'

# Convertir le fichier en UTF-8
with open(input_file, 'r', encoding='latin-1') as file:
    content = file.read()

with open(converted_file, 'w', encoding='utf-8') as file:
    file.write(content)

print(f"Le fichier a été converti en UTF-8 sous le nom '{converted_file}'.")

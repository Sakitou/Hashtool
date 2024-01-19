# Hashtool

Ce script Python permet de calculer les hashs (SHA256, SHA1, SHA512, MD5) pour un texte donné, le contenu d'un fichier ou de comparer deux fichiers.

## Utilisation

### Calculer les hashs pour un texte

```bash
./hashtext.py -s "exemple-de-mot"
```

### Calculer les hashs pour le contenu d'un fichier

```bash
./hashtext.py -f chemin-vers-fichier
```

### Comparer deux fichiers

```bash
./hashtext.py -c chemin-vers-fichier1 chemin-vers-fichier2
```

## Exécution

Assurez-vous que le script est exécutable :

```bash
chmod +x hashtext.py
```

Ensuite, vous pouvez utiliser les commandes décrites ci-dessus.

## Remarques

- Si un fichier spécifié n'existe pas, le script affichera un message d'erreur.
- Le script utilise l'encodage 'replace' pour lire le contenu des fichiers, cela peut entraîner des caractères spéciaux dans les hashs si le fichier n'est pas en texte brut.

N'hésitez pas à explorer et à modifier le script selon vos besoins !

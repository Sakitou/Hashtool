#!/usr/bin/env python3

import hashlib
import argparse
import os

def calculate_hash(text):
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    sha1_hash = hashlib.sha1(text.encode()).hexdigest()
    sha512_hash = hashlib.sha512(text.encode()).hexdigest()
    md5_hash = hashlib.md5(text.encode()).hexdigest()

    return sha256_hash, sha1_hash, sha512_hash, md5_hash

def hash_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Le fichier {file_path} n'existe pas.")
        return

    with open(file_path, 'rb') as f:
        content = f.read()
        return calculate_hash(content.decode(errors='replace'))

def compare_files(file_path1, file_path2):
    hash1 = hash_file(file_path1)
    hash2 = hash_file(file_path2)

    if hash1 and hash2:
        return hash1 == hash2
    else:
        return False

def main():
    parser = argparse.ArgumentParser(description='Calculer et comparer les hashs.')
    parser.add_argument('-s', '--string', help='Calculer les hashs pour le texte fourni.')
    parser.add_argument('-f', '--file', help='Calculer les hashs pour le contenu du fichier.')
    parser.add_argument('-c', '--compare', nargs=2, help='Comparer deux fichiers.')

    args = parser.parse_args()

    if args.string:
        print("Calcul en cours...")
        sha256, sha1, sha512, md5 = calculate_hash(args.string)
        print(f"SHA256 : {sha256}\nSHA1 : {sha1}\nSHA512 : {sha512}\nMD5 : {md5}")

    elif args.file:
        print("Calcul en cours...")
        sha256, sha1, sha512, md5 = hash_file(args.file)
        print(f"SHA256 : {sha256}\nSHA1 : {sha1}\nSHA512 : {sha512}\nMD5 : {md5}")

    elif args.compare:
        file1, file2 = args.compare
        if compare_files(file1, file2):
            print("Les fichiers correspondent.")
        else:
            print("Les fichiers ne correspondent pas.")

if __name__ == "__main__":
    main()

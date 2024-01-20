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
        print(f"The file {file_path} does not exist.")
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
    parser = argparse.ArgumentParser(description='Calculate and compare hashes.')
    parser.add_argument('-s', '--string', help='Calculate hashes for the provided text.')
    parser.add_argument('-f', '--file', help='Calculate hashes for the contents of the file.')
    parser.add_argument('-c', '--compare', nargs=2, help='Compare two files.')

    args = parser.parse_args()

    if args.string:
        print("Calculating...")
        sha256, sha1, sha512, md5 = calculate_hash(args.string)
        print(f"SHA256: {sha256}\nSHA1: {sha1}\nSHA512: {sha512}\nMD5: {md5}")

    elif args.file:
        print("Calculating...")
        sha256, sha1, sha512, md5 = hash_file(args.file)
        print(f"SHA256: {sha256}\nSHA1: {sha1}\nSHA512: {sha512}\nMD5: {md5}")

    elif args.compare:
        file1, file2 = args.compare
        if compare_files(file1, file2):
            print("The files match.")
        else:
            print("The files do not match.")

if __name__ == "__main__":
    main()

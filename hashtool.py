#!/usr/bin/env python3

# Hashtools is a Python script for calculating and comparing hashes by Sakitou.
# github.com/Sakitou/Hashtool

import hashlib
import argparse
import os
import tkinter as tk
from tkinter import filedialog

class HashToolGUI:
    def __init__(self, master):
        self.master = master
        master.title("HashTool GUI")
        master.geometry("620x410")

        self.label = tk.Label(master, text="Text/File to hash:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=50)
        self.entry.pack(pady=10)

        self.calculate_button = tk.Button(master, text="Calculate Hash", command=self.calculate_hash)
        self.calculate_button.pack(pady=10)

        self.compare_button = tk.Button(master, text="Compare Files", command=self.compare_files)
        self.compare_button.pack(pady=10)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=10)

        self.result_text = tk.Text(master, height=45, width=75, state=tk.DISABLED, wrap=tk.WORD) 
        self.result_text.pack(pady=10)

    def calculate_hash(self):
        input_text = self.entry.get()
        if os.path.isfile(input_text):
            hash_result = hash_file(input_text)
            if hash_result:
                result_text = f"SHA256: {hash_result[0]}\nSHA1: {hash_result[1]}\nSHA512: {hash_result[2]}\nMD5: {hash_result[3]}"
            else:
                result_text = "Error calculating hash for the file."
        else:
            hash_result = calculate_hash(input_text)
            result_text = f"SHA256: {hash_result[0]}\nSHA1: {hash_result[1]}\nSHA512: {hash_result[2]}\nMD5: {hash_result[3]}"

        self.display_result(result_text)

    def compare_files(self):
        file_path1 = self.browse_file("Select the first file for comparison")
        file_path2 = self.browse_file("Select the second file for comparison")

        if file_path1 and file_path2:
            if compare_files(file_path1, file_path2):
                result_text = "The files match."
            else:
                result_text = "The files do not match."
        else:
            result_text = "Error selecting files for comparison."

        self.display_result(result_text)

    def browse_file(self, title="Select a file"):
        file_path = filedialog.askopenfilename(title=title)
        if file_path:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, file_path)
        return file_path

    def display_result(self, result_text):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_text)
        self.result_text.config(state=tk.DISABLED)

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
    if not os.path.isfile(file_path1) or not os.path.isfile(file_path2):
        print("Both files must exist for comparison.")
        return False

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
    parser.add_argument('-i', '--interface', action='store_true', help='Launch the GUI interface.')

    args = parser.parse_args()

    if args.interface:
        root = tk.Tk()
        app = HashToolGUI(root)
        root.mainloop()
    else:
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

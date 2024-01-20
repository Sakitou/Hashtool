# Hashtools

Hashtools is a Python script for calculating and comparing hashes by Sakitou.

## Usage

### Calculate Hashes for a String
```bash
python hashtool.py -s "your_text_here"
```

### Calculate Hashes for a File
```bash
python hashtool.py -f /path/to/your/file
```

### Compare Two Files
```bash
python hashtool.py -c /path/to/file1 /path/to/file2
```

## Installation

To use hashtool as a command, follow these steps:

1. Move the script to "/usr/local/bin/":
   ```bash
   sudo mv hashtool.py /usr/local/bin/
   ```

2. Rename the script to "hashtool":
   ```bash
   sudo mv /usr/local/bin/hashtool.py /usr/local/bin/hashtool
   ```

3. Make it executable:
   ```bash
   sudo chmod +x /usr/local/bin/hashtool
   ```

Now, you can use the `hashtool` command globally.

## License

This script is licensed under the GNU General Public License (GPL) - see the [LICENSE.md](LICENSE) file for details.

## GitHub Repository

For more information, contributions, or issues, visit the [Hashtools GitHub repository](https://github.com/Sakitou/Hashtools/).

# Hashtools

Hashtools is a Python script for calculating and comparing hashes by Sakitou.

## Usage

### Start GUI (BETA)
```bash
htool -i
```
### Calculate Hashes for a String
```bash
htool -s "your_text_here"
```

### Calculate Hashes for a File
```bash
htool -f /path/to/your/file
```

### Compare Two Files
```bash
htool -c /path/to/file1 /path/to/file2
```

## Installation

To use hashtool as a command, follow these steps:

1. Move the script to "/usr/local/bin/":
   ```bash
   sudo mv hashtool.py /usr/local/bin/
   ```

2. Rename the script to "htool":
   ```bash
   sudo mv /usr/local/bin/hashtool.py /usr/local/bin/htool
   ```

3. Make it executable:
   ```bash
   sudo chmod +x /usr/local/bin/htool
   ```
Or you can do it in one line: 

```bash
sudo cp hashtool.py /usr/local/bin/htool && sudo chmod +x /usr/local/bin/htool
```

Now, you can use the `htool -<option>` command globally.

## License

This script is licensed under the GNU General Public License (GPL) - see the [LICENSE](LICENSE.md) file for details.

## GitHub Repository

For more information, contributions, or issues, visit the [Hashtools GitHub repository](https://github.com/Sakitou/Hashtools/).

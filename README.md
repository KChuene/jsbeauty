# jsbeauty
Python jsbeautify wrapper script for quick use. Checkout the `jsbeautifier` repo [here](https://github.com/beautifier/js-beautify), if you will.

## General usage
```
python3 jsbeauty.py [OPTION] /path/to/file
```
**Options:**
- **`-f`:** Read list of file paths to beautify.
- **`-dir`:** Read files (all) from a directory.

## Usage examples
**Run on a set of files**
```
python3 jsbeauty.py file1.js file2.js ...
```
**Run from a file list**
```
python3 jsbeauty.py -f /path/to/filelist.txt
```
**Run on a directory**
```
python3 jsbeauty.py -dir /path/to/directory
```

> **Info:**
> All js beautify outputs are saved to a `.jsb` file named as `original-file.ext.jsb`
>

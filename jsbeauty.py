#!/bin/python3

import jsbeautifier as jsb
import sys
import os

options = jsb.default_options()
options.indent_size = 4

def usage():
    print("Usage:")
    print("\tjsbeauty /p/to/file1 /p/to/file2 ...")
    print("\tjsbeauty OPTION /path/to/file")
    print("\nOptions:")
    print("-f   Read list of files.")
    print("-dir Read files in directory.")
    sys.exit()

def dread(dpath: str):
    if not os.path.exists(dpath):
        print("(error) Directory not found.")
        sys.exit()

    dlist, result = os.listdir(dpath), []
    for elem in dlist:
        if os.path.isdir(elem): 
            continue
        result.append(f"{dpath}/{elem}")
    return result

def fread(fpath: str):
    if not os.path.exists(fpath):
        print("(error) File not found.")
        sys.exit()

    with open(fpath, "r") as reader:
        return [
            line.strip() for line in reader
        ]

def fwrite(fpath: str, data: str):
    with open(fpath, "w") as writer:
        writer.write(data)
        writer.flush()

def beautifyall(files: list[str]):
    for elem in files:
        ofile = f"{elem}.jsb"
        try:
            odata = jsb.beautify_file(elem)

            print(f"(info) {elem} : {ofile}")
            fwrite(ofile, odata)

        except Exception as ex:
            print(f"(error) {ex}")

args = sys.argv
if __name__=="__main__":
    files = []
    if "-h" in args or "--help" in args:
        usage()
    elif "-f" in args:
        optid = args.index("-f")
        files = fread(args[optid + 1] if optid < len(args)-1 else "")
    elif "-dir" in args:
        optid = args.index("-dir")
        files = dread(args[optid + 1] if optid < len(args)-1 else "")
    else:
        files = args[1:]

    print("(info) Beautifying {len(files)} file(s).")
    beautifyall(files)
    print("(info) Done.")

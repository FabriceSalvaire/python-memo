from pathlib import Path
import os.path
import sys

def make_file(path: Path | str, path_encoding: str = 'utf8') -> None:
    _ = str(path).encode(path_encoding)
    print(f"make file '{_}'")
    if not os.path.exists(_):
        with open(_, 'w') as fh:
            fh.write('')

# Create a directory
ROOT = Path('./path-encoding')
ROOT.mkdir(exist_ok=True)

# Create a UTF-8 filename
éléphant = ROOT / 'éléphant-utf8'
make_file(éléphant, 'utf8')

# Create a bad encoding filename
éléphant = ROOT / 'éléphant-latin1'
make_file(éléphant, 'latin1')

for root, directories, files in ROOT.walk():
    print(files)
    #  ['éléphant-utf8', '\udce9l\udce9phant-latin1']
    for _ in files:
        #! print(_)
        #  UnicodeEncodeError: 'utf-8' codec can't encode character '\udce9' in position 0: surrogates not allowed
        sys.stdout.buffer.write(str(_).encode('utf8', 'surrogateescape'))

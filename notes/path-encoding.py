####################################################################################################
#
# Published at https://gist.github.com/FabriceSalvaire/69e55e55ae82575370093ca409017b16
# and
# [Python 3: os.walk() file paths UnicodeEncodeError: 'utf-8' codec can't encode: surrogates not allowed - Stack Overflow](https://stackoverflow.com/questions/27366479/python-3-os-walk-file-paths-unicodeencodeerror-utf-8-codec-cant-encode-s)
#
####################################################################################################

from pathlib import Path
import os.path
import sys

# [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
print('sys.getfilesystemencoding:', sys.getfilesystemencoding())
# sys.getfilesystemencoding: utf-8
print('sys.getfilesystemencodeerrors:', sys.getfilesystemencodeerrors())
# sys.getfilesystemencodeerrors: surrogateescape
print()

####################################################################################################

def make_file(path: Path | str, path_encoding: str = 'utf8') -> None:
    _ = str(path).encode(path_encoding)
    print(f"make file '{_}'")
    if not os.path.exists(_):
        with open(_, 'w') as fh:
            fh.write('')

####################################################################################################

# Create a directory
ROOT = Path('./path-encoding')
ROOT.mkdir(exist_ok=True)

# Create a UTF-8 filename
éléphant = ROOT / 'éléphant-utf8'
make_file(éléphant, 'utf8')

# Create a bad encoding filename
éléphant = ROOT / 'éléphant-latin1'
make_file(éléphant, 'latin1')
# ls print on console: ?l?phant

print()
print('Using os and bytes')
for root, directories, files in os.walk(str(ROOT).encode('utf8')):
    print(files)
    # [b'\xc3\xa9l\xc3\xa9phant-utf8', b'\xe9l\xe9phant-latin1']
    for _ in files:
        print(_)
        # same as before

print()
print('Using os')
for root, directories, files in os.walk(ROOT):
    print(files)
    # aka print(str(files))
    # os.walk use surrogateescape \udce9 under the hood
    #   see [os.fsdecode](https://docs.python.org/3/library/os.html#os.fsdecode)
    # for some reasons Python is able to print a list of str...
    # ['éléphant-utf8', '\udce9l\udce9phant-latin1']
    for _ in files:
        # print(_)
        #   UnicodeEncodeError: 'utf-8' codec can't encode character '\udce9' in position 0: surrogates not allowed
        _ = os.path.join(root, _)
        # print(_)
        #   UnicodeEncodeError: 'utf-8' codec can't encode character '\udce9' in position 14: surrogates not allowed
        # We use a lower level API for STDOUT
        #   sys.getfilesystemencodeerrors() = surrogateescape
        #   warning: it will fails if sys.stdout is replaced with file-like objects like io.StringIO
        sys.stdout.buffer.write(_.encode('utf8', 'surrogateescape'))
        sys.stdout.write(os.linesep)
        # path-encoding/�l�phant-latin1

print()
print('Using pathlib')
for root, directories, files in ROOT.walk():
    print(files)
    # same as for os.walk
    for _ in files:
        _ = root / _
        # bad encoding is not an issue for pathlib
        if _.exists():
            print(_.stat())
        # but
        # print(_)
        # same issue
        sys.stdout.buffer.write(str(_).encode('utf8', 'surrogateescape'))
        sys.stdout.write(os.linesep)

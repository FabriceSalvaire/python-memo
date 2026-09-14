####################################################################################################

# [List of Unicode characters - Wikipedia](https://en.wikipedia.org/wiki/List_of_Unicode_characters)
# [Unicode 17.0 Character Code Charts](https://www.unicode.org/charts)

# [pyicu — GitLab](https://gitlab.pyicu.org/main/pyicu)

####################################################################################################

import unicodedata

####################################################################################################
#
# To sort correctly latin and unicode
#

from icu import Collator, Locale

collator = Collator.createInstance(Locale('fr_FR'))
def usorted(iter: list, key: str = None) -> list:
    if key is not None:
        return sorted(iter, key=lambda _: collator.getSortKey(getattr(_, key)))
    else:
        return sorted(iter, key=collator.getSortKey)

####################################################################################################

# \ooo       Octal character
# \xhh       Hexadecimal character
# \N{name}   Named Unicode character
# \uxxxx     Hexadecimal Unicode character
# \Uxxxxxxxx Hexadecimal Unicode character

print('\N{LATIN CAPITAL LETTER P}   \N{SNAKE}')

# ord: unicode -> int
# chr: int -> unicode
ord('(')
chr(40)
unicodedata.lookup('LEFT PARENTHESIS')
unicodedata.name('(')

# unicodedata.lookup('MIDDLE DOT') == '\N{MIDDLE DOT}'

####################################################################################################

# Code point ↔ UTF-8 conversion
#   | First code point | Last code point | Byte 1    | Byte 2    | Byte 3    | Byte 4    |
#   | U+0000           | U+007F          | 0yyy zzzz |
#   | U+0080           | U+07FF          | 110x xxyy | 10yy zzzz |
#   | U+0800           | U+FFFF          | 1110 wwww | 10xx xxyy | 10yy zzzz |           |
#   | U+010000         | U+10FFFF        | 1111 0uvv | 10vv wwww | 10xx xxyy | 10yy zzzz |
#
#   0... .... is a 1-byte char
#   leading 1 encodes the number of bytes
#   10.. .... is a continuation byte

# surrogates means « substitut »
# Surrogates blocks of 1024 characters
#   High Surrogates             U+D800 - U+DB7F
#   High Private Use Surrogates U+DB80 - U+DBFF
#   Low Surrogates              U+DC00 - U+DFFF

# Surrogate pairs
#   The way to represent more than 2**16 symbols with 16-bit
#   characters is to designate some of the “characters” as meta
#   characters. These special characters represent half of a pair of
#   16-bit units corresponding to a single Unicode character.

#   2**16 + 2**10 * (H − 55396) + (L − 56320)
#   where 55396 = 0xD800 and 56320 = 0xDC00

#   rocket emoji has Unicode value U+1F680
#     0x DB3D DE80
#     2**16 + 2**10 * (0xDB3D - 0xD800) + (0xDE80 - 0xDC00)

'éléphant'.encode('latin1').decode('latin1')
# 'éléphant'.encode('latin1').decode('utf8')
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 0: invalid continuation byte

print()
_ = 'éléphant'.encode('utf8')
print(_)
# b'\xc3\xa9l\xc3\xa9phant'
# é is U+E9 -> 1110 1001 -> UTF-8 (110x xxyy) (10yy zzzz) -> (110.0 0011) (10.10 1001) -> \xc3 \xa9

l1 = 'éléphant'.encode('latin1')
print(l1)
# b'\xe9l\xe9phant'
# 1110 1001
# same as unicode but \xc3 is missing

try:
    l1.decode(encoding='utf8', errors='strict')   # default
except UnicodeDecodeError:
    pass
print('replace', l1.decode(encoding='utf8', errors='replace'))
print('ignore', l1.decode(encoding='utf8', errors='ignore'))

# use hexadecimal form of Unicode code point with formats \xhh \uxxxx \Uxxxxxxxx
# NOT COMPATIBLE with Windows Path
br = l1.decode(encoding='utf8', errors='backslashreplace')
print('backslashreplace', br)
for i, c in enumerate(br):
    name = unicodedata.name(c)
    print(f"@{i} '{c}' / {ord(c)} / {name}")

# Allow encoding and decoding surrogate code point (U+D800 - U+DFFF) as normal code point
#! print('backslashreplace', _.decode(encoding='utf8', errors='surrogatepass'))

# replace non-decodable bytes >= 128 with individual surrogate code ranging from U+DC80 (128) to U+DCFF (255)
# [PEP 383 – Non-decodable Bytes in System Character Interfaces | peps.python.org](https://peps.python.org/pep-0383/)
# 128 limit is for security
se = l1.decode(encoding='utf8', errors='surrogateescape')
# print('surrogateescape', se)
# UnicodeEncodeError: 'utf-8' codec can't encode character '\udce9' in position 0: surrogates not allowed

print()
print('surrogateescape')
for i, c in enumerate(se):
    try:
        name = unicodedata.name(c)
        print(f"@{i} '{c}' / {ord(c)} / {name}")
    except ValueError:
        unicode_id = ord(c)
        # Low Surrogates, U+DC00 - U+DFFF
        offset = unicode_id - 0xDC00
        print(f"@{i} surrogate / {unicode_id} / 0x{unicode_id:X} / offset 0x{offset:X}")
        # ISO/CEI 8859-1: 0xE9 char is 'é'

# decode
bad_utf8 = b'C\xc3N'.decode(encoding='utf8', errors='surrogateescape')
# encode
bad_utf8.encode(encoding='utf8', errors='surrogateescape')
# print(bad_utf8)
# UnicodeEncodeError: 'utf-8' codec can't encode character '\udcc3' in position 1: surrogates not allowed

####################################################################################################

# https://gist.github.com/tylerneylon/9773800

def is_cont(x) -> bool:
    # tests if a char is a continuation byte in utf8
    # x & 11.00 0000 == 10.00 0000
    return (x & 0xc0) == 0x80

def clz(c) -> int:
    # Count # of leading 1 bits
    count = 0
    i = 7
    while i > 0:
        mask = 1 << i
        if c & mask:
            count += 1
        else:
            break
        i -= 1
    return count

# This returns the code point encoded at **s and advances *s to point to the
# next character. Thus it can easily be used in a loop.
def decode_code_point(buffer, i=0) -> tuple[int | None, int]:
    c = buffer[i]
    # All 1s with k leading 0s
    k = clz(c)
    mask = (1 << (8 - k)) - 1
    value = c & mask
    print(f"  @{i} c={c:x} {c:b} mask={k}-{mask:b} {value}")
    # k = 0 for one-byte code points; otherwise, k = #total bytes
    k -= 1
    i += 1
    while k > 0:
        c = buffer[i]
        if not is_cont(c):
            return None, i
        value <<= 6
        value += c & 0x3F
        k -= 1
        i += 1
    return value, i

print()
buffer = 'éléphant'.encode('utf8')
print(buffer)
i = 0
while i < len(buffer):
    j = i
    c, i = decode_code_point(buffer, i)
    print(f"@{j:3} {c:6} {chr(c)}")

print()
buffer = 'éléphant'.encode('latin1')
print(buffer)
i = 0
while i < len(buffer):
    j = i
    c, i = decode_code_point(buffer, i)
    if c is not None:
        print(f"@{j:3} {c:6} '{chr(c)}'")
    else:
        print(f"@{j:3} invalid {buffer[j]:x}")

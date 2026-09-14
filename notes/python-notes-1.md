```
p = Path('/etc')
q = p / 'init.d' / 'reboot'

with q.open() as f: f.readline()

PurePath('a/b.py').match('*.py')

p.with_name('setup.py')
p.with_stem('final')
p.with_suffix('.bz2')

for child in p.iterdir(): child

Path.mkdir()

Path.read_bytes()
Path.read_text(encoding=None, errors=None)
Path.write_bytes(data)
Path.write_text(data, encoding=None, errors=None, newline=None)
```

```
type Point = tuple[float, float]

PEP 678: Exceptions can be enriched with notes

def return_self(self) -> Self:
def foo(arg: Optional[int] = None) -> None:

 class collections.abc.MappingView
class collections.abc.ItemsView
class collections.abc.KeysView
class collections.abc.ValuesView
```

namedtuple() factory function for creating tuple subclasses with named fields
deque list-like container with fast appends and pops on either end
ChainMap dict-like class for creating a single view of multiple mappings
Counter dict subclass for counting hashable objects
OrderedDict dict subclass that remembers the order entries were added
defaultdict dict subclass that calls a factory function to supply missing values
UserDict wrapper around dictionary objects for easier dict subclassing
UserList wrapper around list objects for easier list subclassing
UserString wrapper around string objects for easier string subclassing

---

- func to reformat def

---

[How to use modern string formatting options with Python's logging module? - Stack Overflow](https://stackoverflow.com/questions/13500813/how-to-use-modern-string-formatting-options-with-pythons-logging-module)
[Python 3.7 logging: f-strings vs % - Stack Overflow](https://stackoverflow.com/questions/54367975/python-3-7-logging-f-strings-vs)
[Logging HOWTO — Python 3.12.1 documentation](https://docs.python.org/3/howto/logging.html#optimization)

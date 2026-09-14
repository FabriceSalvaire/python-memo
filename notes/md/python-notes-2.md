# Python Language Upgrade

## Type Hints

## PEP

* https://bugs.python.org/issue32954 Lazy Literal String Interpolation (PEP-498-based fl-strings)
* https://www.python.org/dev/peps/pep-0501 General purpose string interpolation

## Python 3.10

* PEP 634: Structural Pattern Matching

```
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the Internet"
```

## Python 3.9

* https://docs.python.org/3/whatsnew/3.9.html
* PEP 616 `str.removeprefix(prefix)` `str.removesuffix(suffix)`
* PEP 584 union operators added to dict

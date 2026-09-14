# [PEP 750 – Template Strings](https://peps.python.org/pep-0750)
# [string.templatelib — Support for template string literals — Python documentation](https://docs.python.org/3/library/string.templatelib.html)

import string.templatelib

variety = 'Stilton'
template = t'Try some {variety} cheese!'
print(template)
print(type(template))
# <class 'string.templatelib.Template'>
print(template.strings)
print(template.interpolations)
print(template.values)
print(list(template))
# ['Try some ', Interpolation('Stilton', 'variety', None, ''), ' cheese!']

# template + template
variety2 = 'cheddar'
template += t' and also {variety2}'
print(list(template))

# print(string.templatelib.convert(..., 's'))

def lower_upper(template: string.templatelib.Template) -> str:
    """Render static parts lowercase and interpolations uppercase."""
    parts = []
    for part in template:
        # if isinstance(part, Interpolation):
        #     parts.append(str(part.value).upper())
        # else:
        #     parts.append(part.lower())
        match part:
            case string.templatelib.Interpolation():
                print(f"value:       {part.value}")
                print(f"expression:  {part.expression}")
                print(f"conversion:  {part.conversion}")
                # `format_spec` can be arbitrary strings
                # including those that do not conform to the `format()` protocol
                print(f"format_spec: {part.format_spec}")
                _ = str(part.value).upper()
            case _:
                _ = part.lower()
        parts.append(_)
    return ''.join(parts)

name = 'Wenslydale'
template = t'Mister {name:>32}'
print(lower_upper(template))
# mister WENSLYDALE

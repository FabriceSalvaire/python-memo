# ...

- https://python-memo.fabrice-salvaire.fr/examples/memo-tools/Tools.html

- check for static generator update
- is it possible to use pyterate to generate

- move to github pages ???

- sphinx sucks API, js/css bundle
- check pyterate version ...
- getthecode need Sphinx API update review
- removed `restructured-text` need API update...
  see `tools/make-api-doc`
- example failure ??? `examples/references/generators.py`
- git temporary files change...

# To be fixed

- sphinx rtd use jquery
- rst sucks especially title syntax
- It would make sense to use md files with block codes !!!
- test pyterate """ syntax
- check there is a full pyterate example
- css
  what was the pygments style used for online version ???
  font size is smaller pre 12 vs 20 px / p 16 vs 20 x
  compare with rtd doc page
- errors
  ```
  doc/sphinx/source/examples/references/data-model.rst:379: ERROR: Unknown interpreted text role "frompy". [docutils]
  doc/sphinx/source/examples/references/data-model.rst:379: ERROR: Unknown interpreted text role "feature". [docutils]
  doc/sphinx/source/examples/references/data-model.rst:493: ERROR: Unknown interpreted text role "frompy". [docutils]
  doc/sphinx/source/examples/references/literals.rst:27: ERROR: Unknown interpreted text role "frompy". [docutils]
  doc/sphinx/source/examples/references/strings.rst:29: ERROR: Unknown interpreted text role "frompy". [docutils]
  ```
- error ???
  ```
  File ".venv/lib64/python3.14/site-packages/sphinx/environment/__init__.py", line 886, in _has_doc_changed
dep_path_is_file = dep_path.is_file()
^^^^^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'is_file'
  ```

# Fixed

- pyterate generate md -> added settings
- fixed in getthecode 1.3

  ```
  File "python-memo/.venv/lib64/python3.14/site-packages/sphinx/events.py", line 452, in emit
  raise ExtensionError(
  ...<3 lines>...
  ) from exc
  sphinx.errors.ExtensionError: Le gestionnaire <function process_getthedoc at 0x7f17d63803b0> de l'évènement 'doctree-read' a créé une exception. (exception: 'BuildEnvironment' object has no attribute 'warn_node')
  ```

  - was loaded two times
  - fixed toggle
  - ipynb path issue
    due to resolved .py symlink
    must check the fix...

- icon font missing
  -> custom theme css outdated
  ```
  downloadable font: download failed (font-family: "Lato" style:normal weight:700 stretch:100 src index:2): status=2152857618 source: file:///home/fabrice/home/developpement/python/python-memo/doc/sphinx/build/html/_static/fonts/Lato-Bold.ttf
  downloadable font: no supported format found (font-family: "FontAwesome" style:normal weight:400 stretch:100 src index:5) source: (end of source list) 
  ```

# Links

- [Markdown — Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/markdown.html#markdown)
- [sphinx.ext.viewcode – Add links to highlighted source code — Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html)
- [sphinx.ext.githubpages – Publish HTML docs in GitHub Pages — Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html)
- [Changelog — Sphinx documentation](https://www.sphinx-doc.org/en/master/changes/index.html)

- [readthedocs/sphinx_rtd_theme: Sphinx theme from Read the Docs](https://github.com/readthedocs/sphinx_rtd_theme)
- [Read the Docs Sphinx Theme — Read the Docs Sphinx Theme 3.1.0 documentation](https://sphinx-rtd-theme.readthedocs.io/en/stable/)

- [Configuration — Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-pygments_style)
- [Styles — Pygments](https://pygments.org/styles/)


- [jQuery Alternatives for Modern JavaScript](https://blog.openreplay.com/jquery-alternatives-modern-js/)
- [Umbrella JS](https://umbrellajs.com)

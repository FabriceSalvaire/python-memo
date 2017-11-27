.. include:: css-tricks.txt

.. _introduction:

==============
 Introduction
==============

Design of the memo
------------------

.. raw:: html

   <div class="reduced-width">

The design of the memo follows these guidelines:

* be concise

  It means that an **arbitrary decision** has to be made, **but** as opposite to Wikipedia, we can
  offer several articles covering the same topics.  Just because there is no right or wrong
  articles.  Articles must just be consistent with themselves.

* don't paraphrase the Python documentation
* add links to the reference documentation or corresponding PEP
* give the Python version of each new feature (**To Be Done**)
* enable indexing and cross-referencing
* examples must be didactic
* a memo source must be a true Python file that work everywhere

  i.e. reader can download, copy-past and execute the code on his machine

  e.g. use a temporary file hierarchy context manager to work on files and directories

.. raw:: html

   </div>

On which OS is made the memo ?
------------------------------

The memo is made on Linux (POSIX OS) thus outputs show UNIX paths ( e.g. `/foo/bar` ).

How to get the page source ?
----------------------------

You can **download** or **show** the raw python file using the icons on top of the pages.

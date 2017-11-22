===========
 Proposals
===========

Code Highlight
==============

.. code-block:: python
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'


.. code-block:: python3
   :linenos:

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'


.. code-block:: python3

   with TemporaryFileHierarchy() as tmp_directory:

       # change current working directory
       os.chdir(tmp_directory)
       print('curent directory is now:', os.getcwd())

       abs_path = os.path.join(tmp_directory, 'subdir', 'file1') + '.txt'
       pretty_print((
           os.path.dirname(abs_path),
           os.path.basename(abs_path), # ref 1
           os.path.splitext(abs_path),
       ))
       abs_path = os.path.join(tmp_directory, 'subdir', '..', 'file1')
       pretty_print((
           abs_path,
           os.path.realpath(abs_path), # remove .. and symlinks
       ))
       abs_path = os.path.join('.', 'subdir', 'file1')
       pretty_print((
           abs_path,
           os.path.abspath(abs_path),
       ))


.. raw:: html

    <div class="highlight-python3"><div class="highlight"><pre><span></span><span class="k">with</span> <span class="n">TemporaryFileHierarchy</span><span class="p">()</span> <span class="k">as</span> <span class="n">tmp_directory</span><span class="p">:</span>
        <span class="c1"># change current working directory</span>
        <span class="n">os</span><span class="o">.</span><span class="n">chdir</span><span class="p">(</span><span class="n">tmp_directory</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="s1">'curent directory is now:'</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">getcwd</span><span class="p">())</span>
    
        <span class="n">abs_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">tmp_directory</span><span class="p">,</span> <span class="s1">'subdir'</span><span class="p">,</span> <span class="s1">'file1'</span><span class="p">)</span> <span class="o">+</span> <span class="s1">'.txt'</span>
        <span class="n">pretty_print</span><span class="p">((</span>
        <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n highlighted-feature">dirname</span><span class="p">(</span><span class="n">abs_path</span><span class="p">),</span>
        <span class="n highlighted-feature">os.path.basename</span><span class="p">(</span><span class="n">abs_path</span><span class="p">),</span><span class="c1 code-ref"># ref 1</span>
        <span class="n highlighted-feature">os.path.splitext</span><span class="p">(</span><span class="n">abs_path</span><span class="p">),</span>
        <span class="p">))</span>
        <span class="n">abs_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">tmp_directory</span><span class="p">,</span> <span class="s1">'subdir'</span><span class="p">,</span> <span class="s1">'..'</span><span class="p">,</span> <span class="s1">'file1'</span><span class="p">)</span>
        <span class="n">pretty_print</span><span class="p">((</span>
        <span class="n">abs_path</span><span class="p">,</span>
        <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">realpath</span><span class="p">(</span><span class="n">abs_path</span><span class="p">),</span> <span class="c1"># remove .. and symlinks</span>
        <span class="p">))</span>
        <span class="n">abs_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s1">'.'</span><span class="p">,</span> <span class="s1">'subdir'</span><span class="p">,</span> <span class="s1">'file1'</span><span class="p">)</span>
        <span class="n">pretty_print</span><span class="p">((</span>
        <span class="n">abs_path</span><span class="p">,</span>
        <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">abs_path</span><span class="p">),</span>
        <span class="p">))</span>
    </pre></div></div>

Banner
======

.. raw:: html

    <ul class="reference-doc-banner">
        <li><span class="python-version">since Python 3.6</span></li>
	<li><a class="reference-doc-link" href="https://docs.python.org/3/reference/expressions.html#generator-expressions">Reference</a></li>
        <li><a class="pep-link" href="https://www.python.org/dev/peps/pep-0525">PEP 525 – Asynchronous Generators</a></li>
    </ul>

foo


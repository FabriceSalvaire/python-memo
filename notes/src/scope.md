- [4. Execution model — Python 3.14.3 documentation](https://docs.python.org/3/reference/executionmodel.html)

## Binding of names

**The following constructs bind names:**
- formal parameters to functions
- class definitions
- function definitions
- assignment expressions
- targets that are identifiers if occurring in an assignment:
  - for loop header,
  - after as in a with statement, except clause, except* clause, or in the as-pattern in structural pattern matching,
  - in a capture pattern in structural pattern matching
- import statements
- type statements
- type parameter lists

The import statement of the form `from ... import *` binds all names defined in the imported module,
**except those beginning with an underscore**. This form may only be used **at the module level**.

??? A target occurring in a del statement is also considered bound for this purpose (though the actual
semantics are to unbind the name).

Each assignment or import statement occurs within a block defined by a class or function definition
or at the module level (the top-level code block).

If a name is bound in a **block**, it is a **local variable of that block**, unless declared as `nonlocal` or
`global`. If a name is bound **at the module level**, it is a **global variable**. (The variables of the
module code block are local and global.) If a variable is used in a code block but not defined
there, it is a free variable.

Each occurrence of a name in the program text refers to the binding of that name established by the
following name resolution rules.

## Resolution of names

A scope defines the visibility of a name within a block. If a local variable is defined in a **block**,
its scope includes that block. If the definition occurs in a **function block**, the scope extends to
any blocks contained within the defining one, unless a contained block introduces a different
binding for the name.

When a name is used in a code block, it is resolved using the **nearest enclosing scope**. The set of
all such scopes visible to a code block is called the block’s environment.

When a name is not found at all, a `NameError` exception is raised. If the current scope is a function
scope, and the name refers to a local variable that has not yet been bound to a value at the point
where the name is used, an `UnboundLocalError` exception is raised. `UnboundLocalError` is a subclass of
`NameError`.

If a name binding operation occurs anywhere within a code block, all uses of the name within the
block are treated as references to the current block. This can lead to errors when a name is used
within a block before it is bound. This rule is subtle. **Python lacks declarations and allows name
binding operations to occur anywhere within a code block.** The local variables of a code block can be
determined by scanning the entire text of the block for name binding operations. See the FAQ entry
on `UnboundLocalError` for examples.

If the `global` statement occurs within a block, all uses of the names specified in the statement
refer to the bindings of those names in the top-level namespace. Names are resolved in the top-level
namespace by searching the **global namespace**, i.e. the namespace of the module containing the code
block, and the **builtins namespace**, the namespace of the module builtins. The global namespace is
searched first. If the names are not found there, the builtins namespace is searched next. If the
names are also not found in the builtins namespace, **new variables are created in the global
namespace**. The global statement must precede all uses of the listed names.

The global statement has the same scope as a name binding operation in the same block. If the
nearest enclosing scope for a free variable contains a global statement, the free variable is
treated as a global.

The `nonlocal` statement causes corresponding names to refer to previously bound variables in the
nearest enclosing function scope. `SyntaxError` is raised at compile time if the given name does not
exist in any enclosing function scope. Type parameters cannot be rebound with the `nonlocal`
statement.

The namespace for a module is automatically created the first time a module is imported. The main
module for a script is always called `__main__`.

Class definition blocks and arguments to `exec()` and `eval()` are special in the context of name
resolution. A class definition is an executable statement that may use and define names. These
references follow the normal rules for name resolution with an exception that **unbound local
variables are looked up in the global namespace**. The namespace of the class definition becomes the
**attribute dictionary of the class**. The scope of names defined in a class block is limited to the
class block; it does not extend to the code blocks of methods. This includes comprehensions and
generator expressions, but it does not include annotation scopes, which have access to their
enclosing class scopes. This means that the following will fail:

```py
class A:
    a = 42
    b = list(a + i for i in range(10))
```

However, the following will succeed:

```py
class A:
    type Alias = Nested
    class Nested: pass

print(A.Alias.__value__)  # <type 'A.Nested'>
```

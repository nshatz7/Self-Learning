# The Big Picture: 4 Core Pillars

## 1. Importing & Namespaces (Section 1)
* **`import mod`**: Keeps `mod`'s namespace separate. You must qualify names (`mod.func()`).
* **`from mod import func`**: Pulls `func` directly into your local namespace. Watch out for name collisions—if you define your own `func` afterward, it silently shadows the imported one.
* **`from mod import *`**: Imports all public entities (anything not starting with an underscore `_`), which is discouraged in production because it pollutes your namespace.
* **Aliasing (`as`)**: Once you alias a module (`import math as m`), the original name (`math`) is no longer recognized in that scope.

## 2. Standard Library Modules (Section 2)
* **`math`**: Key exam functions include:
  * `ceil()`
  * `floor()`
  * `trunc()` *(drops decimals toward zero—different from `floor()` on negative numbers!)*
  * `hypot()`
  * `factorial()`
  * `radians()` / `degrees()`
* **`random`**: Know the boundary rules!
  * `randint(a, b)` is inclusive on both ends.
  * `randrange(start, stop, step)` excludes `stop`.
  * Also know `choice()` vs. `sample()` *(without replacement)*.
* **`platform`**: Queries the underlying hardware, OS, and Python implementation:
  * `platform()`
  * `machine()`
  * `processor()`
  * `system()`
  * `version()`
  * `python_implementation()`
  * `python_version_tuple()`

## 3. Custom Modules & Packages (Section 3)
* **`__name__`**: Equals `"__main__"` when a file is run directly, or the module's filename when imported.
* **`__pycache__` & `.pyc`**: Python compiles imported modules into bytecode inside `__pycache__` to speed up future imports.
* **`sys.path`**: The list of directories Python searches when importing (starting with the directory of the executed script). You can append custom paths or `.zip` archives to it.
* **Packages & `__init__.py`**: A directory containing modules becomes a package. `__init__.py` runs automatically when the package is first imported.

## 4. PIP & PyPI (Section 4)
Know the core CLI commands and what they output:
* `pip --version`
* `pip list`
* `pip show <package>` *(shows metadata and dependencies)*
* `pip search`
* `pip install` *(including `-U` to upgrade and `==` for specific versions)*
* `pip uninstall`

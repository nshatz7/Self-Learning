## The Highest-Yield Exam Traps (Cheat Sheet)

| Topic | The Trap on the Exam | What Actually Happens |
| :--- | :--- | :--- |
| `__init__` Return | A constructor has `return 1` or `return self`. | Raises `TypeError`. `__init__` can only return `None`. |
| `__name__` on Objects | `obj = MyClass(); print(obj.__name__)` | Raises `AttributeError`. Only classes have `__name__`, not instances (`type(obj).__name__` works). |
| `__bases__` on Objects | `print(obj.__bases__)` | Raises `AttributeError`. Only classes have `__bases__` (returns a tuple of direct parent class objects). |
| `hasattr()` Syntax | `hasattr(obj, prop)` (second arg not in quotes) | Raises `TypeError` (or `NameError`). The second argument must be a string: `hasattr(obj, 'prop')`. |
| MRO `TypeError` | `class B(A): pass` followed by `class C(A, B): pass` | Raises `TypeError` (inconsistent MRO). A subclass (`B`) must always be listed before its superclass (`A`) in `class C(B, A):`. |
| `.find()` vs `.index()` | Looking for a missing substring `'z'` in `'abc'`. | `.find('z')` returns `-1`. `.index('z')` raises `ValueError`. |
| `sorted()` vs `.sort()` | `s = "cba"; s.sort()` or `x = [3,1].sort()` | Strings have no `.sort()` (`AttributeError`). And `list.sort()` returns `None`, whereas `sorted(s)` returns a list `['a', 'b', 'c']`. |
| `randint` vs `randrange` | `randint(1, 3)` vs `randrange(1, 3)` | `randint(1, 3)` includes `3` (`1, 2, 3`). `randrange(1, 3)` excludes `3` (`1, 2`). |
| `random.sample()` | `sample([1, 2], 3)` | Raises `ValueError` because `k` (`3`) is larger than the population (`2`). I also need to remember `sample()` never repeats elements. |
| `timedelta` Attributes | `td = timedelta(weeks=1, hours=2)` -> `td.hours` | Raises `AttributeError`. `timedelta` only stores `.days`, `.seconds`, and `.microseconds` internally (`td.days == 7`, `td.seconds == 7200`). |
| `calendar.leapdays()` | `calendar.leapdays(2020, 2024)` | Returns `1`, not `2`! The end year (`2024`) is exclusive, just like `range()`. |

---

## Top Code Patterns I Must Be Able to Trace Cold

### Pattern A: OOP Variable Lookup, `__dict__`, and Name Mangling (Highest Weight)

I should expect 5–8 questions testing what resides in `obj.__dict__` vs `Class.__dict__` and how double underscores behave across inheritance:

```python
class A:
    var = 1               # Class variable -> lives in A.__dict__, NOT in obj.__dict__
    def __init__(self):
        self.x = 10       # Instance variable -> in obj.__dict__ as 'x'
        self.__y = 20     # Mangled instance variable -> in obj.__dict__ as '_A__y'

class B(A):
    var = 2
    def __init__(self):
        super().__init__() # If this line is missing, b.x and b._A__y DO NOT EXIST!
        self.__y = 30      # Stored as '_B__y' — does NOT overwrite '_A__y'!

b = B()
print(len(b.__dict__))     # Output: 3 -> {'x': 10, '_A__y': 20, '_B__y': 30}
```

* **Key Rule:** Class variables are never included in `instance.__dict__`.
* **Key Rule:** If a subclass defines `__init__` and does not explicitly call `super().__init__()` or `A.__init__(self)`, the parent constructor never runs and parent instance variables are never created.
* **Key Rule:** `issubclass(A, A)` is always `True` (every class is a subclass of itself). `isinstance(b, (A, B))` is `True`.

### Pattern B: Exception Hierarchy & `try-except-else-finally`

I will see questions where two `except` blocks match the same error, or where an exception is raised inside `except`:

```python
try:
    x = [1, 2][5]          # Raises IndexError
except LookupError:        # Parent of IndexError & KeyError!
    print("Lookup")        # THIS RUNS FIRST because it appears first
except IndexError:
    print("Index")         # Unreachable!
else:
    print("Else")          # Only runs if NO exception was raised in try
finally:
    print("Finally")       # ALWAYS runs, even if an uncaught error crashes the program
```

* **Must-Know Parent -> Child Pairs:**
  * `BaseException` -> `Exception`, `SystemExit`, `KeyboardInterrupt` *(Note: `except Exception:` will not catch `KeyboardInterrupt` or `SystemExit`!)*
  * `ArithmeticError` -> `ZeroDivisionError`, `OverflowError`
  * `LookupError` -> `IndexError`, `KeyError`
* **`e.args` Trap:** If an exception is raised as `raise Exception("a", "b")`, `len(e.args)` is `2`. If raised as `raise Exception()`, `len(e.args)` is `0` (`e.args` is `()`).

### Pattern C: Closures, Lambdas, and Generators

Every exam has 1–2 closure questions and 2–3 generator questions:

```python
# Closure pattern
def outer(par):
    def inner(loc):
        return par ** loc
    return inner

func = outer(2)
print(func(3))             # Output: 8 (par=2 is remembered, loc=3)

# Generator pattern
def gen(n):
    for i in range(n):
        yield i * 2

g = gen(3)
print(list(g))             # Output: [0, 2, 4]
print(list(g))             # Output: [] -> Generators can only be iterated ONCE!
```

* **Key Rule:** Once a generator or `map()` / `filter()` iterator is exhausted, iterating over it a second time yields nothing (`[]`), and calling `next(g)` on an exhausted generator raises `StopIteration`.

### Pattern D: ASCII Math & String Comparisons

I need to memorize these four ASCII code points so I never guess on `ord()` / `chr()` or string comparison questions:

* `' '` (Space) = `32`
* `'0'` (Zero) = `48` (so `'1'` is `49`, `'9'` is `57`)
* `'A'` = `65`
* `'a'` = `97` (Notice `'a' - 'A' == 32`)

* **Comparison Traps:**
  * `'10' < '2'` is `True` (compares first characters `'1'` (`49`) vs `'2'` (`50`)).
  * `'Alpha' < 'alpha'` is `True` (`'A'` (`65`) is less than `'a'` (`97`)).
  * `'10' == 10` is `False` (does not raise `TypeError` for `==` or `!=`), but `'10' < 10` raises `TypeError`!

---

## Quick-Fire Checklist

* **String `.split()` vs `.split(' ')`:**
  * `"a  b \n c".split()` (no args) groups all whitespace together -> `['a', 'b', 'c']`.
  * `"a  b".split(' ')` (explicit space) splits on every single space -> `['a', '', 'b']`.
  * `"".split()` returns `[]`, whereas `"".split(' ')` returns `['']`.
  * `"abc".split("")` (empty separator) raises `ValueError: empty separator`.

* **File Modes & `errno`:**
  * `'r'` raises `FileNotFoundError` (`errno.ENOENT`) if missing.
  * `'w'` wipes the file immediately upon opening.
  * `'x'` creates a new file and raises `FileExistsError` (`errno.EEXIST`) if it already exists.
  * `bytearray(10)` creates 10 zero-initialized bytes (`0` to `255` integer range only).

* **`datetime` Weekday Numbering:**
  * `d.weekday()` -> Monday is `0`, Sunday is `6`.
  * `d.isoweekday()` -> Monday is `1`, Sunday is `7`.
  * `strftime` (`f` = format object to string) vs `strptime` (`p` = parse string to object).

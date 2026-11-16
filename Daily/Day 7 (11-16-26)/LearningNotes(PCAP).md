# The Big Picture: 4 Core Pillars

---

## 1. Characters, Encodings & String Internals (Sections 1–2)

### ASCII vs. Unicode & UTF-8
* **ASCII:** A legacy character encoding standard covering **128 characters** (code points `0–127`), primarily English letters, digits, and basic punctuation.
* **Unicode:** A universal standard covering **over a million code points** to represent text across virtually all writing systems and symbols.
* **UTF-8:** The standard variable-width encoding for Unicode, using **1 to 4 bytes** per character (backward-compatible with ASCII for the first 128 characters).

### `ord()` and `chr()`
* **`ord(char)`:** Converts a single character into its integer Unicode code point.
  * *Example:* `ord('A')` returns `65`.
* **`chr(code_point)`:** Converts an integer Unicode code point back into its corresponding character.
  * *Example:* `chr(65)` returns `'A'`.

### Immutability
* **Read-Only Nature:** Python strings are immutable and cannot be modified in place.
* **Prohibited Operations:** Attempting in-place mutations—such as `del s[0]`, `s.append('x')`, or `s[0] = 'x'`—will raise a `TypeError` (or `AttributeError` for missing list methods).
* **Workaround:** To "modify" a string, you must construct a brand-new string using concatenation (`+`), slicing, or string methods.

### Sequence Operations
* **Supported Operations:** Because strings are sequences, standard operations like indexing (`s[0]`), slicing (`s[1:4]`), membership testing (`in` / `not in`), `index()`, and `list(s)` all work as expected.
* **`min()` and `max()` Gotcha:** These functions compare characters by their **Unicode code points**, not alphabetical order.
  * *Example:* Uppercase `'Z'` (`90`) is considered "less than" lowercase `'a'` (`97`).

---

## 2. String Methods (Section 3)

### Search & Inspection
* **`find()` vs. `index()`:** Both search for a substring and return its lowest starting index.
  * `find()` returns `-1` if the substring is not found.
  * `index()` raises a `ValueError` if the substring is not found.
* **Additional Inspection Methods:**
  * `rfind()`: Searches from the right (end of the string) and returns the highest index (or `-1`).
  * `startswith()` / `endswith()`: Return `True` or `False` based on prefix/suffix matches.
  * `count()`: Returns the number of non-overlapping occurrences of a substring.

### Character Classification
* **Core Methods:** `isalpha()`, `isdigit()`, `isalnum()`, `isspace()`, `islower()`, and `isupper()`.
* **Edge Case — Empty Strings:** Calling any of these methods on an empty string (`""`) always returns `False`.
* **Edge Case — Spaces & Punctuation:** Spaces count as non-alphanumeric characters.
  * *Example:* `"abc 123".isalnum()` evaluates to `False`.

### Transformation & Splitting
* **`join()`:** Called on the **separator** string, taking an iterable of strings as its argument.
  * *Example:* `",".join(["a", "b"])` returns `"a,b"`.
* **`split()`:** Breaks a string into a list of substrings, splitting on any whitespace by default (or a specified delimiter).
* **`strip()` / `lstrip()` / `rstrip()`:** Return a copy of the string with leading and/or trailing whitespace (or specified characters) removed.

---

## 3. String Comparisons & Sorting (Section 4)

### Lexicographical Comparison
* **Character-by-Character:** Python compares strings from left to right using Unicode code points rather than numerical or dictionary value.
  * *Example:* `'10' < '2'` evaluates to `True` because the first character `'1'` (`49`) has a lower code point than `'2'` (`50`).

### String vs. Number Comparisons
* **Equality (`==`, `!=`):** Safely evaluates to `False` and `True`, respectively, without raising an error (e.g., `'5' == 5` is `False`).
* **Ordering (`<`, `>`, `<=`, `>=`):** Attempting to order a string against a number raises a `TypeError`.

### `sorted()` vs. `.sort()`
* **`sorted(iterable)`:**
  * Returns a **new sorted list**, leaving the original iterable unchanged.
  * Works on any iterable, including strings (e.g., `sorted("cab")` returns `['a', 'b', 'c']`).
* **`list.sort()`:**
  * Mutates the list **in place** and returns `None`.
  * Only available on lists (cannot be called directly on strings).

---

## 4. Exceptions & Handling (Sections 5–8)

### `try` / `except` Ordering
* **Top-to-Bottom Evaluation:** Python checks `except` branches sequentially from top to bottom and executes only the first matching handler.
* **Specificity Rule:** Always place **more specific subclasses before general parent classes**.
  * *Example:* Place `ZeroDivisionError` before `ArithmeticError`, and keep `Exception` (or a bare `except:`) at the very bottom.

### The Core Exception Hierarchy
Understanding parent-child relationships is crucial for proper `except` ordering:

```text
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    └── OverflowError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── ValueError
      ├── TypeError
      └── AssertionError
```

### `assert` Statements
* **Behavior:** `assert expression` evaluates the given expression for truthiness.
* **Failure Condition:** If the expression evaluates to a **falsy** value (`False`, `0`, `""`, `None`, empty collections), Python immediately raises an `AssertionError`.
* **Use Case:** Primarily used as a debugging and sanity-check tool during development rather than for handling expected runtime errors.

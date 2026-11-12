Python Learning Notes (11-10-26): PCAP 
==============================================================

Table of Contents
-----------------
1. Character Encoding Standards
2. Nature of Strings in Python
3. Essential String Methods
4. Exceptions & Error Handling

---

1. Character Encoding Standards
-------------------------------

Encoding translates abstract text characters into raw bytes for storage and network transfer.

| Standard | Bit Width | Character Range / Description | Notable Code Points |
| :--- | :--- | :--- | :--- |
| **ASCII** | 7-bit (or 8-bit extended) | Standard: `0` to `127` (128 total)<br>Extended: `0` to `255` (256 total) | Space = `32`<br>`'A'` = `65`<br>`'a'` = `97`<br>`'0'` = `48` |
| **Unicode & UCS-4** | Fixed / Abstract | Global standard mapping 1,000,000+ unique characters. UCS-4 uses fixed 4-byte representations. | Covers all modern alphabets, historic scripts, and symbols. |
| **UTF-8** | Variable (1 to 4 bytes) | Dynamic-width encoding. Fully backwards-compatible with ASCII (uses 1 byte for ASCII chars). | Default string encoding across modern systems and Python 3 source files. |

> **Correction Note:** UTF-8 uses **1 to 4 bytes** (8 to 32 bits) per character, not bits.

### Code Point Conversion Functions

```python
"""ord(char) returns the integer Unicode code point (len must be 1)"""
ord('A')        """returns 65"""
ord('a')        """returns 97"""

"""chr(int_code) returns string character for the given code point"""
chr(65)         """returns 'A'"""
chr(97)         """returns 'a'"""

"""Exceptions triggered on invalid inputs"""
ord("ab")       """TypeError: ord() expected a character, but string of length 2 found"""
chr(1_114_112)  """ValueError: chr() arg not in range(0x110000)"""
```

---

2. Nature of Strings in Python
------------------------------

Strings (`str`) are **immutable sequences** of Unicode characters.

### Sequence Operations

Strings support standard sequence behaviors without altering underlying data:

* **Indexing & Slicing:** `s[0]`, `s[1:4]`, `s[::-1]`
* **Concatenation & Replication:** `s1 + s2`, `s * 3`
* **Membership:** `'sub' in s`, `'xyz' not in s`
* **Aggregations:** `len(s)`, `min(s)`, `max(s)`

### Sorting: `sorted()` vs `.sort()`

```python
"""sorted(iterable): Built-in function; returns a NEW sorted list"""
s = "python"
result = sorted(s)
print(result)   """['h', 'n', 'o', 'p', 't', 'y']"""
print(s)        """'python' (original string remains unchanged)"""

"""list.sort(): In-place list mutation; returns None"""
lst = ['b', 'a', 'c']
lst.sort()      """mutates lst to ['a', 'b', 'c'] in place and returns None"""

"""Note: strings do NOT have a .sort() method because they are immutable:"""
"""s.sort() -> AttributeError: 'str' object has no attribute 'sort'"""
```

### Lexicographical Comparison

Comparisons are evaluated **character-by-character** by comparing their Unicode numeric code points (`ord()` value).

```python
"""Uppercase letters have lower code points than lowercase letters:"""
ord('A') < ord('a')   """65 < 97 evaluates to True"""
"Apple" < "apple"     """True because 'A' < 'a'"""
"Zoo" < "apple"       """True because 'Z' (90) < 'a' (97)"""
```

---

3. Essential String Methods
---------------------------

> **Important:** Because strings are **immutable**, methods never mutate in-place; they always return a **newly allocated string object**.

### Case Transformation

```python
text = "hello WORLD"

text.capitalize()  """'Hello world'  (First char uppercase, rest lowercase)"""
text.title()       """'Hello World'  (Capitalizes every word boundary)"""
text.upper()       """'HELLO WORLD'"""
text.lower()       """'hello world'"""
text.swapcase()    """'HELLO world'"""
```

### Searching & Counting

| Method | Behavior on Match | Behavior if Not Found | Safe / Non-throwing |
| :--- | :--- | :--- | :--- |
| `.find(sub[, start[, end]])` | Lowest index of `sub` | Returns `-1` | Yes |
| `.rfind(sub[, start[, end]])` | Highest index of `sub` | Returns `-1` | Yes |
| `.index(sub[, start[, end]])` | Lowest index of `sub` | Raises `ValueError` | No |
| `.rindex(sub[, start[, end]])`| Highest index of `sub` | Raises `ValueError` | No |
| `.count(sub)` | Integer count of non-overlapping matches | Returns `0` | Yes |

### Inspection Predicates

Return a boolean (`True`/`False`). All return `False` on empty strings `""`.

| Predicate | Evaluates `True` If |
| :--- | :--- |
| `.isalnum()` | All characters are alphanumeric (letters or numbers) |
| `.isalpha()` | All characters are alphabetic |
| `.isdigit()` | All characters are numeric digits |
| `.islower()` | Contains at least one cased character, and all are lowercase |
| `.isupper()` | Contains at least one cased character, and all are uppercase |
| `.isspace()` | All characters are whitespace (`' '`, `\t`, `\n`, `\r`, `\v`, `\f`) |

### Splitting, Joining, Stripping & Replacing

```python
"""1. 'sep'.join(iterable)"""
"""Joins elements; raises TypeError if any item is not a string"""
"-".join(["2026", "11", "04"])          """returns '2026-11-04'"""

"""2. .split(sep=None)"""
"""None splits by runs of consecutive whitespace and strips leading/trailing spaces"""
"  apple   orange \n banana  ".split()  """returns ['apple', 'orange', 'banana']"""
"a,b,c".split(",")                      """returns ['a', 'b', 'c']"""

"""3. .strip(), .lstrip(), .rstrip()"""
"""Strips characters (defaults to whitespace) from boundaries"""
"  hello  ".strip()                    """returns 'hello'"""
"***hello***".lstrip("*")               """returns 'hello***'"""

"""4. .replace(old, new[, count])"""
"banana".replace("a", "o", 2)          """returns 'bonona'"""
```

---

4. Exceptions & Error Handling
------------------------------

### Try-Except-Else-Finally Flow

```python
try:
    """1. Monitored block: code that might raise an exception"""
    value = int(user_input)
    result = 10 / value

except ValueError as e:
    """2. Handled if a ValueError occurs"""
    print(f"Invalid integer: {e}")

except ZeroDivisionError as e:
    """Evaluated top-to-bottom. Most specific child exceptions must go first!"""
    print(f"Cannot divide by zero: {e}")

except Exception as e:
    """Generic catch-all for other programmatic errors"""
    print(f"Unexpected error: {e}")

else:
    """3. Executes ONLY if no exceptions were raised inside the try block"""
    print(f"Operation succeeded: {result}")

finally:
    """4. ALWAYS executes regardless of success, caught, or uncaught errors"""
    print("Execution complete.")
```

> **Warning:** Placing a bare `except:` anywhere other than the very end of the `except` blocks will raise a `SyntaxError`.

### Core Exception Hierarchy

```text
BaseException
 │
 ├── SystemExit                  (Raised by sys.exit)
 ├── KeyboardInterrupt           (Triggered by Ctrl+C)
 └── Exception                   (Root for non-system-exiting exceptions)
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    └── OverflowError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── ValueError
      ├── TypeError
      ├── AssertionError         (Raised when assert statement fails)
      └── ImportError
           └── ModuleNotFoundError
```

### Raising Exceptions & Assertions

```python
"""Explicit raise"""
raise ValueError("Invalid parameter provided")

"""Re-raising inside an except block (preserves traceback)"""
try:
    process_data()
except KeyError:
    log_failure()
    raise  """Re-raises active KeyError"""

"""Assertions"""
"""Syntax: assert <condition>, [optional message]"""
"""Raises AssertionError when condition is Falsy"""
assert x > 0, "x must be positive"
```

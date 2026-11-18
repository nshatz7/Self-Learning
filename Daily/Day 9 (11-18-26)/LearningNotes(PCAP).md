# PE2 (Module 4) - The Big Picture: 3 Core Pillars

## 1. Generators, Iterators, Lambdas & Closures (Section 1)

* **Iterator Protocol:** Any iterable object must implement `__iter__()` (which returns the iterator object itself) and `__next__()` (which returns the next value and raises `StopIteration` when exhausted).
* **`yield` & Generators:** Replacing `return` with `yield` turns a function into a generator function. Calling it does not execute the body immediately—it returns a generator object that pauses and resumes state on each `next()` call.
* **List Comprehensions vs. Generator Expressions:** 
  * `[x for x in range(5)]` builds the entire list in memory immediately.
  * `(x for x in range(5))` creates a lazy generator object that computes items on demand (and can only be iterated through once).
* **`lambda`, `map()`, and `filter()`:**
  * `lambda params: expression` creates an anonymous single-expression function.
  * `map(func, iterable)` applies `func` to every element and returns an iterator (not a list—wrap in `list()` to materialize it).
  * `filter(func, iterable)` yields elements where `func(item)` evaluates to truthy.
* **Closures:** An inner function that remembers and accesses variables from its enclosing function's scope even after the outer function has finished executing.

---

## 2. File Streams & I/O Operations (Sections 2–3)

* **Opening Streams & Modes:** `open(file, mode='r', encoding=None)`. Know the text vs. binary modes:
  * `'r'`: Read (default)
  * `'w'`: Write (truncates/overwrites)
  * `'a'`: Append
  * `'r+'`: Read + write without truncating
  * Append `'b'` (e.g., `'rb'`, `'wb'`) for binary streams.
* **Pre-opened Standard Streams (`sys`):** `sys.stdin` (keyboard), `sys.stdout` (screen), and `sys.stderr` (error output)—already open, no `open()` needed.
* **Reading Methods:**
  * `read(size)`: Reads up to `size` characters/bytes (or the whole file if omitted) and returns `""` (or `b""`) at EOF.
  * `readline()`: Reads a single line including the trailing `\n`.
  * `readlines()`: Returns a list of all lines; iterating directly over the stream (`for line in f:`) is memory-efficient and steps line-by-line.
* **Binary `bytearray`:** Mutable sequence of integers in range `0` to `255` (`bytearray(10)` initializes 10 zeroed bytes). Used with `stream.readinto(buf)` and `stream.write(buf)`.
* **`errno` & `strerror()`:** File I/O failures raise `OSError` / `IOError`. You can inspect `e.errno` against `errno` constants (e.g., `errno.ENOENT` for missing file, `errno.EACCES` for permission denied) or pass `e.errno` to `os.strerror()`.

---

## 3. OS, Datetime & Calendar Modules (Sections 4–6)

### `os` Module
* **System Info:** `os.uname()` (Unix/macOS—attributes `systemname`, `nodename`, `release`, `version`, `machine`) vs. `os.name` (`'posix'`, `'nt'`, `'java'`).
* **Directory & System Operations:**
  * `os.mkdir("dir")`: Single directory creation (fails if parent is missing or dir exists).
  * `os.makedirs("a/b/c")`: Recursive directory creation.
  * `os.getcwd()`, `os.chdir()`, `os.listdir()`, `os.rmdir()`, `os.removedirs()`
  * `os.system("cmd")`: Executes a shell command and returns the exit status.

### `datetime` & `time` Modules
* **Constructors:** `date(year, month, day)`, `time(hour, minute, second)`, and `datetime(year, month, day, ...)`.
* **Current Time:** `date.today()` vs. `datetime.now()` / `datetime.utcnow()`.
* **Formatting & Parsing:** 
  * `strftime("%Y-%m-%d")` formats a `date`/`datetime` object into a string.
  * `strptime(str, fmt)` parses a string into a `datetime` object.
* **`timedelta`:** Subtracting two `date` or `datetime` objects produces a `timedelta` object (which stores `.days`, `.seconds`, `.microseconds`—note there is no `.hours` or `.years` attribute!).

### `calendar` Module
* **Week Indexing:** Weeks start on Monday (`0`) through Sunday (`6`) (`calendar.MONDAY == 0`).
* **Key Functions:** 
  * `calendar.calendar(year)` / `prcal(year)`
  * `calendar.month(year, month)` / `prmonth()`
  * `calendar.weekday(y, m, d)`
  * `calendar.weekheader(n)`
  * `calendar.isleap(year)`
  * `calendar.leapdays(y1, y2)` (half-open range `[y1, y2)`, excluding `y2`).

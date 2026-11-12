# Operating System & Time Modules (`os`, `datetime`, `time`, `calendar`)

## `os` Module
* **`os.uname()`** — returns system info attributes (`sysname`, `nodename`, `release`, `version`, `machine`) on POSIX/macOS systems; `os.name` returns `'posix'` (macOS/Linux) or `'nt'` (Windows).
* **Directory operations:** 
  * `os.mkdir('dir')`
  * `os.makedirs('a/b/c')` (recursive)
  * `os.listdir(path='.')` (returns list of filenames, excluding `.` and `..`)
  * `os.chdir('path')`
  * `os.getcwd()`
  * `os.rmdir('dir')`
  * `os.removedirs('a/b/c')`
* **`os.system('command')`** — executes a shell command and returns the exit status code (`0` typically indicates success).

---

## `datetime` & `time` Modules
* **`date(year, month, day)`:** 
  * `.today()`
  * `.fromisoformat('YYYY-MM-DD')`
  * `.fromtimestamp(ts)`
  * `.replace(...)`
  * `.weekday()` (Monday is `0`, Sunday is `6`)
  * `.isoweekday()` (Monday is `1`, Sunday is `7`)
* **`time(hour, minute, second, microsecond)` & `datetime(...)`:** 
  * `datetime.now()`
  * `datetime.today()`
  * `datetime.utcnow()`
* **Formatting & Parsing:**
  * **`.strftime(format_str)`** — converts a `date`/`time`/`datetime` object into a formatted string:
    * `%Y`: 4-digit year
    * `%y`: 2-digit year
    * `%m`: month
    * `%d`: day
    * `%H`: 24-hr
    * `%I`: 12-hr
    * `%M`: minute
    * `%S`: second
    * `%B`: full month name
    * `%A`: full weekday name
  * **`datetime.strptime(date_str, format_str)`** — parses a string into a `datetime` object.
* **`timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)`:** 
  * Resulting object when subtracting two `date` or `datetime` objects. Internally stores only `days`, `seconds`, and `microseconds` attributes!
* **`time` module functions:** 
  * `time.time()` (epoch float seconds)
  * `time.sleep(secs)`
  * `time.ctime(ts)` (human-readable string)
  * `time.gmtime(ts)` / `time.localtime(ts)` (`struct_time` objects)

---

## `calendar` Module
* **Days of the week constants:** `calendar.MONDAY` (`0`) through `calendar.SUNDAY` (`6`).
* **`calendar.calendar(year)` / `calendar.prcal(year)`** — returns / prints full year calendar string.
* **`calendar.month(year, month)` / `calendar.prmonth(year, month)`** — returns / prints single month string.
* **`calendar.setfirstweekday(day)`** — changes the first column of displayed calendars.
* **`calendar.weekday(year, month, day)`** — returns day of week (`0`–`6`) for a given date.
* **`calendar.weekheader(n)`** — returns string of weekday abbreviations truncated to width `n` (e.g., `n=2` $\rightarrow$ `'Mo Tu We Th Fr Sa Su'`).
* **`calendar.isleap(year)`** — returns `True` if leap year; **`calendar.leapdays(y1, y2)`** — counts leap years in range $[y1, y2)$ (excludes `y2`!).
* **`calendar.Calendar` class:** 
  * `.iterweekdays()`
  * `.itermonthdates(y, m)`
  * `.itermonthdays(y, m)` (pads out-of-month days in the week with `0`)
  * `.monthdays2calendar(y, m)` (list of week lists containing `(day_number, weekday_number)` tuples)

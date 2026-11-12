## Classes, Objects, and Properties

* **Constructor (`__init__`)**: Initializes an instance's state upon creation.
  * **PCAP Rule**: `__init__` cannot return a value; it must implicitly return `None` (returning anything else raises `TypeError`).
* **Instance Variables**: Attached to `self` (`self.val = 1`). Each object gets its own independent copy. Python allows adding or deleting (`del obj.val`) instance attributes dynamically outside the class definition.
* **Class Variables**: Defined directly inside the class body outside any method. Shared across all instances of the class (accessible even before any instance is created).
* **Name Mangling (Encapsulation)**: Prefixing an attribute or method with two leading underscores (`__secret`) without trailing underscores triggers name mangling. Python internally renames it to `_ClassName__secret`. It remains accessible externally via `obj._ClassName__secret`.
* **Introspection (`__dict__` and `hasattr`)**:
  * `obj.__dict__`: dictionary containing only that specific instance's variables.
  * `ClassName.__dict__`: dictionary containing class variables, methods, and metadata.
  * `hasattr(obj_or_class, 'attr_name')`: checks safely if an attribute exists (the second argument must be a string, or it raises `TypeError`).

---

## Methods & Reflection

* **`self` Parameter**: The first parameter of every standard instance method, referencing the calling object. Passed implicitly via `obj.method()`, or explicitly via `ClassName.method(obj)`.
* **Dunder / Magic Methods**:
  * `__str__(self)`: invoked by `print(obj)` and `str(obj)`. Must return a `str`. If omitted, Python falls back to `<__main__.ClassName object at 0x...>`.
* **Class & Instance Relationships**:
  * `__name__`: attribute of a class only (accessing `obj.__name__` raises `AttributeError`; use `type(obj).__name__` instead).
  * `__module__`: exists on both classes and instances; stores the name of the module where the class was defined (`"__main__"` if defined in the executing script).
  * `__bases__`: attribute of a class only; returns a tuple of direct superclasses as class objects, not string names.
  * `issubclass(SubClass, SuperClass)`: returns `True` if `SubClass` inherits from `SuperClass` (every class is considered a subclass of itself: `issubclass(A, A) == True`).
  * `isinstance(obj, ClassOrTuple)`: returns `True` if `obj` is an instance of the class or any of its superclasses.
  * `obj1 is obj2`: identity operator; checks whether two variables point to the exact same memory address (`A() is A()` evaluates to `False`).

---

## Inheritance, Polymorphism & MRO

* **`super()` vs. Explicit Superclass Calls**:
  * `super().__init__()`: invokes the superclass method automatically without passing `self`.
  * `SuperClass.__init__(self)`: calls the superclass method explicitly and requires passing `self`.
* **Inheritance Behavior**: Subclasses inherit all methods, class variables, and instance variables initialized by the parent's `__init__` (provided the child does not override `__init__` without invoking `super().__init__()`). If both define the same variable or method, the child overrides the parent.
* **Method Resolution Order (MRO)**: Dictates how Python resolves methods in multiple inheritance (`class C(A, B):`).
  * Uses the **C3 Linearization** algorithm: searches bottom-to-top (child before parent) and left-to-right (the order base classes appear in the class definition).
  * **MRO Violation (`TypeError`)**: Defining `class C(A, B)` when `B` inherits from `A` (`class B(A)`) raises `TypeError: Cannot create a consistent method resolution order (MRO)` because superclass `A` cannot precede its own subclass `B`.

---

## Exceptions as Objects

* **`e.args` Attribute**: Every exception instance carries an `args` attribute: a tuple containing all arguments passed to the exception's constructor when raised. If raised without arguments (`raise Exception()`), `e.args` is an empty tuple `()`.
* **Custom Exceptions**: Created by subclassing built-in exceptions (typically `Exception` or a domain-specific subclass). Overriding `__init__` in a custom exception should call `super().__init__(*args)` to preserve standard `e.args` behavior.

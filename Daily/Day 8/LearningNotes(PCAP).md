# PE2 - Module 3: The Big Picture: 4 Core Pillars 

---

## 1. Procedural vs. Object-Oriented Foundations (Section 1)

* **Procedural vs. OOP:** Procedural programming separates data and functions; OOP bundles data (properties/attributes) and behavior (methods) into **classes** (blueprints) and **objects** (instances).
* **The Stack Example:** PE2 uses a stack (`push` / `pop`) to demonstrate why encapsulation matters—without hiding the internal list, external code can directly corrupt the stack state.
* **Encapsulation & Name Mangling:** Prefixing an attribute or method with two underscores (`__val`) triggers name mangling—Python internally renames it to `_ClassName__val`. 
  * It is **not** truly private: accessing `obj._ClassName__val` still works, whereas `obj.__val` raises an `AttributeError`.

---

## 2. Properties: Instance vs. Class Variables (Section 2)

* **Instance Variables:** Created inside methods via `self.x = 1` (usually in `__init__`). Each object gets its own independent copy, stored in `obj.__dict__`.
* **Class Variables:** Defined inside the class body outside of any methods. Shared across all instances and stored in `ClassName.__dict__` (not in `obj.__dict__`).
* **The Shadowing Trap:** Reading `obj.class_var` falls back to `ClassName.class_var` if the instance doesn't have its own copy. However, assigning `obj.class_var = 99` creates a new instance variable on `obj` that *shadows* the class variable without modifying it for other instances.
* **`hasattr()`:** `hasattr(obj_or_class, 'attr_name')` safely checks whether an attribute exists, returning `True` or `False`. *(Remember: the second argument must be a string).*

---

## 3. Methods & Introspection (Section 3)

* **`self` Parameter:** Every instance method must declare `self` as its first parameter, though you do not pass it explicitly when calling `obj.method()`.
* **`__init__` Constructor:** Runs automatically upon instantiation. It cannot return anything other than `None` (returning a value raises a `TypeError`).
* **Reflection / Introspection:** Know the built-in attributes:
  * `__dict__`: Dictionary of an object's or class's writable attributes.
  * `__name__`: String name of a class *(exists only on classes, not on instances—`obj.__name__` raises `AttributeError`)*.
  * `__module__`: Name of the module where the class was defined (`"__main__"` if run directly).
  * `__bases__`: Tuple containing the direct superclasses of a class *(also exists only on classes, not instances)*.

---

## 4. Inheritance, Polymorphism & Custom Exceptions (Sections 4–6)

* **`issubclass(Sub, Super)` & `isinstance(obj, Class)`:** Every class is considered a subclass of itself (`issubclass(A, A)` evaluates to `True`).
* **Attribute Lookup Order:** Python searches in the following order:
  $$\text{instance.\_\_dict\_\_} \rightarrow \text{Class.\_\_dict\_\_} \rightarrow \text{Superclass.\_\_dict\_\_}$$
  *(Resolved left-to-right in multiple inheritance).*
* **MRO (Method Resolution Order):** Python uses **C3 linearization** to resolve diamond inheritance. Having a superclass appear before its subclass in an inheritance list (e.g., `class C(A, B):` where `B` inherits from `A`) raises:
  ```text
  TypeError: Cannot create a consistent method resolution order
  ```
* **`super()`:** Invokes methods or `__init__` from the superclass without hardcoding the parent class name (e.g., `super().__init__()`).
* **`__str__()`:** Overriding `__str__(self)` controls what `print(obj)` and `str(obj)` output *(must return a string)*.
* **Custom Exceptions:** Created by subclassing `Exception` (or a narrower built-in exception), allowing you to pass custom arguments via `self.args` or attach custom attributes.

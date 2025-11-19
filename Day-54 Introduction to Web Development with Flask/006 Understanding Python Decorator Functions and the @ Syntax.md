### **Lecture Learnings**

1.  **Python Decorator:** A function that **wraps another function** to modify or extend its behavior **without permanently modifying it**. It's a function that takes a function and returns a function (usually with added functionality).

2.  **Structure of a Decorator:**
    *   Define a decorator function that takes a function (`func`) as an argument.
    *   Inside, define a **wrapper function** that:
        *   Contains code to run **before** the original function.
        *   Calls the original function (`func()`).
        *   Contains code to run **after** the original function.
    *   The decorator function **returns the wrapper function** (without parentheses).

3.  **Applying a Decorator (`@` Syntax):** Place `@decorator_name` on the line directly above the function you want to decorate. This is **syntactic sugar** for:
    `decorated_function = decorator_name(original_function)`

4.  **Use Case:** Decorators are perfect for adding **cross-cutting concerns** (like logging, timing, access control, delays) to multiple functions without repeating code.

---

### **Notebook Notes**

*   **Decorator:** A function that modifies/enhances another function.
*   **Syntax:**
    ```python
    def my_decorator(func):
        def wrapper():
            # Do something BEFORE
            func()
            # Do something AFTER
        return wrapper

    @my_decorator
    def say_hello():
        print("Hello")
    ```
*   **`@` is syntactic sugar** for:
    `say_hello = my_decorator(say_hello)`

---

### **Interview Points**

1.  **Q: What is a Python decorator and how does it work?**
    *   **A:** A decorator is a **higher-order function** that takes a function as input, adds some functionality (by defining an inner wrapper function), and returns the modified function. The `@decorator` syntax provides a clean way to apply this transformation.

2.  **Q: Explain the concept of "syntactic sugar" in the context of decorators.**
    *   **A:** The `@decorator` syntax is syntactic sugar. It is a cleaner, more readable alternative to the equivalent operation `original_function = decorator(original_function)`. Both methods achieve the same result, but the `@` syntax is preferred for its clarity.

3.  **Q: What is a common practical use case for a decorator?**
    *   **A:** A very common use case is **logging execution time**. A `@timer` decorator can be applied to any function to automatically measure and print how long it takes to run, which is invaluable for performance profiling without cluttering the core function's logic.

---

### **Updates/Corrections**

The lecture content is excellent and perfectly explains the core concept. There are no mistakes. The example of adding a `time.sleep()` delay is a clear and valid illustration, though in real-world applications, decorators are more commonly used for logging, authentication, timing, and caching.
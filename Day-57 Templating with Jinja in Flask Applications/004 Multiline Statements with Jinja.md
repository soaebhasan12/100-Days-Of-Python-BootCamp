### **Lecture Breakdown: Multiline Statements with Jinja**

**Learning Objectives:**
*   Understand the difference between Jinja expressions (`{{ }}`) and statements (`{% %}`).
*   Learn how to use control flow statements (like `for` loops and `if` conditions) inside HTML templates.
*   Integrate data from an external JSON API into a Flask app and display it dynamically.
*   Use the `{% for ... %} ... {% endfor %}` and `{% if ... %} ... {% endif %}` syntax.

**Explanation for Beginners:**

1.  **Two Types of Jinja Syntax:**
    *   **`{{ expression }}`:** Used for **output**. Anything inside is a Python expression that is evaluated, and the *result* is inserted into the HTML. (e.g., `{{ name }}`, `{{ 5*6 }}`).
    *   **`{% statement %}`:** Used for **logic and control flow**. This is for Python statements that don't output a value directly but control *how* the template is rendered (e.g., `for`, `if`, `endif`, `endfor`). These tags come in pairs to mark the beginning and end of a logic block.

2.  **The `for` Loop in Jinja:** The most common use case is to loop through a list of items (like blog posts from an API) and generate HTML for each one.
    *   **Structure:**
        ```jinja
        {% for item in list_of_items %}
            <!-- HTML to repeat for each item -->
            <h1>{{ item.title }}</h1>
        {% endfor %}
        ```
    *   You **must** close the loop with `{% endfor %}`. Jinja needs this to know where the repeating block of HTML ends.

3.  **The `if` Statement in Jinja:** Used to conditionally render parts of the template.
    *   **Structure:**
        ```jinja
        {% if condition %}
            <!-- HTML to show if condition is True -->
        {% endif %}
        ```
    *   You **must** close the conditional with `{% endif %}`.

4.  **The Power of Combining Server and Template:** The server's job (`server.py`) is to fetch and prepare the data (e.g., getting JSON from an API). The template's job (`blog.html`) is to focus on *displaying* that data beautifully, using Jinja's loops and conditionals to handle the logic of presentation.

**Notes for Notebook:**
*   **Output/Expression:** `{{ python_expression }}`
*   **Logic/Statement:** `{% python_statement %}`
*   **For Loop:**
    ```jinja
    {% for item in list %}
        {{ item.property }}
    {% endfor %}
    ```
*   **If Statement:**
    ```jinja
    {% if condition %}
        <!-- HTML -->
    {% endif %}
    ```
*   **Data Flow:** `External API -> Flask Route (gets JSON) -> render_template() -> Jinja Template (loops through data) -> Final HTML`

**Key Interview Points:**
*   **Q: What is the difference between `{{ }}` and `{% %}` in Jinja?**
    *   **A:** `{{ }}` is used for expressions that are evaluated and outputted into the final HTML. `{% %}` is used for statements that control the template's logic, such as loops and conditionals, which do not output content directly but define blocks of HTML to be rendered based on certain conditions.
*   **Q: Why is it a good practice to use loops in templates instead of in the Flask route?**
    *   **A:** It adheres to the principle of **Separation of Concerns**. The Flask route should handle data fetching, processing, and business logic. The template should handle presentation logic. Keeping the loop in the template makes the Python code cleaner and puts the decision of *how* to display the list of items in the same file (HTML) where the display is defined.
*   **Q: How do you end a `for` loop or an `if` block in Jinja?**
    *   **A:** You use the specific closing tags `{% endfor %}` and `{% endif %}`. Unlike Python, which uses indentation, Jinja requires these explicit closing tags to define the scope of the loop or conditional block within the HTML.

**Common Mistakes & Updates:**
*   **Mistake:** Forgetting the closing tag (`{% endfor %}` or `{% endif %}`). This will cause a template syntax error.
*   **Mistake:** Using `{{ }}` for statements like `{% for ... %}`.
*   **Mistake:** Trying to do complex data processing or calculations inside the template. The template is for presentation; complex logic should be done in the Flask route before passing the data to `render_template()`.
*   **Update/Clarification:** The service used in the lecture is called "JSONBin" (or a similar mock API service). These are great for learning and prototyping. In a real-world application, this data would typically come from your own database. The concept of fetching data and looping over it in the template remains exactly the same.
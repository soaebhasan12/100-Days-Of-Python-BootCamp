### Lecture Learnings (Explained for Beginners)

This lecture dives into the practical steps of serving full HTML pages with Flask, moving beyond simple strings.

1.  **Basic Flask Server Setup:** A recap of creating a minimal Flask application:
    *   Import the `Flask` class.
    *   Create an instance: `app = Flask(__name__)`
    *   Use the `@app.route('/')` **decorator** to define what happens when a user visits the root URL (`/`).
    *   The function under the decorator returns the content to be shown in the browser.
    *   `app.run(debug=True)` starts the server. `debug=True` enables auto-reloading on code changes and better error messages (only for development).

2.  **Rendering HTML Files:** The key concept is to move from returning HTML as a string inside your Python code (`return "<h1>Hello</h1>"`) to returning a dedicated HTML file. This is cleaner and more manageable.

3.  **The `render_template()` Function:** This is a crucial Flask function used to generate output from a template file. You import it: `from flask import Flask, render_template`.

4.  **The `templates` Folder:** Flask enforces a specific project structure for organization. All HTML template files **must** be placed inside a folder named **`templates`** at the root of your project. This is a non-negotiable convention; Flask will only look for HTML files in this specific folder by default.

5.  **File Paths in `render_template()`:** When calling `render_template('index.html')`, you only need to provide the filename if it's directly inside the `templates` folder. If you organize templates into subfolders (e.g., `templates/cv/angela.html`), you must provide the relative path: `render_template('cv/angela.html')`.

6.  **The Problem with External Assets:** The lecture ends by identifying a key issue: while the HTML file renders, linked external files (like images, CSS) are broken. This is because the browser can't find them. This perfectly sets up the need for the next topic: handling **static files**.

---

### Notebook Notes (Minimal & To-The-Point)

*   **To Render an HTML File:**
    1.  Create a `templates` folder in your project root.
    2.  Put all `.html` files inside this folder.
    3.  Import `render_template` from `flask`.
    4.  In your route function, return `render_template('filename.html')`.
    5.  Use subfolders inside `templates` for organization (e.g., `blog/post1.html`).
*   **`app.run(debug=True)`** enables auto-reload and debug mode. **Never use in production.**
*   **Current Issue:** Images/CSS from external websites work, but local files are broken. We need to handle **static files**.

---

### Interview Points

*   **Q: Why do we use `render_template()` instead of just returning HTML strings?**
    *   **A:** Separating presentation (HTML) from logic (Python) is a core principle of good software design (Separation of Concerns). It makes code more readable, maintainable, and allows designers and developers to work more independently. It also allows for the use of Flask's powerful **Jinja2 templating engine** later for dynamic content.

*   **Q: What is the purpose of the `templates` folder?**
    *   **A:** The `templates` folder is a convention enforced by Flask's default configuration. It provides a predictable and standardized location for the framework to find template files, keeping the project organized and making the application's structure clear to other developers.

*   **Q: What does the `debug=True` parameter do in `app.run()`?**
    *   **A:** It enables Flask's debugger and reloader. The **debugger** provides interactive error pages when an exception occurs, which is invaluable for development. The **reloader** automatically restarts the server whenever it detects a change in your source code, so you don't have to stop and start it manually after every edit.

*   **Q: The image on my rendered HTML page is broken. What is the most likely cause?**
    *   **A:** The most likely cause is that the image is a **local static file** (e.g., `src="my_photo.jpg"`), but you haven't placed it in the correct directory or used the correct URL to serve it. Flask requires static files to be placed in a `static` folder and referenced using the `{{ url_for('static', ...) }}` function, which we'll learn next.

---

### Updates & Corrections

*   **File Extension `.htm` vs `.html`:** The lecture mentions that some servers don't accept four-letter extensions, making `.htm` necessary. This is **largely outdated**. Modern web servers and operating systems have no issue with `.html`. It is now a best practice to consistently use the `.html` extension for clarity and standardization. The advice to rename `.htm` to `.html` is correct.
*   **Downloading HTML from GitHub:** The method described (right-click -> save as on a GitHub page) will not save the actual source code. It will save the *rendered* GitHub page HTML, which is not what you want. The correct way is to:
    1.  Navigate to your repository on GitHub.com.
    2.  Find the actual HTML file (e.g., `index.html`).
    3.  Click on it to view its content.
    4.  Click the "Raw" button to see the pure HTML file.
    5.  *Then* right-click and "Save As..." to download it correctly. A better method is to clone the entire repository using Git.
# -*- coding: utf-8 -*-
"""Curriculum content for the "Odoo Technical Training SDTek" course.

Pure data module consumed by the post_init_hook in __init__.py.
Edit the curriculum here directly; the hook syncs it to the database.
"""

CHANNEL_DESCRIPTION_SHORT = "Joint venture between ProspireNext and SDTEK. 16 classes + capstone, ~38 hours: Python, SQL & PostgreSQL, FastAPI integration and full Odoo 18 module development."

CHANNEL_DESCRIPTION = "<div class=\"prospire-course-intro\">\n  <p><strong>SDTEKH — Odoo Technical Training</strong> is a joint venture between <strong>ProspireNext</strong> and <strong>SDTEK</strong>. It takes you from zero Python to shipping production-grade Odoo 18 custom modules and FastAPI integrations.</p>\n  <p>The program runs <strong>16 classes plus a capstone project</strong> — about <strong>38 hours</strong> of guided, exercise-driven lessons covering Python fundamentals, SQL &amp; PostgreSQL, FastAPI integration and full Odoo 18 module development.</p>\n  <h3>Who this course is for</h3>\n  <ul>\n    <li>Beginner developers who want a structured path into Python and Odoo development.</li>\n    <li>Working developers (PHP, Java, .NET, JavaScript) transitioning to Python and the Odoo framework.</li>\n    <li>Technical consultants and implementers who need to build and deploy custom Odoo modules with confidence.</li>\n  </ul>\n  <h3>Prerequisites</h3>\n  <ul>\n    <li>Basic computer literacy and command-line comfort (terminal / shell usage).</li>\n    <li>A laptop able to run Python 3.12, PostgreSQL and VSCode (Windows, macOS or Linux).</li>\n    <li>No prior Python or Odoo experience required — we start from the absolute basics.</li>\n  </ul>\n  <h3>Roadmap</h3>\n  <ol>\n    <li><strong>Phase 1 — Foundations:</strong> Python Fundamentals; Database Query (SQL &amp; PostgreSQL).</li>\n    <li><strong>Phase 2 — Integration:</strong> FastAPI + Odoo Integration (JSON-RPC, REST endpoints, Pydantic, auth).</li>\n    <li><strong>Phase 3 — Odoo Development:</strong> architecture &amp; environment, first module, ORM models &amp; fields, computed fields &amp; constraints, ORM methods, views (form, list, search), inheritance, workflows, wizards, security, QWeb reports, scheduled actions, external API, deployment.</li>\n    <li><strong>Phase 4 — Capstone:</strong> a full custom Service Request Management module, built and deployed end-to-end (6 hours).</li>\n  </ol>\n</div>"

CHANNEL_DESCRIPTION_HTML = "<div class=\"prospire-course-detail\">\n  <h3>About this training</h3>\n  <p>Delivered as a joint venture between ProspireNext and SDTEK, this instructor-led style eLearning track mirrors the SDTEKH technical bootcamp. Every lesson pairs concise theory with a hands-on exercise, and every section ends with a deliverable you can show in a portfolio or at work.</p>\n  <h3>What you will be able to do</h3>\n  <ul>\n    <li>Write idiomatic Python: data structures, functions, OOP, files and error handling.</li>\n    <li>Design and query PostgreSQL databases: joins, aggregates, subqueries, indexes.</li>\n    <li>Build FastAPI services that talk to Odoo over JSON-RPC / XML-RPC, with Pydantic schemas and proper auth.</li>\n    <li>Develop complete Odoo 18 modules: models, views, security, workflows, wizards, PDF reports, cron jobs and external endpoints.</li>\n    <li>Deploy Odoo on Ubuntu with Nginx, SSL and automated PostgreSQL backups.</li>\n  </ul>\n  <h3>Format</h3>\n  <ul>\n    <li>16 classes + 1 capstone project, ~38 hours total.</li>\n    <li>Each lesson states its level (Beginner / Intermediate / Advanced) and duration.</li>\n    <li>Lessons are text outlines today; video walkthroughs are added progressively.</li>\n  </ul>\n</div>"

CURRICULUM = [
    {
        'name': "Python Fundamentals",
        'lessons': [
            {
                'name': "Python Setup & Developer Roadmap",
                'hours': 0.5,
                'level': "Beginner",
                'summary': "Level: Beginner | Duration: ~0.5h. Install Python 3.12, pip, venv and VSCode, run your first scripts, and preview the full beginner-to-advanced Python developer roadmap.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Get a professional Python environment running and understand where this course is taking you.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Installing Python 3.12 on Windows, macOS and Linux; verifying with <code>python --version</code>.</li>\n    <li>pip: installing, upgrading and listing packages.</li>\n    <li>Virtual environments with <code>venv</code>: create, activate, deactivate, why isolation matters.</li>\n    <li>VSCode setup: Python extension, interpreters, running and debugging scripts, the integrated terminal.</li>\n    <li>Running scripts: <code>python app.py</code>, the REPL, and <code>if __name__ == \"__main__\"</code>.</li>\n    <li>Developer roadmap: syntax basics → data structures → functions → OOP → files/exceptions → packages → testing → web APIs (FastAPI) → databases (SQL) → Odoo framework.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Install Python 3.12 and VSCode, create a virtual environment <code>sdtekh-env</code>, and run a script <code>hello.py</code> that prints your name, Python version and the path of the active interpreter.</p>\n</div>",
            },
            {
                'name': "Variables, Data Types & Operators",
                'hours': 0.5,
                'level': "Beginner",
                'summary': "Level: Beginner | Duration: ~0.5h. Names, values and the core built-in types, plus every operator group you will use daily.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Master the vocabulary of Python: how values are stored, typed and combined.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Variables as names bound to objects; assignment and reassignment; naming rules and conventions (snake_case).</li>\n    <li>Core types: <code>int</code>, <code>float</code>, <code>str</code>, <code>bool</code>, <code>NoneType</code>; <code>type()</code> and <code>isinstance()</code>.</li>\n    <li>Strings: indexing, slicing, immutability, f-strings, common methods (<code>strip</code>, <code>split</code>, <code>join</code>, <code>replace</code>).</li>\n    <li>Operators: arithmetic, comparison, logical (<code>and</code>/<code>or</code>/<code>not</code>), membership (<code>in</code>), identity (<code>is</code>), assignment shortcuts; operator precedence.</li>\n    <li>Truthiness and type conversion (<code>int()</code>, <code>str()</code>, <code>float()</code>).</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Build a <code>profile_card.py</code> that stores your name, age, height and \"is enrolled\" flag in variables, then prints a one-line summary using an f-string with a type shown for each value.</p>\n</div>",
            },
            {
                'name': "Control Flow: if/elif/else, loops",
                'hours': 0.5,
                'level': "Beginner",
                'summary': "Level: Beginner | Duration: ~0.5h. Decision-making and repetition: conditionals, for/while loops, break/continue and comprehensions.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Control the path your program takes: branch on conditions and repeat work without repeating code.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li><code>if</code> / <code>elif</code> / <code>else</code>; nested conditions; ternary expressions.</li>\n    <li><code>for</code> loops over ranges, strings and collections; <code>range()</code>, <code>enumerate()</code>, <code>zip()</code>.</li>\n    <li><code>while</code> loops and sentinel values; avoiding infinite loops.</li>\n    <li>Loop control: <code>break</code>, <code>continue</code>, <code>else</code> on loops.</li>\n    <li>List and dictionary comprehensions; when they help and when they hurt readability.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Write a number-classifier script: for numbers 1–50 print \"Fizz\" (÷3), \"Buzz\" (÷5), \"FizzBuzz\" (both) or the number, then count and display how many of each category were printed using a loop — no hard-coded counts.</p>\n</div>",
            },
            {
                'name': "Functions, Arguments & Modules",
                'hours': 0.5,
                'level': "Beginner",
                'summary': "Level: Beginner | Duration: ~0.5h. Defining functions, every argument flavor, return values, lambda expressions, and organizing code into modules.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Functions are the unit of reuse in Python — and the building blocks of every Odoo model method you will write later.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li><code>def</code>, parameters vs arguments, return values, multiple returns, early returns.</li>\n    <li>Positional, keyword, default, <code>*args</code> and <code>**kwargs</code>; keyword-only arguments.</li>\n    <li>Scope: local vs global, the LEGB rule, why globals are avoided.</li>\n    <li>Lambda expressions and the key functions <code>sorted()</code>, <code>min()</code>, <code>max()</code>, <code>filter()</code>, <code>map()</code>.</li>\n    <li>Modules and imports: <code>import</code>, <code>from ... import</code>, <code>__name__</code>, the standard library tour (datetime, json, csv, os, sys).</li>\n    <li>Docstrings and type hints as documentation habits.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Create a module <code>text_utils.py</code> with <code>slugify(text)</code>, <code>word_count(text)</code> and <code>censor(text, *words)</code>; import it from <code>main.py</code> and demo each function with printed output.</p>\n</div>",
            },
            {
                'name': "Data Structures: list, tuple, dict, set",
                'hours': 0.5,
                'level': "Beginner",
                'summary': "Level: Beginner | Duration: ~0.5h. The four built-in collections, when to use each, and the operations that cover 95% of real code.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Choosing the right collection is half of Python programming — and Odoo recordsets behave like specialized lists.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li><code>list</code>: ordered, mutable; append/insert/remove/pop, slicing, sorting (<code>sort()</code> vs <code>sorted()</code>), list methods.</li>\n    <li><code>tuple</code>: ordered, immutable; packing/unpacking, named tuples.</li>\n    <li><code>dict</code>: key-value storage; get/setdefault/pop, keys/values/items, dict comprehensions, nesting; why dict keys must be hashable.</li>\n    <li><code>set</code>: uniqueness and set algebra (union, intersection, difference).</li>\n    <li>Mutability vs immutability; shallow vs deep copies; common pitfalls (mutable default arguments).</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Build an inventory tracker: a dict of products → stock counts, a list of restock transactions, and functions using set operations to report \"products sold but never restocked\" and low-stock items.</p>\n</div>",
            },
            {
                'name': "OOP Basics: classes, objects, inheritance",
                'hours': 0.5,
                'level': "Beginner",
                'summary': "Level: Beginner | Duration: ~0.5h. Classes, instances, methods, inheritance and dunder methods — the exact concepts the Odoo ORM is built on.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Odoo models <em>are</em> Python classes — this lesson is the direct on-ramp to the framework.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Class vs instance; <code>__init__</code> and instance attributes; class attributes and shared state.</li>\n    <li>Instance methods, <code>@classmethod</code>, <code>@staticmethod</code>; <code>self</code> explained.</li>\n    <li>Inheritance: extending and overriding methods, <code>super()</code>, multiple inheritance basics.</li>\n    <li>Encapsulation conventions (public, <code>_protected</code>, <code>__private</code>); <code>@property</code>.</li>\n    <li>Dunder methods: <code>__str__</code>, <code>__repr__</code>, <code>__eq__</code>, <code>__len__</code>, <code>__getitem__</code> — how objects plug into Python syntax.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Model a mini LMS: a <code>Course</code> class (title, lessons list, add/remove lesson, <code>duration_hours</code> property) and an inherited <code>PublishedCourse</code> that adds publish state and overrides <code>__str__</code>.</p>\n</div>",
            },
            {
                'name': "File Handling & Exceptions",
                'hours': 0.5,
                'level': "Beginner",
                'summary': "Level: Beginner | Duration: ~0.5h. Reading and writing files safely, and handling errors with try/except instead of crashing.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Real programs read files and survive bad input — here is how to do both cleanly.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>The <code>with open(...) as f</code> pattern; read/write/append modes; text vs binary.</li>\n    <li>Reading line by line, <code>read()</code> vs <code>readlines()</code>; writing and <code>json</code>/<code>csv</code> module basics.</li>\n    <li>Exceptions: try/except/else/finally; catching specific exceptions; raising with <code>raise</code>; custom exception classes.</li>\n    <li>EAFP vs LBYL styles; the exception hierarchy; never bare <code>except:</code>.</li>\n    <li>Path handling with <code>pathlib</code>.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Write <code>expenses.py</code>: load a CSV of expenses, skip malformed rows with per-row error messages, compute totals per category, and write a JSON summary — then handle a missing file gracefully.</p>\n</div>",
            },
            {
                'name': "Problem-Solving Lab — 10 Python Exercises",
                'hours': 1.0,
                'level': "Beginner",
                'summary': "Level: Beginner | Duration: ~1h. Ten small real exercises — from FizzBuzz to a CSV summarizer — each with a solution hint to unblock you.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Ten exercises that combine everything from this section. Try each for 10 minutes before reading the hint.</p>\n  <h4>Exercises</h4>\n  <ol>\n    <li><strong>FizzBuzz:</strong> print 1–100; multiples of 3 → \"Fizz\", of 5 → \"Buzz\", of both → \"FizzBuzz\". <em>Hint: check the combined condition first, or use a list of parts and <code>\"\".join</code>.</em></li>\n    <li><strong>Palindrome checker:</strong> return True if a string reads the same ignoring case, spaces and punctuation. <em>Hint: filter with <code>str.isalnum</code>, then compare <code>s == s[::-1]</code>.</em></li>\n    <li><strong>Word counter:</strong> read a text and return the 5 most frequent words with counts. <em>Hint: <code>dict.get(word, 0) + 1</code>, then <code>sorted(items, key=lambda kv: kv[1], reverse=True)</code> or <code>collections.Counter</code>.</em></li>\n    <li><strong>Fibonacci:</strong> return the first N Fibonacci numbers, both as a list and as a generator. <em>Hint: iterate with two variables <code>a, b = b, a + b</code>; <code>yield</code> for the generator.</em></li>\n    <li><strong>Duplicate remover:</strong> given a list, return it deduplicated while preserving order. <em>Hint: <code>list(dict.fromkeys(items))</code>, or a set for seen membership in a loop.</em></li>\n    <li><strong>CSV reader summary:</strong> read <code>sales.csv</code> (date, product, amount) and print total and average amount per product. <em>Hint: <code>csv.DictReader</code> + a dict of lists, or running totals with <code>float(row[\"amount\"])</code>.</em></li>\n    <li><strong>Prime numbers:</strong> list all primes below N using a simple sieve. <em>Hint: start from a list of True flags, cross out multiples of each prime up to √N.</em></li>\n    <li><strong>Password strength validator:</strong> score a password 0–4 for length ≥ 8, upper+lower, digit, symbol. <em>Hint: sum boolean checks; use <code>any(c.isupper() for c in pw)</code>.</em></li>\n    <li><strong>Contact book:</strong> dict-backed add/search/delete/list commands in a loop, persisted to JSON on exit. <em>Hint: <code>while True</code> + <code>input()</code> dispatch, <code>json.dump</code> in a <code>finally</code>.</em></li>\n    <li><strong>Number guessing game:</strong> the program picks 1–100 and answers \"higher/lower\" until guessed; count attempts. <em>Hint: <code>random.randint</code>, <code>int(input())</code> wrapped in try/except for non-numeric input.</em></li>\n  </ol>\n  <h4>Deliverable</h4>\n  <p>One <code>lab01.py</code> (or a <code>lab01/</code> package) where each exercise is a function with a docstring, plus a small demo block that runs all ten.</p>\n</div>",
            },
        ],
    },
    {
        'name': "Database Query (SQL & PostgreSQL)",
        'lessons': [
            {
                'name': "Relational Databases & PostgreSQL Setup",
                'hours': 0.5,
                'level': "Beginner",
                'summary': "Level: Beginner | Duration: ~0.5h. Relational concepts (tables, keys, relationships) and a working local PostgreSQL with a practice database.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Odoo stores everything in PostgreSQL — understanding relational basics makes the whole framework click.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Relational model: tables, rows, columns; primary keys, foreign keys, NULL semantics.</li>\n    <li>Relationship types: one-to-many, many-to-many (join tables); normalization in one paragraph.</li>\n    <li>Installing PostgreSQL (Windows installer, macOS Homebrew, apt on Ubuntu); the <code>psql</code> shell and pgAdmin.</li>\n    <li>Creating a database and user: <code>CREATE DATABASE training;</code>, roles and passwords.</li>\n    <li>Data types: INTEGER, NUMERIC/DECIMAL, VARCHAR/TEXT, BOOLEAN, DATE/TIMESTAMP, JSONB; choosing wisely.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Install PostgreSQL, create database <code>sdtekh_training</code> with user <code>student</code>, and design on paper (or SQL) two related tables — <code>customers</code> and <code>orders</code> — linked by a foreign key.</p>\n</div>",
            },
            {
                'name': "SELECT, WHERE, ORDER BY, LIMIT",
                'hours': 0.5,
                'level': "Beginner",
                'summary': "Level: Beginner | Duration: ~0.5h. The 90%-of-queries toolkit: projecting columns, filtering rows, sorting and paging results.",
                'html': "<div class=\"prospire-lesson\">\n  <p>The core SELECT statement — every ORM, including Odoo's, compiles down to this.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li><code>SELECT</code> column lists, aliases, <code>DISTINCT</code>, expressions and computed columns.</li>\n    <li><code>WHERE</code> filters: comparison, <code>AND/OR/NOT</code>, <code>IN</code>, <code>BETWEEN</code>, <code>LIKE</code> with wildcards, <code>IS NULL</code>.</li>\n    <li><code>ORDER BY</code> multi-column asc/desc; <code>LIMIT</code> / <code>OFFSET</code> paging.</li>\n    <li>NULL three-valued logic and why <code>= NULL</code> never matches.</li>\n    <li>Logical order of execution: FROM → WHERE → SELECT → ORDER BY → LIMIT.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>On your <code>orders</code> table: write queries for (1) orders above $500 sorted newest-first, (2) unique cities of customers, (3) the 10 most recent pending orders — save them in <code>queries/02_select.sql</code>.</p>\n</div>",
            },
            {
                'name': "JOINs: INNER, LEFT, RIGHT",
                'hours': 0.5,
                'level': "Intermediate",
                'summary': "Level: Intermediate | Duration: ~0.5h. Combining tables: INNER vs LEFT vs RIGHT joins, join conditions, and the classic mistakes.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Odoo's relational fields (Many2one, One2many) are JOINs underneath — read this lesson and the ORM stops being magic.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>INNER JOIN: only matching rows on both sides; the join condition in <code>ON</code> vs <code>WHERE</code>.</li>\n    <li>LEFT JOIN: keep all left rows, NULLs where no match; the canonical \"orders with customer names\" pattern.</li>\n    <li>RIGHT JOIN and why most people rewrite it as a LEFT JOIN; FULL OUTER JOIN for completeness.</li>\n    <li>Self joins and joining more than two tables; aliasing tables.</li>\n    <li>Pitfalls: filtering on the right table in <code>WHERE</code> silently turning a LEFT JOIN into an INNER JOIN; accidental row multiplication.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Write three reports over <code>customers</code>/<code>orders</code>: all orders with customer name (INNER), all customers including those without orders (LEFT), and all customers who have <em>never</em> ordered (LEFT + <code>IS NULL</code>).</p>\n</div>",
            },
            {
                'name': "GROUP BY, Aggregates & HAVING",
                'hours': 0.5,
                'level': "Intermediate",
                'summary': "Level: Intermediate | Duration: ~0.5h. Summarizing data: COUNT/SUM/AVG/MIN/MAX, grouping rules, and filtering groups with HAVING.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Aggregations turn rows into answers — the same math Odoo shows in its pivot and graph views.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Aggregate functions: <code>COUNT(*)</code> vs <code>COUNT(col)</code>, <code>SUM</code>, <code>AVG</code>, <code>MIN</code>, <code>MAX</code>; NULL handling in aggregates.</li>\n    <li><code>GROUP BY</code> one or several columns; every selected column must be aggregated or grouped.</li>\n    <li><code>HAVING</code> vs <code>WHERE</code>: filter rows before grouping vs filter groups after.</li>\n    <li>Grouping with joins; <code>GROUP BY</code> with expressions (e.g. date parts).</li>\n    <li>Odoo connection: <code>read_group()</code> in the ORM is exactly this lesson in Python form.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Produce a sales report: revenue and order count per customer, only customers with 3+ orders and revenue over $1000, sorted by revenue descending.</p>\n</div>",
            },
            {
                'name': "Subqueries & Indexes",
                'hours': 0.5,
                'level': "Intermediate",
                'summary': "Level: Intermediate | Duration: ~0.5h. Queries inside queries, and the indexes that keep them fast as data grows.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Two skills separate hobby SQL from professional SQL: composing subqueries, and understanding indexes.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Subquery types: scalar, IN, EXISTS (and NOT EXISTS); correlated vs non-correlated.</li>\n    <li>Subqueries in SELECT/WHERE/FROM; when a JOIN is clearer than a subquery.</li>\n    <li>Indexes: B-tree default, how they speed lookups and sorts, the cost on writes.</li>\n    <li>Composite indexes and column order; partial and unique indexes.</li>\n    <li>Reading a query plan with <code>EXPLAIN ANALYZE</code>; spotting sequential scans; why Odoo indexes every <code>xxx_id</code> column automatically.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Write \"customers whose latest order is above average\" using a subquery, then re-implement with a JOIN; add an index supporting your most common filter and show the plan difference with <code>EXPLAIN ANALYZE</code>.</p>\n</div>",
            },
            {
                'name': "SQL from Python (psycopg2) & SQL vs Odoo ORM",
                'hours': 0.5,
                'level': "Intermediate",
                'summary': "Level: Intermediate | Duration: ~0.5h. Executing SQL from Python with psycopg2, parameterized queries, and when to use raw SQL vs the Odoo ORM.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Bridge the two worlds: talk to PostgreSQL directly from Python, then understand how the Odoo ORM relates to it.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>psycopg2 setup: <code>pip install psycopg2-binary</code>, connecting with <code>psycopg2.connect</code>, connection/cursor lifecycle.</li>\n    <li>Executing queries: <code>execute()</code>, <code>fetchall/fetchone</code>, row factories, dict cursors; transactions, <code>commit()</code>/<code>rollback()</code>.</li>\n    <li>SQL injection and parameterized queries (<code>%s</code> placeholders) — never f-strings for values.</li>\n    <li>SQL vs Odoo ORM: <code>search()/browse()</code> generate SQL but add access rights, record rules, caching and computed fields; <code>cr.execute()</code> when you truly need raw SQL.</li>\n    <li>Rule of thumb: ORM by default, SQL for reporting/performance, always parameterized.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Write <code>db_report.py</code>: connect with psycopg2, take a customer name as a <em>parameterized</em> input, print their order totals; then write the equivalent Odoo <code>env['sale.order'].search([...])</code> call and note the differences.</p>\n</div>",
            },
        ],
    },
    {
        'name': "FastAPI + Odoo Integration",
        'lessons': [
            {
                'name': "FastAPI Project Setup & Uvicorn",
                'hours': 0.5,
                'level': "Advanced",
                'summary': "Level: Advanced | Duration: ~0.5h. Scaffold a FastAPI project, understand the app/router structure, and run it with Uvicorn (with auto-reload).",
                'html': "<div class=\"prospire-lesson\">\n  <p>FastAPI is our integration layer: a modern, fast Python web framework that will sit in front of Odoo's RPC APIs.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Project scaffold: <code>pip install fastapi uvicorn</code>, the <code>main.py</code> entry point, virtualenv layout.</li>\n    <li>First app: <code>app = FastAPI()</code>, path operations (<code>@app.get/post/put/delete</code>), path and query parameters.</li>\n    <li>Running with Uvicorn: <code>uvicorn main:app --reload</code>, host/port options, what the ASGI server does.</li>\n    <li>Interactive docs out of the box: <code>/docs</code> (Swagger UI) and <code>/redoc</code>.</li>\n    <li>Project structure: routers, <code>APIRouter</code> prefixes, settings via environment variables.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Create the <code>odoo-bridge</code> project: a <code>/health</code> endpoint returning <code>{\"status\": \"ok\"}</code> and a <code>/hello/{name}</code> endpoint, both visible and testable in <code>/docs</code>.</p>\n</div>",
            },
            {
                'name': "Odoo JSON-RPC & xmlrpc.client from FastAPI",
                'hours': 0.5,
                'level': "Advanced",
                'summary': "Level: Advanced | Duration: ~0.5h. Two ways to call Odoo from FastAPI: JSON-RPC over HTTP and Python's built-in xmlrpc.client.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Odoo exposes its whole ORM over RPC. This lesson connects FastAPI to a live Odoo instance both ways.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>The RPC landscape: <code>/jsonrpc</code> endpoint, common methods <code>authenticate</code>, <code>execute_kw</code>; session cookies vs explicit credentials.</li>\n    <li>JSON-RPC from FastAPI with <code>httpx</code> or <code>requests</code>: payload shape, <code>jsonrpc=2.0</code> envelope, reading <code>result</code>/<code>error</code>.</li>\n    <li><code>xmlrpc.client</code>: <code>ServerProxy</code> for <code>common</code> (uid) and <code>models</code> (<code>execute_kw</code>) — no extra dependency.</li>\n    <li>Typical flow: authenticate → uid → <code>execute_kw(db, uid, password, model, method, args, kwargs)</code>.</li>\n    <li>Hiding credentials in env vars; connection reuse; timeouts and error envelopes.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Build <code>odoo_client.py</code> with a small client class exposing <code>search_read(model, domain, fields)</code> over <code>xmlrpc.client</code>; call it from a FastAPI endpoint that lists CRM leads.</p>\n</div>",
            },
            {
                'name': "REST Endpoints Reading & Writing Odoo Models",
                'hours': 0.5,
                'level': "Advanced",
                'summary': "Level: Advanced | Duration: ~0.5h. Design clean REST resources (GET/POST/PUT/DELETE) that map onto Odoo model operations via RPC.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Turn Odoo's ORM into a clean REST API you control — the pattern used in real integrations.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Resource design: nouns in URLs (<code>/leads</code>, <code>/leads/{id}</code>), verbs via HTTP methods, status codes (200/201/404/422/500).</li>\n    <li>Read side: <code>search_read</code> with domains, field lists, limits and offsets; pagination with <code>count</code>.</li>\n    <li>Write side: <code>create</code> (returns id), <code>write</code>, <code>unlink</code>; mapping JSON bodies to Odoo field values.</li>\n    <li>Calling model methods over RPC (e.g. <code>action_confirm</code>) from a POST endpoint.</li>\n    <li>Error translation: Odoo exceptions → meaningful HTTP errors, never raw tracebacks to clients.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Implement <code>GET /leads</code> (paged, filterable by stage) and <code>GET /leads/{id}</code> (404 when missing) against Odoo <code>crm.lead</code>, returning clean JSON.</p>\n</div>",
            },
            {
                'name': "Auth: API Key vs Session Token",
                'hours': 0.5,
                'level': "Advanced",
                'summary': "Level: Advanced | Duration: ~0.5h. Secure the bridge: FastAPI API keys for service clients, Odoo session tokens for user-delegated calls, and when to use which.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Every integration answers one question first: <em>who is calling, and on whose behalf?</em></p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>FastAPI-side API keys: <code>Header(...)</code> or <code>APIKeyHeader</code>, dependency injection with <code>Depends</code>, key storage and rotation.</li>\n    <li>Odoo-side identities: service account (dedicated user, least-privilege groups) vs end-user delegation.</li>\n    <li>Odoo session tokens: logging in via <code>/web/session/authenticate</code> (JSON-RPC) and reusing the session cookie for subsequent calls.</li>\n    <li>Trade-offs: API key = simple, service-level permissions; session token = acts as the real user, inherits their rights and record rules.</li>\n    <li>TLS everywhere, key in headers (never query strings), rejecting unknown keys with 401 vs 403.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Protect your <code>/leads</code> endpoints with a FastAPI API-key dependency, and implement an <code>/auth/session</code> endpoint that exchanges Odoo credentials for a session cookie and returns the user's rights summary.</p>\n</div>",
            },
            {
                'name': "Pydantic Schemas",
                'hours': 0.5,
                'level': "Advanced",
                'summary': "Level: Advanced | Duration: ~0.5h. Validate and document payloads with Pydantic models: request bodies, response models, field types and constraints.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Pydantic gives you validation, serialization and OpenAPI documentation from one class definition.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Defining <code>BaseModel</code> schemas: field types, defaults, <code>Optional</code>, nested models, lists of models.</li>\n    <li>Validation: constraints (<code>gt/ge/lt/le</code>, <code>min_length</code>, <code>regex</code>), custom validators with <code>@field_validator</code>, <code>EmailStr</code> and friends.</li>\n    <li>Request bodies (<code>payload: LeadCreate</code>) and response models (<code>response_model=LeadOut</code>); how they shape the OpenAPI schema.</li>\n    <li>Serialization helpers: <code>model_dump()</code>, <code>model_dump(by_alias=True)</code>, <code>from_attributes</code> for ORM/RPC rows.</li>\n    <li>422 responses for free: FastAPI turns validation errors into structured error responses.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Define <code>LeadCreate</code> (name required, email validated, expected_revenue ≥ 0, optional phone) and <code>LeadOut</code>; wire them as request/response models on your lead endpoints.</p>\n</div>",
            },
            {
                'name': "Background Tasks & Error Handling",
                'hours': 0.5,
                'level': "Advanced",
                'summary': "Level: Advanced | Duration: ~0.5h. Keep endpoints fast with background tasks, and handle failures consistently across the service.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Slow Odoo calls shouldn't block your API — and failures must be observable, not silent.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>FastAPI <code>BackgroundTasks</code>: fire-and-forget work after the response; when it is (and isn't) enough.</li>\n    <li>Heavier workloads: task queues in one paragraph (Celery/RQ), and why cron-style Odoo jobs sometimes replace them entirely.</li>\n    <li>Exception handlers: <code>@app.exception_handler</code> mapping Odoo/XML-RPC faults to HTTP errors; consistent error body shape.</li>\n    <li>Logging: structured logs with request ids; never log secrets or full credentials.</li>\n    <li>Resilience: timeouts on every RPC call, retries with backoff for transient failures, circuit-breaker mindset.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Add a <code>POST /leads/{id}/notify</code> endpoint that responds immediately and sends the notification via a background task; add a global exception handler returning <code>{\"detail\": ...}</code> with the right status codes.</p>\n</div>",
            },
            {
                'name': "Exercise: Build a FastAPI Service — POST /leads → Odoo CRM Lead",
                'hours': 0.5,
                'level': "Advanced",
                'summary': "Level: Advanced | Duration: ~0.5h. Capstone exercise for the section: a validated, secured POST /leads endpoint that creates a real CRM lead in Odoo.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Combine the whole section: a public, validated endpoint that writes into Odoo CRM.</p>\n  <h4>Requirements</h4>\n  <ul>\n    <li><code>POST /leads</code> accepting a Pydantic-validated body (name, email, phone, expected_revenue, notes).</li>\n    <li>Create the lead in Odoo via <code>execute_kw(..., 'crm.lead', 'create', [values])</code> using a least-privilege Odoo service account.</li>\n    <li>Respond <code>201 Created</code> with the new lead id and Odoo link; <code>422</code> on invalid payloads; <code>502</code> with a safe message when Odoo is unreachable.</li>\n    <li>Protect the route with an API key; log the creation with a request id.</li>\n    <li>Optional stretch goal: send a confirmation email from a background task.</li>\n  </ul>\n  <h4>Deliverable</h4>\n  <p>A working service: <code>curl -X POST /leads</code> creates a visible lead in the Odoo CRM pipeline, with a README covering setup, env vars and example calls.</p>\n</div>",
            },
        ],
    },
    {
        'name': "Odoo Architecture & Dev Environment Setup",
        'lessons': [
            {
                'name': "Odoo Architecture & Dev Environment Setup",
                'hours': 1.0,
                'level': "Intermediate",
                'summary': "Level: Intermediate | Duration: ~1h. MVC in Odoo, installing Odoo 18/19 Community from source, VSCode + odoo.conf + debug mode, and the anatomy of a module's file structure.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Before writing modules, understand the machine: Odoo's MVC-flavored architecture and a source install you control.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>MVC in Odoo: Models (Python/ORM), Views (XML/QWeb), Controllers (HTTP); where business logic belongs and why fat models beat fat controllers.</li>\n    <li>Source install of Odoo 18/19 Community: system dependencies, PostgreSQL, Python virtualenv, <code>pip install -r requirements.txt</code>, running from source with <code>odoo-bin</code>.</li>\n    <li>VSCode configuration: Python interpreter, launch.json for debugging <code>odoo-bin</code>, breakpoints in framework code.</li>\n    <li><code>odoo.conf</code>: addons_path, db_host/port/user/password, xmlrpc_port, workers, log_level; the <code>-c</code> flag, <code>-d</code>, <code>-u</code>, <code>--dev=xml</code>.</li>\n    <li>Developer mode: activating it (<code>?debug=1</code>), what the UI reveals — fields, views, model metadata, the technical menu.</li>\n    <li>Module file structure: <code>__manifest__.py</code>, <code>__init__.py</code>, <code>models/</code>, <code>views/</code>, <code>security/</code>, <code>data/</code>, <code>static/</code>, <code>controllers/</code>.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Install Odoo 18 (or 19) Community from source with its own virtualenv and database, start it with a custom <code>odoo.conf</code>, connect VSCode and hit a breakpoint in <code>odoo-bin</code>, and activate developer mode in the UI.</p>\n</div>",
            },
        ],
    },
    {
        'name': "Creating Your First Custom Module",
        'lessons': [
            {
                'name': "Creating Your First Custom Module",
                'hours': 1.0,
                'level': "Beginner",
                'summary': "Level: Beginner | Duration: ~1h. Every key of __manifest__.py, the __init__.py import chain, categories, dependencies, and the install/upgrade cycle — ending in a Hello World module.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Your first module, built line by line so nothing in the boilerplate stays mysterious.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li><code>__manifest__.py</code> keys: <code>name</code>, <code>version</code> (<code>18.0.1.0.0</code>), <code>summary</code>, <code>category</code>, <code>author</code>, <code>license</code>, <code>depends</code>, <code>data</code> (ordered file list), <code>assets</code>, <code>installable</code>, <code>application</code>, <code>post_init_hook</code>.</li>\n    <li>The <code>__init__.py</code> import chain: root imports <code>models</code>, <code>models/__init__.py</code> imports each model file; forgotten imports as the #1 \"my code doesn't load\" bug.</li>\n    <li>Module categories and what they change (grouping in the apps list — nothing technical); <code>application: True/False</code>.</li>\n    <li>Dependencies: depending on <code>base</code> vs <code>sale</code>; load order; never depends on what you don't use.</li>\n    <li>The cycle: install (-i), upgrade/update (-u), uninstall; when a full restart is required; reading tracebacks during install.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Build module <code>hello_world</code>: a <code>hello.world</code> model with a <code>name</code> field, a menu + action + form/list views, installable from the apps list with no warnings. Screenshot the working list view.</p>\n</div>",
            },
        ],
    },
    {
        'name': "Models & Fields — The Odoo ORM",
        'lessons': [
            {
                'name': "Models & Fields — The Odoo ORM",
                'hours': 1.5,
                'level': "Intermediate",
                'summary': "Level: Intermediate | Duration: ~1.5h. Scalar and relational field types (Char, Integer, Float, Boolean, Date, Binary, Many2one, One2many, Many2many, Selection, Html) plus _name, _rec_name and _order.",
                'html': "<div class=\"prospire-lesson\">\n  <p>The ORM is Odoo's heart: define models in Python, get tables, forms and APIs for free.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Model basics: <code>class ProjectTask(models.Model)</code>, <code>_name</code>, <code>_description</code>, <code>_rec_name</code> (display name field), <code>_order</code> (default sort).</li>\n    <li>Scalar fields: <code>Char</code>, <code>Text</code>, <code>Html</code>, <code>Integer</code>, <code>Float</code> (<code>digits</code>), <code>Boolean</code>, <code>Date</code>, <code>Datetime</code>, <code>Binary</code> (attachments), <code>Selection</code> (list of key-label pairs).</li>\n    <li>Common field attributes: <code>string</code>, <code>required</code>, <code>readonly</code>, <code>default</code> (value or callable), <code>index</code>, <code>copy</code>, <code>help</code>.</li>\n    <li>Relational fields: <code>Many2one('res.partner')</code> (and <code>ondelete</code>), <code>One2many('model', 'inverse_field')</code> — never stored, a window on the other side; <code>Many2many</code> with the auto-created relation table.</li>\n    <li>Automatic fields: <code>id</code>, <code>create_date/write_date</code>, <code>create_uid/write_uid</code>, <code>display_name</code>; conventions: model names singular dotted (<code>project.task</code>), tables auto-named.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Model a <code>project.task</code> with 6+ field types: Char (title), Text (description), Selection (priority), Date (deadline), Float (planned_hours, digits), Many2one (assigned user → res.users), plus Boolean (is_done) and Html (notes). Install and inspect the generated table in PostgreSQL.</p>\n</div>",
            },
        ],
    },
    {
        'name': "Computed Fields, Constraints & Onchange",
        'lessons': [
            {
                'name': "Computed Fields, Constraints & Onchange",
                'hours': 1.5,
                'level': "Intermediate",
                'summary': "Level: Intermediate | Duration: ~1.5h. @api.depends with stored vs real-time computed fields, @api.constrains, @api.onchange and _sql_constraints — with an auto-computed total plus a validation rule.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Make the ORM work for you: values that compute themselves, rules that reject bad data, and forms that react while you type.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Computed fields: <code>compute='_compute_total'</code> with <code>@api.depends('line_ids.price')</code>; non-stored (real-time, not writable/searchable) vs <code>store=True</code> (written to DB, searchable, recomputed on dependency change).</li>\n    <li>Inverse methods (<code>inverse='_set_total'</code>) and computed defaults; multi-record compute loops.</li>\n    <li>Python constraints: <code>@api.constrains('amount')</code> raising <code>ValidationError</code>; when they run (create/write).</li>\n    <li>SQL constraints: <code>_sql_constraints</code> (<code>UNIQUE</code>, <code>CHECK</code>) — faster, DB-level, but no custom messages per context; the modern <code>models.Constraint</code> syntax.</li>\n    <li>Onchange: <code>@api.onchange('partner_id')</code> updating fields live in the form and returning warning domains; why onchange is UI-only (never rely on it for data integrity).</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Extend your task model: a stored computed field <code>total_hours</code> summing a One2many of time entries (with <code>@api.depends</code>), a <code>@api.constrains</code> rule rejecting negative hours, an <code>_sql_constraint</code> making task titles unique per project, and an onchange that sets a default deadline 7 days out when a project is chosen.</p>\n</div>",
            },
        ],
    },
    {
        'name': "ORM Methods & Recordset Operations",
        'lessons': [
            {
                'name': "ORM Methods & Recordset Operations",
                'hours': 1.5,
                'level': "Intermediate",
                'summary': "Level: Intermediate | Duration: ~1.5h. search/browse/create/write/unlink, domain syntax in depth, filtered/mapped/sorted, and sudo/with_context/with_user — exercised on overdue invoices.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Everything you do in Odoo is a recordset operation. This lesson is the API reference you will actually use.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>CRUD: <code>create(vals)</code> (single & multi), <code>write(vals)</code>, <code>unlink()</code>; <code>browse(ids)</code> vs <code>search(domain)</code> (recordsets, not lists).</li>\n    <li><code>search</code> options: <code>offset</code>, <code>limit</code>, <code>order</code>, <code>count=True</code>, <code>search_count</code>; <code>search_read</code> for dict rows.</li>\n    <li>Domain syntax: <code>[('state','=','open')]</code>; operators =, !=, &gt;, &gt;=, &lt;, &lt;=, like/ilike, in, not in, child_of; prefixes <code>'|'</code> (OR) and <code>'!'</code> (NOT) and implicit AND; common traps (OR chaining, date comparisons).</li>\n    <li>Recordset pipelines: <code>filtered(lambda r: ...)</code>, <code>filtered('state')</code>, <code>mapped('field')</code>, <code>sorted(key=...)</code>, <code>+</code> union, <code>ids</code>, <code>ensure_one()</code>, <code>exists()</code>.</li>\n    <li>Environment switching: <code>sudo()</code> (bypass rights — use with care), <code>with_context(key=value)</code> (tracking_disable, mail_notrack, custom flags), <code>with_user(user)</code> (act as someone else, rights still apply).</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Write a script/method (run via shell or a server action) that finds unpaid <code>account.move</code> invoices more than 30 days past invoice date, groups them by commercial partner, and returns a printable summary sorted by amount due.</p>\n</div>",
            },
        ],
    },
    {
        'name': "Form & List Views — XML Architecture",
        'lessons': [
            {
                'name': "Form & List Views — XML Architecture",
                'hours': 1.5,
                'level': "Intermediate",
                'summary': "Level: Intermediate | Duration: ~1.5h. sheet/header/chatter, groups/notebooks/pages, list optional columns and decoration attributes, and buttons type=object vs type=action.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Views turn models into usable screens. Learn the form/list XML architecture properly once, and every module benefits.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>View record anatomy: <code>&lt;record model=\"ir.ui.view\"&gt;</code> with <code>name</code>, <code>model</code>, <code>arch</code> (the XML structure), plus the action and menu wiring (<code>ir.actions.act_window</code>, <code>ir.ui.menu</code>).</li>\n    <li>Form layout: <code>&lt;form&gt;</code> → <code>&lt;header&gt;</code> (buttons + statusbar), <code>&lt;sheet&gt;</code> (<code>oe_button_box</code>, title <code>h1</code>, <code>oe_title</code>), <code>&lt;chatter/&gt;</code> (messages + activities, needs mail dependency).</li>\n    <li>Organizing fields: <code>&lt;group&gt;</code> and nested groups for two-column layouts, <code>&lt;notebook&gt;</code> with <code>&lt;page&gt;</code> tabs, <code>invisible</code>/<code>readonly</code> attrs, <code>groups=</code> for visibility by access group.</li>\n    <li>List views: <code>&lt;tree&gt;</code> (<code>&lt;list&gt;</code>) columns, <code>optional=\"show/hide\"</code> for user-togglable columns, <code>decoration-info/success/danger/muted</code> with expressions for row coloring, <code>default_order</code>, <code>editable</code> inline editing.</li>\n    <li>Buttons: <code>type=\"object\"</code> calls a model method on the record; <code>type=\"action\"</code> triggers an <code>ir.actions</code>; <code>confirm</code>, <code>class</code> (oe_highlight), <code>invisible</code> attrs; smart buttons (stat buttons) in the button box.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Build a complete form view for your task model — header with a \"Mark Done\" object button, sheet with title, two-column groups, a notebook (General / Time Entries / Notes pages), chatter at the bottom — plus a list view with two optional columns and a red decoration for overdue deadlines.</p>\n</div>",
            },
        ],
    },
    {
        'name': "Search Views, Filters & Group By",
        'lessons': [
            {
                'name': "Search Views, Filters & Group By",
                'hours': 1.0,
                'level': "Intermediate",
                'summary': "Level: Intermediate | Duration: ~1h. Search view architecture: fields, filters with domains, group-by options, and favorite searches — exercise: 3 custom filters + a group-by.",
                'html': "<div class=\"prospire-lesson\">\n  <p>A good search view makes a module feel professional. It is also mostly declarative XML.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Search view anatomy: <code>&lt;search&gt;</code> with <code>&lt;field name=\"...\"&gt;</code> entries (quick search targets, with <code>filter_domain</code> for custom matching), <code>&lt;separator/&gt;</code> for UI grouping.</li>\n    <li>Filters: <code>&lt;filter name=\"...\" string=\"...\" domain=\"[...]\"/&gt;</code>; combining multiple filters with OR/AND semantics; date filters with <code>date</code> attribute and period grouping.</li>\n    <li>Group by: <code>&lt;filter name=\"groupby_...\" context=\"{'group_by': 'field'}\"/&gt;</code>; grouping by date fields with <code>date_stop</code> style intervals; multiple group-by levels.</li>\n    <li>Action integration: <code>search_view_id</code>, context-driven defaults (<code>search_default_filtername</code>), and the favorites users save themselves.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>For your task model add a search view with: quick search on title and assigned user; three filters — \"My Tasks\" (assigned to current user), \"Overdue\" (deadline &lt; today, not done), \"High Priority\" (priority in high/critical); and group-bys by Assignee, Project and Month (deadline:month). Set \"My Tasks\" as default via search_default in the action context.</p>\n</div>",
            },
        ],
    },
    {
        'name': "View Inheritance & Module Extension",
        'lessons': [
            {
                'name': "View Inheritance & Module Extension",
                'hours': 1.5,
                'level': "Advanced",
                'summary': "Level: Advanced | Duration: ~1.5h. Extending native views with inherit_id and xpath positions, and the difference between _inherit (model extension) and _inherits (delegation inheritance). Exercise: add a custom field to the native Sale Order form.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Real projects rarely build from scratch — they extend. This lesson is the safe way to customize native Odoo.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>View inheritance: a new <code>ir.ui.view</code> with <code>&lt;field name=\"inherit_id\" ref=\"sale.view_order_form\"/&gt;</code> and <code>&lt;field name=\"arch\"&gt;</code> containing <code>&lt;xpath&gt;</code> nodes.</li>\n    <li>xpath positions: <code>position=\"inside\"</code> (default — append into matched node), <code>before</code> / <code>after</code> (siblings), <code>replace</code> (swap the node; keep it safe with minimal targets), <code>attributes</code> (patch attrs like invisible/readonly in place).</li>\n    <li>Writing robust xpath expressions: target by <code>name</code> attribute or stable structure; why position-based paths break across versions; checking the final combined arch with developer mode's \"view inheritance\" debug.</li>\n    <li>Model extension: <code>_inherit = 'sale.order'</code> adds fields/methods to the existing model (same table); <code>_inherits = {'res.partner': 'partner_id'}</code> creates a new model delegating to another (new table, copied columns conceptually) — when each is appropriate.</li>\n    <li>Extension etiquette: never edit native XML directly; prefer attributes-position patches; keep custom modules upgrade-safe.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Create module <code>sale_order_custom</code> that adds a <code>x_client_reference</code> Char field to <code>sale.order</code> via <code>_inherit</code>, shows it in the native Sale Order form (after the Customer field) and list view (optional column) via xpath inheritance, and survives an upgrade with no other changes.</p>\n</div>",
            },
        ],
    },
    {
        'name': "Business Methods, Workflows & Status Bars",
        'lessons': [
            {
                'name': "Business Methods, Workflows & Status Bars",
                'hours': 1.5,
                'level': "Intermediate",
                'summary': "Level: Intermediate | Duration: ~1.5h. State fields and statusbar_visible, action_confirm/done/cancel method conventions, header buttons, and message_post() for the chatter — exercise: a 3-stage approval workflow.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Documents in Odoo live through states: draft → confirmed → done, or cancelled. Build that machinery yourself.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>State fields: <code>state = fields.Selection([...], default='draft', tracking=True)</code>; <code>tracking=True</code> logs changes to the chatter automatically.</li>\n    <li>Status bar widget in the header: <code>&lt;field name=\"state\" widget=\"statusbar\" statusbar_visible=\"draft,confirmed,done\"/&gt;</code>; clicking visible states to jump (with <code>statusbar_colors</code> legacy note).</li>\n    <li>Transition methods: the <code>action_confirm()</code> / <code>action_done()</code> / <code>action_cancel()</code> naming convention; writing <code>{'state': 'confirmed'}</code>; validating preconditions with <code>UserError</code>.</li>\n    <li>Header buttons: <code>&lt;button name=\"action_confirm\" type=\"object\" string=\"Confirm\" class=\"oe_highlight\" invisible=\"state != 'draft'\"/&gt;</code>; button visibility driven by state attrs.</li>\n    <li>Communication: <code>message_post(body=..., subtype_xmlid=...)</code> to document transitions in the chatter; <code>activity_schedule()</code> for follow-ups.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Give your task model a 3-stage approval flow — Draft → Approved → Done, plus Cancelled from any non-done state: statusbar with visible states, header buttons with proper invisibility, precondition checks (e.g. cannot approve without an assignee) raising UserError, and a message_post entry on every transition.</p>\n</div>",
            },
        ],
    },
    {
        'name': "Wizards (TransientModel)",
        'lessons': [
            {
                'name': "Wizards (TransientModel)",
                'hours': 1.5,
                'level': "Intermediate",
                'summary': "Level: Intermediate | Duration: ~1.5h. TransientModel lifecycle, dialog forms, context passing from the active record, and returning actions — exercise: a 'Send Quotation' wizard.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Wizards collect user input for a one-shot action without cluttering your real models.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li><code>models.TransientModel</code>: same fields/API as Model, but rows live in a temporary table and are vacuumed automatically (<code>_transient_max_hours</code>/<code>_transient_max_count</code>).</li>\n    <li>Wizard structure: model file, a form view with <code>&lt;form&gt;</code> without sheet/chatter, footer buttons (<code>class=\"btn-primary\"</code> for the action, <code>special=\"cancel\"</code> for discard), and an <code>ir.actions.act_window</code> with <code>target=\"new\"</code> for the dialog.</li>\n    <li>Context passing: <code>active_id</code>/<code>active_ids</code>/<code>active_model</code> from the calling view; <code>default_&lt;field&gt;</code> keys prefilling wizard fields; reading them safely with <code>self.env.context</code>.</li>\n    <li>Wizard action methods: validating input, doing the work on real records (<code>self.env[model].browse(ids)</code>), then <code>return {'type': 'ir.actions.act_window_close'}</code> — or return a window action to open what was created.</li>\n    <li>Multi-record wizards and report-launching wizards; common mistakes (storing computed defaults at class level, forgetting sudo for privileged operations).</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Build a \"Send Quotation\" wizard: opened from sale orders (active_ids), fields for a custom subject and message, a \"Send by Email\" button that posts the message to each order's chatter (and marks them sent), and a cancel button. Handle both single and multiple selected orders.</p>\n</div>",
            },
        ],
    },
    {
        'name': "Security — Groups, Access Rights & Record Rules",
        'lessons': [
            {
                'name': "Security — Groups, Access Rights & Record Rules",
                'hours': 1.5,
                'level': "Advanced",
                'summary': "Level: Advanced | Duration: ~1.5h. ir.model.access.csv, res.groups, ir.rule record rules, and groups= in views — exercise: managers see everything, users see only their own records.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Security in Odoo is four layers. Miss one and your data is either open to everyone or hidden from everyone.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Access rights (ACL): <code>security/ir.model.access.csv</code> columns (id, name, model_id:id, group_id:id, perm_read/write/create/unlink); the wildcard group for public/portal cases; listing models in the manifest's data list in dependency order.</li>\n    <li>Groups: <code>res.groups</code> records in a <code>security/*.xml</code> file; categories (<code>ir.module.category</code>); implied groups (user → manager); putting users in groups via the settings form.</li>\n    <li>Record rules (<code>ir.rule</code>): per-group domain filters applied invisibly to every search/read/write; global vs group rules; the manager-sees-all / user-sees-own pattern; multi-company rules as the reference example.</li>\n    <li>Field- and view-level security: <code>groups_id</code> on fields and <code>groups=\"...\"</code> on view elements; <code>groups=\"base.group_no_one\"</code> for developer-mode-only fields.</li>\n    <li>Debugging: effective permissions with <code>--log-level=debug_rpc</code> habits, \"Access Denied\" tracebacks, checking rules in developer mode.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>For your task module define \"Task User\" and \"Task Manager\" groups with proper ACLs; add a record rule so users see only tasks where they are the assignee (or creator), while managers see all; hide a \"Cost\" field from users via <code>groups=</code> in the form view. Verify by logging in as each.</p>\n</div>",
            },
        ],
    },
    {
        'name': "QWeb Reports — PDF & Print Layouts",
        'lessons': [
            {
                'name': "QWeb Reports — PDF & Print Layouts",
                'hours': 1.5,
                'level': "Advanced",
                'summary': "Level: Advanced | Duration: ~1.5h. ir.actions.report, QWeb directives (t-if/t-foreach/t-field/t-call), headers/footers/logo, and print SCSS — exercise: a branded PDF.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Every PDF Odoo prints is a QWeb template rendered to HTML and converted by wkhtmltopdf. Learn to design your own.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Report wiring: <code>&lt;record model=\"ir.actions.report\"&gt;</code> with <code>model</code>, <code>report_type=\"qweb-pdf\"</code>, <code>report_name</code> (dotted template name), <code>report_file</code>, <code>print_report_name</code>; the Print menu appears automatically.</li>\n    <li>QWeb template: <code>&lt;template id=\"report_task_document\"&gt;</code> and the wrapping <code>t-call=\"web.html_container\"</code> + <code>t-call=\"web.external_layout\"</code>; the <code>t-foreach=\"docs\"</code> loop and <code>t-esc/t-field/t-raw</code> output directives.</li>\n    <li>Logic in templates: <code>t-if</code>, <code>t-elif/t-else</code>, <code>t-set</code> variables, <code>t-call</code> sub-templates, <code>t-attf-class</code> dynamic attributes; calling model methods with <code>t-field</code> widget options (date, monetary, contact).</li>\n    <li>Paper &amp; layout: <code>report.paperformat</code> records (A4/Letter, margins, header spacing), company header/footer/logo via the external layout and <code>web.layout</code> inheritance, <code>webkit header</code> per-report override.</li>\n    <li>Print styling: report assets in the manifest (<code>web.report_assets_common</code>) with dedicated SCSS; wkhtmltopdf limitations (no flexbox gaps, use tables and Bootstrap grid carefully).</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Create a branded \"Task Summary\" PDF: company logo and header via external_layout, task title/state/deadline/assignee table, a time-entries section with totals, a footer with page numbers and your company tagline, styled with a small print SCSS file using the ProspireNext purple (#6D28D9).</p>\n</div>",
            },
        ],
    },
    {
        'name': "Scheduled Actions & Automated Rules",
        'lessons': [
            {
                'name': "Scheduled Actions & Automated Rules",
                'hours': 1.5,
                'level': "Advanced",
                'summary': "Level: Advanced | Duration: ~1.5h. ir.cron scheduled actions, base.automation rules, server actions and email templates — exercise: a reminder email 3 days before the deadline.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Let the system work while nobody is logged in: cron jobs, automated rules and templated emails.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Scheduled actions (<code>ir.cron</code>): XML record with <code>model_id</code>, <code>code</code> or <code>function</code> call, <code>interval_number/interval_type</code>, <code>nextcall</code>, <code>numbercall</code>, <code>doall</code>; user the job runs as; avoiding overlap and long transactions.</li>\n    <li>Automated rules (<code>base.automation</code>, Automation app): triggers on create/write/delete or on time conditions (<code>delay_after_field</code> pattern: \"3 days before deadline\"); filter domains; executed server actions.</li>\n    <li>Server actions (<code>ir.actions.server</code>): action types (Execute Python Code, Create/Update Record, Send Email, Add Followers); evaluation context (<code>records</code>, <code>env</code>, <code>log()</code>); reusable named actions callable from buttons/automations.</li>\n    <li>Email templates (<code>mail.template</code>): <code>subject</code>, <code>email_to</code> with placeholders, QWeb/HTML body with <code>${object.field}</code> placeholders and <code>t-field</code> rendering; sending via <code>message_post_with_template</code> or the automation.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Build a deadline reminder: an automated rule on tasks that triggers 3 days before the deadline for unfinished tasks, sending a branded email template to the assignee (with task name, deadline and a link); log every send in the chatter; test by backdating a task's deadline.</p>\n</div>",
            },
        ],
    },
    {
        'name': "External API & JSON-RPC Deep Dive",
        'lessons': [
            {
                'name': "External API & JSON-RPC Deep Dive",
                'hours': 1.5,
                'level': "Advanced",
                'summary': "Level: Advanced | Duration: ~1.5h. /web/dataset/call_kw internals, xmlrpc.client clients, custom HTTP controllers, and a webhook receiver — exercise: GET /api/orders endpoint.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Odoo is not just an app — it is a platform. Open it up safely to other systems.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>The internal JSON-RPC endpoints: <code>/web/dataset/call_kw</code> (model + method + args/kwargs), <code>/web/dataset/search_read</code>, <code>/web/session/authenticate</code>, <code>/jsonrpc</code> envelope format; what the web client itself uses.</li>\n    <li>External clients: <code>xmlrpc.client</code> (common/models endpoints), Python <code>requests</code> against JSON-RPC, official API keys per user (Settings → Users → API keys) for scripted access.</li>\n    <li>Custom HTTP controllers: <code>from odoo import http</code>, <code>@http.route('/api/...', type='json'|'http', auth='public'|'user'|'none', methods=[...], csrf=False)</code>; <code>request.env['model']</code>, returning JSON with <code>request.make_response</code>.</li>\n    <li>Securing public routes: token/API-key checks, rate limiting considerations, never leak tracebacks, CORS for browser clients.</li>\n    <li>Webhook receiver pattern: an <code>auth='none'</code> POST route that validates a shared secret and creates/updates records; queuing heavy work via <code>env['ir.cron']._trigger()</code> or immediate processing for light payloads.</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Create a controller module exposing <code>GET /api/orders?partner_email=...</code> (JSON list of that customer's confirmed sale orders with lines, secured by an API key header) and <code>POST /api/webhook/payment</code> that validates a secret and marks the matching order as paid. Document both with curl examples.</p>\n</div>",
            },
        ],
    },
    {
        'name': "On-Prem & Cloud Deployment",
        'lessons': [
            {
                'name': "On-Prem & Cloud Deployment",
                'hours': 2.0,
                'level': "Advanced",
                'summary': "Level: Advanced | Duration: ~2h. Ubuntu 22.04 + PostgreSQL + Nginx + systemd, reverse proxy and SSL with Certbot, Hetzner/DigitalOcean/AWS choices, production odoo.conf, and pg_dump backups. Exercise: deploy your module to a VPS with Nginx + SSL.",
                'html': "<div class=\"prospire-lesson\">\n  <p>Development is done when it runs in production. Here is the full production stack, end to end.</p>\n  <h4>Key topics</h4>\n  <ul>\n    <li>Server baseline: Ubuntu 22.04 LTS setup (users, SSH hardening, ufw), installing PostgreSQL and creating the Odoo role/database.</li>\n    <li>Odoo as a systemd service: unit file for <code>odoo-bin -c /etc/odoo.conf</code>, restart policies, journald logs, running under a dedicated user.</li>\n    <li>Nginx reverse proxy: proxy_pass to Odoo's port, <code>proxy_set_header</code> directives for X-Forwarded-* and Host, client_max_body_size, serving static files directly, gzip.</li>\n    <li>SSL with Certbot: <code>certbot --nginx</code>, auto-renewal timers, HTTP→HTTPS redirect, HSTS basics.</li>\n    <li>Cloud providers compared: Hetzner (price/performance), DigitalOcean (simplicity), AWS (scale, complexity); sizing for small/medium installs.</li>\n    <li>Production <code>odoo.conf</code>: <code>workers</code> (≈ CPU×2), <code>max_cron_threads</code>, <code>limit_memory_soft/hard</code>, <code>limit_time_cpu/real</code>, <code>dbfilter</code>, <code>proxy_mode = True</code>, logging.</li>\n    <li>Backups: <code>pg_dump</code> (custom format), filestore/ir_attachment sync, retention policy, restore drills; off-server copies (object storage or another host).</li>\n  </ul>\n  <h4>Exercise / deliverable</h4>\n  <p>Deploy your task module to a VPS: Ubuntu 22.04, PostgreSQL, Odoo behind Nginx with a Certbot SSL certificate on a real domain, systemd auto-start, production-tuned odoo.conf, and a nightly pg_dump + filestore backup script with 7-day retention. Verify HTTPS access and a test restore.</p>\n</div>",
            },
        ],
    },
    {
        'name': "Capstone — Full Custom Module Build",
        'lessons': [
            {
                'name': "Capstone — Full Custom Module Build",
                'hours': 6.0,
                'level': "Advanced",
                'summary': "Level: Advanced | Duration: ~6h. Build a Service Request Management module end-to-end: 8+ fields, form/list/search views, 3-stage workflow, security rules, QWeb PDF, auto-email, FastAPI endpoint, and a staging deployment.",
                'html': "<div class=\"prospire-lesson\">\n  <p>The capstone integrates every section of this course into one deliverable: a production-shaped custom module for managing service requests.</p>\n  <h4>Requirements</h4>\n  <ul>\n    <li><strong>Model:</strong> <code>service.request</code> with 8+ fields across types — Char (reference, title), Text (description), Selection (category: it/support/maintenance; priority), Date (deadline), Float (estimated/actual hours), Many2one (customer → res.partner, assigned engineer → res.users), Many2many (tags), Boolean (billable), plus a stored computed field and a constraint from Section 7.</li>\n    <li><strong>Views:</strong> form with header buttons, statusbar, groups, notebook pages and chatter; list with optional columns and decorations; search view with 3+ filters and group-bys (Sections 9–10).</li>\n    <li><strong>Workflow:</strong> 3-stage lifecycle (New → In Progress → Done) with Cancel, precondition validation and message_post logging (Section 12).</li>\n    <li><strong>Security:</strong> user/manager groups, ACLs, and a record rule limiting users to their own requests (Section 14).</li>\n    <li><strong>Reporting:</strong> branded QWeb PDF summary of a request (Section 15).</li>\n    <li><strong>Automation:</strong> reminder email 3 days before the deadline, and a weekly digest cron to the manager (Section 16).</li>\n    <li><strong>Integration:</strong> FastAPI endpoint <code>POST /service-requests</code> creating a request in Odoo over RPC (Section 3); plus a native <code>GET /api/service-requests</code> controller (Section 17).</li>\n    <li><strong>Deployment:</strong> install on a staging VPS behind Nginx + SSL with backups configured (Section 18).</li>\n  </ul>\n  <h4>Deliverable</h4>\n  <p>A module repository with README (install, configure, API docs), clean commit history, the module running on a public staging URL, and a short demo video or screenshots of each requirement working.</p>\n</div>",
            },
        ],
    },
]
